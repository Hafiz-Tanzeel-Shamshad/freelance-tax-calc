/* ───────────────────────────────────────────────
   tax-calculator-core.js — 2026 US Tax Logic
   Shared across all FreelanceTaxCalc calculators
   ─────────────────────────────────────────────── */

/* 2026 Tax Parameters */
var TAX_PARAMS_2026 = {
  SE_RATE: 0.153,        // 12.4% SS + 2.9% Medicare
  SS_RATE: 0.124,
  MEDICARE_RATE: 0.029,
  ADD_MEDICARE_RATE: 0.009,
  SS_WAGE_BASE: 184500,
  SE_BASE_FACTOR: 0.9235,
  SE_DEDUCTION_RATE: 0.5,
  STANDARD_DEDUCTION: {
    single: 16100,
    married: 32200,
    hoh: 24150
  },
  // Medicare surtax thresholds
  ADD_MEDICARE_THRESHOLD: {
    single: 200000,
    mfj: 250000,
    mfs: 125000,
    hoh: 200000
  },
  /* Tax Brackets — Single */
  BRACKETS_SINGLE: [
    { upper: 12400,   rate: 0.10 },
    { upper: 50400,   rate: 0.12 },
    { upper: 105700,  rate: 0.22 },
    { upper: 201775,  rate: 0.24 },
    { upper: 256225,  rate: 0.32 },
    { upper: 640600,  rate: 0.35 },
    { upper: Infinity, rate: 0.37 }
  ],
  /* Tax Brackets — Married Filing Jointly */
  BRACKETS_MARRIED: [
    { upper: 24800,   rate: 0.10 },
    { upper: 100800,  rate: 0.12 },
    { upper: 211400,  rate: 0.22 },
    { upper: 403550,  rate: 0.24 },
    { upper: 512450,  rate: 0.32 },
    { upper: 768700,  rate: 0.35 },
    { upper: Infinity, rate: 0.37 }
  ],
  /* Tax Brackets — Head of Household */
  BRACKETS_HOH: [
    { upper: 17700,   rate: 0.10 },
    { upper: 67450,   rate: 0.12 },
    { upper: 107450,  rate: 0.22 },
    { upper: 205200,  rate: 0.24 },
    { upper: 260550,  rate: 0.32 },
    { upper: 651400,  rate: 0.35 },
    { upper: Infinity, rate: 0.37 }
  ]
};

/* Map filing status to param key */
function _statusKey(status) {
  if (status === 'mfj' || status === 'married') return 'married';
  if (status === 'hoh') return 'hoh';
  return 'single';
}

/* Get standard deduction */
function getStandardDeduction(filingStatus) {
  return TAX_PARAMS_2026.STANDARD_DEDUCTION[_statusKey(filingStatus)];
}

/* Get 2026 brackets */
function getBrackets2026(filingStatus) {
  var key = _statusKey(filingStatus);
  if (key === 'married') return TAX_PARAMS_2026.BRACKETS_MARRIED;
  if (key === 'hoh') return TAX_PARAMS_2026.BRACKETS_HOH;
  return TAX_PARAMS_2026.BRACKETS_SINGLE;
}

/* Calculate progressive federal income tax */
function calculateFederalIncomeTax(taxableIncome, filingStatus) {
  if (taxableIncome <= 0) return 0;
  var brackets = getBrackets2026(filingStatus);
  var tax = 0;
  var prev = 0;
  for (var i = 0; i < brackets.length; i++) {
    var bracket = brackets[i];
    if (taxableIncome <= prev) break;
    var chunk = Math.min(taxableIncome, bracket.upper) - prev;
    if (chunk > 0) tax += chunk * bracket.rate;
    prev = bracket.upper;
  }
  return tax;
}

/* Calculate additional Medicare (0.9% surtax) */
function calculateAdditionalMedicare(magi, filingStatus) {
  var key = _statusKey(filingStatus);
  var threshold = TAX_PARAMS_2026.ADD_MEDICARE_THRESHOLD[key];
  if (!threshold) return 0;
  return magi > threshold ? (magi - threshold) * TAX_PARAMS_2026.ADD_MEDICARE_RATE : 0;
}

/*
 * Core Self-Employment Tax Calculation
 * Handles SE tax, SE deduction, and federal income tax
 */
function calculateSelfEmploymentTax(grossIncome, expenses, filingStatus, extraIncome) {
  if (filingStatus === undefined) filingStatus = 'single';
  if (extraIncome === undefined) extraIncome = 0;

  var netProfit = Math.max(0, grossIncome - expenses);

  // SE tax base: 92.35% of net profit
  var seBase = netProfit * TAX_PARAMS_2026.SE_BASE_FACTOR;

  // Social Security: 12.4% up to wage base
  var socialSecurity = Math.min(seBase, TAX_PARAMS_2026.SS_WAGE_BASE) * TAX_PARAMS_2026.SS_RATE;

  // Medicare: 2.9% on all SE base
  var medicare = seBase * TAX_PARAMS_2026.MEDICARE_RATE;

  // Additional Medicare: 0.9% on MAGI over threshold (includes extra income)
  var magi = netProfit + extraIncome;
  var addMedicare = calculateAdditionalMedicare(magi, filingStatus);

  var selfEmploymentTax = socialSecurity + medicare + addMedicare;

  // SE tax deduction: 50% of total SE tax (including additional Medicare)
  var seTaxDeduction = selfEmploymentTax * TAX_PARAMS_2026.SE_DEDUCTION_RATE;

  // Adjusted gross income (simplified)
  var agi = netProfit - seTaxDeduction;

  // Taxable income after standard deduction
  var stdDed = getStandardDeduction(filingStatus);
  var taxableIncome = Math.max(0, agi - stdDed);

  // Federal income tax
  var federalTax = calculateFederalIncomeTax(taxableIncome, filingStatus);

  var totalTax = federalTax + selfEmploymentTax;
  var takeHome = netProfit - totalTax;

  return {
    netProfit: netProfit,
    seBase: seBase,
    socialSecurity: Math.round(socialSecurity),
    medicare: Math.round(medicare),
    addMedicare: Math.round(addMedicare),
    selfEmploymentTax: Math.round(selfEmploymentTax),
    seTaxDeduction: Math.round(seTaxDeduction),
    agi: Math.round(agi),
    stdDed: stdDed,
    taxableIncome: Math.round(taxableIncome),
    federalIncomeTax: Math.round(federalTax),
    totalTax: Math.round(totalTax),
    takeHomePay: Math.round(takeHome),
    effectiveTaxRate: totalTax > 0 && netProfit > 0 ?
      ((totalTax / netProfit) * 100).toFixed(1) + '%' : '0%'
  };
}

/*
 * Quarterly Tax Estimator
 */
function calculateQuarterlyTaxes(annualNetProfit, expenses, filingStatus) {
  var annual = calculateSelfEmploymentTax(annualNetProfit, expenses, filingStatus);
  var quarterlyPayment = Math.ceil(annual.totalTax / 4);

  return {
    totalTax: annual.totalTax,
    quarterlyPayment: quarterlyPayment,
    seTax: annual.selfEmploymentTax,
    federalTax: annual.federalIncomeTax,
    taxableIncome: annual.taxableIncome,
    dueDates: [
      { label: 'Q1', date: 'April 15, 2026' },
      { label: 'Q2', date: 'June 15, 2026' },
      { label: 'Q3', date: 'September 15, 2026' },
      { label: 'Q4', date: 'January 15, 2027' }
    ],
    safeHarborNote: 'To avoid penalties, pay at least 90% of this year\'s tax or 100% of last year\'s tax (110% if AGI > $150,000).'
  };
}

/*
 * 1099 Tax Calculator (with state tax)
 */
function calculate1099Tax(gross1099, expenses, filingStatus, stateTaxRate) {
  if (stateTaxRate === undefined) stateTaxRate = 0;
  var result = calculateSelfEmploymentTax(gross1099, expenses, filingStatus);
  var stateTax = result.taxableIncome * stateTaxRate;
  return {
    netProfit: result.netProfit,
    selfEmploymentTax: result.selfEmploymentTax,
    federalIncomeTax: result.federalIncomeTax,
    stateIncomeTax: Math.round(stateTax),
    totalTax: Math.round(result.totalTax + stateTax),
    takeHomePay: Math.round(result.netProfit - result.totalTax - stateTax)
  };
}

/*
 * Gig Worker / Side Hustle Tax Calculator
 * Coordinates W-2 + 1099 income correctly
 */
function calculateGigWorkerTax(w2Income, w2Pretax, gigIncome, gigExpenses, filingStatus, stateTaxRate) {
  if (stateTaxRate === undefined) stateTaxRate = 0;

  var netGig = Math.max(0, gigIncome - gigExpenses);
  var adjW2 = Math.max(0, w2Income - w2Pretax);
  var totalIncome = adjW2 + netGig;

  var stdDed = getStandardDeduction(filingStatus);
  var brackets = getBrackets2026(filingStatus);

  // WITHOUT side hustle
  var taxableWo = Math.max(0, adjW2 - stdDed);
  var fedWo = calculateFederalIncomeTax(taxableWo, filingStatus);
  var stateWo = taxableWo * stateTaxRate;
  var ssW2wo = Math.min(adjW2, TAX_PARAMS_2026.SS_WAGE_BASE) * TAX_PARAMS_2026.SS_RATE;
  var mcW2wo = adjW2 * TAX_PARAMS_2026.MEDICARE_RATE;
  var addMcW2wo = calculateAdditionalMedicare(adjW2, filingStatus);
  var ficaWo = ssW2wo + mcW2wo + addMcW2wo;
  var totalWo = Math.round(fedWo + stateWo + ficaWo);

  // WITH side hustle
  // SE tax on gig income (coordinate SS with W-2)
  var seBase = netGig * TAX_PARAMS_2026.SE_BASE_FACTOR;
  var w2SsBase = Math.min(adjW2, TAX_PARAMS_2026.SS_WAGE_BASE);
  var seSsBase = Math.min(seBase, Math.max(0, TAX_PARAMS_2026.SS_WAGE_BASE - w2SsBase));
  var seSs = seSsBase * TAX_PARAMS_2026.SS_RATE;
  var seMc = seBase * TAX_PARAMS_2026.MEDICARE_RATE;
  var addMcSe = calculateAdditionalMedicare(totalIncome, filingStatus);
  // Avoid double-counting additional Medicare (already in ficaWo if W-2 triggered it)
  var addMcSeOnly = Math.max(0, addMcSe - addMcW2wo);
  var seTax = seSs + seMc + addMcSeOnly;
  var seDed = seTax * TAX_PARAMS_2026.SE_DEDUCTION_RATE;

  var agiWith = adjW2 + netGig - seDed;
  var taxableWith = Math.max(0, agiWith - stdDed);

  // QBI: 20% of gig net, capped at 20% of taxable income before QBI
  var qbi = Math.min(netGig * 0.20, taxableWith);
  taxableWith = Math.max(0, taxableWith - qbi);

  var fedWith = calculateFederalIncomeTax(taxableWith, filingStatus);
  var stateWith = taxableWith * stateTaxRate;
  // W-2 FICA with side hustle
  var ssW2w = Math.min(adjW2, TAX_PARAMS_2026.SS_WAGE_BASE) * TAX_PARAMS_2026.SS_RATE;
  var mcW2w = adjW2 * TAX_PARAMS_2026.MEDICARE_RATE;
  var ficaW2w = ssW2w + mcW2w + addMcW2wo;
  var totalWith = Math.round(fedWith + stateWith + ficaW2w + seTax);

  var additionalTax = totalWith - totalWo;
  var netFromSide = netGig - additionalTax;

  return {
    netGig: netGig,
    seTax: Math.round(seTax),
    additionalTax: additionalTax,
    netFromSide: Math.round(netFromSide),
    totalWithout: totalWo,
    totalWith: totalWith,
    taxableWithout: Math.round(taxableWo),
    taxableWith: Math.round(taxableWith),
    stateWithout: Math.round(stateWo),
    stateWith: Math.round(stateWith),
    qbi: Math.round(qbi),
    fedWithout: Math.round(fedWo),
    fedWith: Math.round(fedWith),
    mustFile: netGig > 400
  };
}

/*
 * 1099 vs W-2 Comparison Calculator
 */
function compare1099vsW2(w2Salary, w2Benefits, c1099Rate, c1099Expenses, filingStatus, stateTaxRate, healthInsurance, retirementContrib) {
  if (healthInsurance === undefined) healthInsurance = 0;
  if (retirementContrib === undefined) retirementContrib = 0;

  var stdDed = getStandardDeduction(filingStatus);
  var brackets = getBrackets2026(filingStatus);

  // W-2
  var taxableW2 = Math.max(0, w2Salary - stdDed);
  var fedW2 = calculateFederalIncomeTax(taxableW2, filingStatus);
  var stateW2 = taxableW2 * stateTaxRate;
  var ssW2 = Math.min(w2Salary, TAX_PARAMS_2026.SS_WAGE_BASE) * TAX_PARAMS_2026.SS_RATE;
  var mcW2 = w2Salary * TAX_PARAMS_2026.MEDICARE_RATE;
  var addMcW2 = calculateAdditionalMedicare(w2Salary, filingStatus);
  var ficaW2 = ssW2 + mcW2 + addMcW2;
  var takehomeW2 = w2Salary - fedW2 - stateW2 - ficaW2;

  // 1099
  var net1099 = Math.max(0, c1099Rate - c1099Expenses);
  // SE tax
  var seBase = net1099 * TAX_PARAMS_2026.SE_BASE_FACTOR;
  var seSs = Math.min(seBase, TAX_PARAMS_2026.SS_WAGE_BASE) * TAX_PARAMS_2026.SS_RATE;
  var seMc = seBase * TAX_PARAMS_2026.MEDICARE_RATE;
  var seAddMc = calculateAdditionalMedicare(c1099Rate, filingStatus);
  var seTax = seSs + seMc + seAddMc;
  var seDed = seTax * TAX_PARAMS_2026.SE_DEDUCTION_RATE;

  var agi1099 = net1099 - seDed - healthInsurance - retirementContrib;
  var taxable1099 = Math.max(0, agi1099 - stdDed);
  var qbi = Math.min(net1099 * 0.20, taxable1099);
  taxable1099 = Math.max(0, taxable1099 - qbi);

  var fed1099 = calculateFederalIncomeTax(taxable1099, filingStatus);
  var state1099 = taxable1099 * stateTaxRate;
  var takehome1099 = c1099Rate - c1099Expenses - seTax - fed1099 - state1099 - healthInsurance - retirementContrib;

  return {
    w2TakeHome: Math.round(takehomeW2),
    fedW2: Math.round(fedW2),
    stateW2: Math.round(stateW2),
    ficaW2: Math.round(ficaW2),
    c1099TakeHome: Math.round(takehome1099),
    fed1099: Math.round(fed1099),
    state1099: Math.round(state1099),
    seTax: Math.round(seTax),
    qbi: Math.round(qbi),
    difference: Math.round(takehome1099 - takehomeW2),
    winner: takehome1099 > takehomeW2 ? '1099' : 'W-2'
  };
}

/* ───────────────────────────────────────────────
   Federal Income Tax + Refund Estimator
   ─────────────────────────────────────────────── */
function calculateFederalTaxRefund(grossIncome, preTaxDeductions, credits, filingStatus, taxWithheld) {
  if (taxWithheld === undefined) taxWithheld = 0;
  var stdDed = getStandardDeduction(filingStatus);
  var agi = Math.max(0, grossIncome - preTaxDeductions);
  var taxableIncome = Math.max(0, agi - stdDed);
  var federalTax = calculateFederalIncomeTax(taxableIncome, filingStatus);
  var netTax = Math.max(0, federalTax - credits);
  var refundOrOwed = taxWithheld - netTax;

  return {
    grossIncome: Math.round(grossIncome),
    standardDeduction: stdDed,
    taxableIncome: Math.round(taxableIncome),
    federalTaxLiability: Math.round(federalTax),
    credits: Math.round(credits),
    netTaxOwed: Math.round(netTax),
    taxWithheld: Math.round(taxWithheld),
    estimatedRefund: refundOrOwed > 0 ? Math.round(refundOrOwed) : 0,
    amountOwed: refundOrOwed < 0 ? Math.round(Math.abs(refundOrOwed)) : 0,
    effectiveRate: taxableIncome > 0 ? ((netTax / taxableIncome) * 100).toFixed(1) + '%' : '0%'
  };
}

/* ───────────────────────────────────────────────
   Tax Bracket Locator
   ─────────────────────────────────────────────── */
function findTaxBracket(income, filingStatus) {
  var brackets = getBrackets2026(filingStatus);
  var marginalRate = 0;
  var bracketUpper = 0;
  var bracketLower = 0;

  for (var i = 0; i < brackets.length; i++) {
    var prev = i > 0 ? brackets[i-1].upper : 0;
    if (income <= brackets[i].upper) {
      marginalRate = brackets[i].rate;
      bracketUpper = brackets[i].upper;
      bracketLower = prev;
      break;
    }
    if (i === brackets.length - 1) {
      marginalRate = brackets[i].rate;
      bracketUpper = Infinity;
      bracketLower = prev;
    }
  }

  var topOfPrev = i > 0 ? brackets[i-1].upper : 0;
  var taxInBracket = Math.max(0, Math.min(income, bracketUpper) - bracketLower) * marginalRate;

  return {
    marginalRate: (marginalRate * 100) + '%',
    marginalRateDecimal: marginalRate,
    bracketLower: bracketLower,
    bracketUpper: bracketUpper === Infinity ? Infinity : bracketUpper,
    bracketRange: bracketUpper === Infinity
      ? '$' + bracketLower.toLocaleString() + '+'
      : '$' + bracketLower.toLocaleString() + ' - $' + bracketUpper.toLocaleString(),
    taxInBracket: Math.round(taxInBracket)
  };
}

/* ───────────────────────────────────────────────
   Capital Gains Tax Calculator
   ─────────────────────────────────────────────── */
function calculateCapitalGains(shortTermGain, longTermGain, ordinaryIncome, filingStatus) {
  // Short-term gains are taxed as ordinary income
  var incomeWithoutST = ordinaryIncome;
  var incomeWithST = ordinaryIncome + shortTermGain;
  var taxWithoutST = calculateFederalIncomeTax(incomeWithoutST, filingStatus);
  var taxWithST = calculateFederalIncomeTax(incomeWithST, filingStatus);
  var shortTermTax = taxWithST - taxWithoutST;

  // Long-term capital gains rates: 0%, 15%, 20%
  // 2026 thresholds (single): 0% up to $47,025, 15% up to $518,900, 20% above
  var ltBrackets;
  if (filingStatus === 'married' || filingStatus === 'mfj') {
    ltBrackets = [
      { upper: 94050,   rate: 0.00 },
      { upper: 583750,  rate: 0.15 },
      { upper: Infinity, rate: 0.20 }
    ];
  } else if (filingStatus === 'hoh') {
    ltBrackets = [
      { upper: 63000,   rate: 0.00 },
      { upper: 551350,  rate: 0.15 },
      { upper: Infinity, rate: 0.20 }
    ];
  } else {
    ltBrackets = [
      { upper: 47025,   rate: 0.00 },
      { upper: 518900,  rate: 0.15 },
      { upper: Infinity, rate: 0.20 }
    ];
  }

  var totalIncome = ordinaryIncome + longTermGain;
  var ltRate = 0.20;
  for (var i = 0; i < ltBrackets.length; i++) {
    if (totalIncome <= ltBrackets[i].upper) {
      ltRate = ltBrackets[i].rate;
      break;
    }
  }

  var longTermTax = longTermGain * ltRate;
  var totalTax = shortTermTax + longTermTax;

  return {
    shortTermGain: Math.round(shortTermGain),
    longTermGain: Math.round(longTermGain),
    shortTermTax: Math.round(shortTermTax),
    longTermRate: (ltRate * 100) + '%',
    longTermTax: Math.round(longTermTax),
    totalCapitalGainsTax: Math.round(totalTax)
  };
}

/* ───────────────────────────────────────────────
   Canada Income Tax Estimator (Federal + Provincial)
   2026 federal brackets + progressive provincial rates
   ─────────────────────────────────────────────── */

// 2026 Federal brackets (indexed)
var FEDERAL_BRACKETS_2026 = [
  { upper: 58523,  rate: 0.14 },
  { upper: 117045, rate: 0.205 },
  { upper: 181440, rate: 0.26 },
  { upper: 258482, rate: 0.29 },
  { upper: Infinity, rate: 0.33 }
];

// Basic Personal Amount 2026 (approximate indexed value)
var CANADA_BPA_2026 = 17000;

// Provincial / Territorial progressive brackets (2025-2026 rates)
var PROVINCIAL_BRACKETS = {
  ON: [
    { upper: 53891,  rate: 0.0505 },
    { upper: 107785, rate: 0.0915 },
    { upper: 150000, rate: 0.1116 },
    { upper: 220000, rate: 0.1216 },
    { upper: Infinity, rate: 0.1316 }
  ],
  BC: [
    { upper: 50363,   rate: 0.0506 },
    { upper: 100728,  rate: 0.077  },
    { upper: 115648,  rate: 0.105  },
    { upper: 140430,  rate: 0.1229 },
    { upper: 190405,  rate: 0.147  },
    { upper: 265545,  rate: 0.168  },
    { upper: Infinity, rate: 0.205 }
  ],
  AB: [
    { upper: 61200,   rate: 0.08 },
    { upper: 154259,  rate: 0.10 },
    { upper: 185111,  rate: 0.12 },
    { upper: 246813,  rate: 0.13 },
    { upper: 370220,  rate: 0.14 },
    { upper: Infinity, rate: 0.15 }
  ],
  MB: [
    { upper: 36842,  rate: 0.108  },
    { upper: 79625,  rate: 0.1275 },
    { upper: Infinity, rate: 0.174 }
  ],
  NB: [
    { upper: 49958,   rate: 0.094 },
    { upper: 99916,   rate: 0.14  },
    { upper: 185064,  rate: 0.16  },
    { upper: Infinity, rate: 0.195 }
  ],
  NL: [
    { upper: 43198,   rate: 0.087 },
    { upper: 86395,   rate: 0.145 },
    { upper: 154244,  rate: 0.158 },
    { upper: 215943,  rate: 0.178 },
    { upper: Infinity, rate: 0.198 }
  ],
  NS: [
    { upper: 29590,  rate: 0.0879 },
    { upper: 59180,  rate: 0.1495 },
    { upper: 93000,  rate: 0.1667 },
    { upper: 150000, rate: 0.175  },
    { upper: Infinity, rate: 0.21  }
  ],
  PE: [
    { upper: 31984,  rate: 0.0965 },
    { upper: 63969,  rate: 0.1363 },
    { upper: 104000, rate: 0.1665 },
    { upper: Infinity, rate: 0.18  }
  ],
  QC: [
    { upper: 51780,   rate: 0.14   },
    { upper: 103545,  rate: 0.19   },
    { upper: 126000,  rate: 0.24   },
    { upper: Infinity, rate: 0.2575 }
  ],
  SK: [
    { upper: 52057,   rate: 0.105 },
    { upper: 148734,  rate: 0.125 },
    { upper: Infinity, rate: 0.145 }
  ],
  NT: [
    { upper: 50597,   rate: 0.059 },
    { upper: 101198,  rate: 0.086 },
    { upper: 164615,  rate: 0.122 },
    { upper: Infinity, rate: 0.1405 }
  ],
  NU: [
    { upper: 50877,   rate: 0.04 },
    { upper: 101754,  rate: 0.07 },
    { upper: 165429,  rate: 0.09 },
    { upper: Infinity, rate: 0.115 }
  ],
  YT: [
    { upper: 55867,   rate: 0.064 },
    { upper: 111733,  rate: 0.09  },
    { upper: 173205,  rate: 0.109 },
    { upper: 500000,  rate: 0.128 },
    { upper: Infinity, rate: 0.15  }
  ]
};

function calculateCanadaIncomeTax(grossIncome, province, deductions) {
  if (province === undefined) province = 'ON';
  if (deductions === undefined) deductions = 0;

  // Apply Basic Personal Amount + user deductions
  var bpa = CANADA_BPA_2026;
  var taxableIncome = Math.max(0, grossIncome - deductions - bpa);

  // Federal tax using progressive brackets
  var federalTax = 0;
  var prev = 0;
  for (var i = 0; i < FEDERAL_BRACKETS_2026.length; i++) {
    var b = FEDERAL_BRACKETS_2026[i];
    if (taxableIncome <= prev) break;
    var chunk = Math.min(taxableIncome, b.upper) - prev;
    if (chunk > 0) federalTax += chunk * b.rate;
    prev = b.upper;
  }

  // Provincial tax using progressive brackets
  var provincialTax = 0;
  var provBrackets = PROVINCIAL_BRACKETS[province] || PROVINCIAL_BRACKETS.ON;
  prev = 0;
  for (var p = 0; p < provBrackets.length; p++) {
    var pb = provBrackets[p];
    if (taxableIncome <= prev) break;
    var chunk = Math.min(taxableIncome, pb.upper) - prev;
    if (chunk > 0) provincialTax += chunk * pb.rate;
    prev = pb.upper;
  }

  var totalTax = Math.round(federalTax + provincialTax);
  var effectiveRate = grossIncome > 0 ? ((totalTax / grossIncome) * 100).toFixed(1) + '%' : '0%';

  return {
    taxableIncome: Math.round(taxableIncome),
    federalTax: Math.round(federalTax),
    provincialTax: Math.round(provincialTax),
    provRate: ((provincialTax / Math.max(1, taxableIncome)) * 100).toFixed(1) + '%',
    totalTax: totalTax,
    takeHome: Math.round(grossIncome - totalTax),
    effectiveRate: effectiveRate
  };
}

// Old Canada tax function kept for backward compatibility
var CANADA_PARAMS = {
  FED_BRACKETS: [
    { upper: 57375,  rate: 0.15 },
    { upper: 114750, rate: 0.205 },
    { upper: 177882, rate: 0.26 },
    { upper: 253414, rate: 0.29 },
    { upper: Infinity, rate: 0.33 }
  ],
  BASIC_PERSONAL: 16375,
  PROVINCIAL_RATES: {
    'AB': 0.10, 'BC': 0.05, 'MB': 0.12, 'NB': 0.14,
    'NL': 0.15, 'NS': 0.15, 'ON': 0.051, 'PE': 0.14,
    'QC': 0.14, 'SK': 0.115, 'NT': 0.059, 'NU': 0.04, 'YT': 0.064
  },
  CPP_RATE: 0.119,
  CPP_BASIC_EXEMPTION: 3500,
  CPP_MAX_PENSIONABLE: 73200
};

function calculateCanadaTax(income, province) {
  if (province === undefined) province = 'ON';
  var fedTax = 0;
  var prev = 0;
  for (var i = 0; i < CANADA_PARAMS.FED_BRACKETS.length; i++) {
    var b = CANADA_PARAMS.FED_BRACKETS[i];
    if (income <= prev) break;
    var chunk = Math.min(income, b.upper) - prev;
    if (chunk > 0) fedTax += chunk * b.rate;
    prev = b.upper;
  }
  var bpaCredit = CANADA_PARAMS.BASIC_PERSONAL * 0.15;
  fedTax = Math.max(0, fedTax - bpaCredit);
  var provRate = CANADA_PARAMS.PROVINCIAL_RATES[province] || 0.06;
  var provTax = income * provRate;
  var cppIncome = Math.max(0, income - CANADA_PARAMS.CPP_BASIC_EXEMPTION);
  var cpp = Math.min(cppIncome, CANADA_PARAMS.CPP_MAX_PENSIONABLE - CANADA_PARAMS.CPP_BASIC_EXEMPTION) * CANADA_PARAMS.CPP_RATE;
  var totalTax = Math.round(fedTax + provTax + cpp);
  var effectiveRate = income > 0 ? ((totalTax / income) * 100).toFixed(1) + '%' : '0%';
  return {
    income: Math.round(income),
    federalTax: Math.round(fedTax),
    provincialTax: Math.round(provTax),
    provRate: (provRate * 100) + '%',
    cpp: Math.round(cpp),
    totalTax: totalTax,
    takeHome: Math.round(income - totalTax),
    effectiveRate: effectiveRate
  };
}

/* ───────────────────────────────────────────────
   Canada RRSP Contribution Tax Savings Calculator
   ─────────────────────────────────────────────── */
var RRSP_MAX_2026 = 33810;

function calculateRRSPTaxSavings(earnedIncome, rrspContribution, marginalRate) {
  if (marginalRate === undefined) marginalRate = 0.30;
  var maxContribution = Math.min(RRSP_MAX_2026, earnedIncome * 0.18);
  var actualContrib = Math.min(rrspContribution, maxContribution);
  var taxSavings = actualContrib * marginalRate;

  return {
    maxAllowed: Math.round(maxContribution),
    contributed: Math.round(actualContrib),
    immediateTaxSavings: Math.round(taxSavings),
    note: "RRSP contribution reduces taxable income dollar-for-dollar."
  };
}

/* ───────────────────────────────────────────────
   Canada Self-Employed / Business Income Tax
   ─────────────────────────────────────────────── */
function calculateCanadaSelfEmployedTax(grossBusinessIncome, expenses, province) {
  if (expenses === undefined) expenses = 0;
  if (province === undefined) province = 'ON';
  var netIncome = Math.max(0, grossBusinessIncome - expenses);

  // Self-employed pay full CPP (employee + employer portions combined)
  var cppMax2026 = 3740;
  var cpp = Math.min(netIncome * 0.114, cppMax2026);

  var result = calculateCanadaIncomeTax(netIncome, province, 0);

  return {
    netBusinessIncome: Math.round(netIncome),
    cppContributions: Math.round(cpp),
    federalTax: result.federalTax,
    provincialTax: result.provincialTax,
    totalTax: Math.round(result.totalTax + cpp),
    takeHome: Math.round(netIncome - result.totalTax - cpp)
  };
}

/* ───────────────────────────────────────────────
   Canada Capital Gains Tax Calculator
   Inclusion rate remains 50% for 2026
   ─────────────────────────────────────────────── */
function calculateCanadaCapitalGains(capitalGain, otherIncome, province) {
  if (otherIncome === undefined) otherIncome = 0;
  if (province === undefined) province = 'ON';
  var inclusionRate = 0.50;

  var taxableCapitalGain = capitalGain * inclusionRate;
  var totalTaxable = otherIncome + taxableCapitalGain;

  var taxWithout = calculateCanadaIncomeTax(otherIncome, province, 0).totalTax;
  var taxWith = calculateCanadaIncomeTax(totalTaxable, province, 0).totalTax;
  var taxOnGain = taxWith - taxWithout;

  return {
    totalCapitalGain: Math.round(capitalGain),
    taxablePortion: Math.round(taxableCapitalGain),
    capitalGainsTax: Math.round(taxOnGain),
    effectiveRateOnGain: capitalGain > 0 ? ((taxOnGain / capitalGain) * 100).toFixed(1) + '%' : '0%'
  };
}

/* ───────────────────────────────────────────────
   Canada Payroll Deductions / Take-Home Pay Calculator
   Income tax + CPP (employee) + EI
   ─────────────────────────────────────────────── */
function calculateCanadaTakeHome(grossPay, province, isSelfEmployed) {
  if (province === undefined) province = 'ON';
  if (isSelfEmployed === undefined) isSelfEmployed = false;

  var incomeTaxResult = calculateCanadaIncomeTax(grossPay, province, 0);
  var incomeTax = incomeTaxResult.totalTax;

  // CPP (employee portion: 5.7% on income above $3,500, max ~$3,740/2)
  var cppRate = isSelfEmployed ? 0.114 : 0.057;
  var cppMax = isSelfEmployed ? 3740 : 1870;
  var cppBase = Math.max(0, grossPay - 3500);
  var cpp = Math.min(cppBase * cppRate, cppMax);

  // EI (employee portion: 1.66% up to max ~$1,100)
  var ei = isSelfEmployed ? 0 : Math.min(grossPay * 0.0166, 1100);

  var totalDeductions = incomeTax + cpp + ei;
  var takeHome = grossPay - totalDeductions;

  return {
    grossPay: Math.round(grossPay),
    incomeTax: Math.round(incomeTax),
    cpp: Math.round(cpp),
    ei: Math.round(ei),
    totalDeductions: Math.round(totalDeductions),
    takeHomePay: Math.round(takeHome)
  };
}

/* ───────────────────────────────────────────────
   UK Self Assessment Tax Calculator (England/Wales/NI)
   2025/26: Personal Allowance £12,570, taper at £100k
   ─────────────────────────────────────────────── */
var PERSONAL_ALLOWANCE_2026 = 12570;

function calculateUKSelfAssessment(grossIncome, expenses, dividends) {
  if (expenses === undefined) expenses = 0;
  if (dividends === undefined) dividends = 0;
  var taxableIncome = Math.max(0, grossIncome - expenses);

  var pa = PERSONAL_ALLOWANCE_2026;
  if (taxableIncome > 100000) {
    pa = Math.max(0, pa - Math.floor((taxableIncome - 100000) / 2));
  }

  var taxableAfterPA = Math.max(0, taxableIncome - pa);

  var incomeTax = 0;
  if (taxableAfterPA > 0) {
    var basicSlice = Math.min(taxableAfterPA, 37700);
    incomeTax += basicSlice * 0.20;
  }
  if (taxableAfterPA > 37700) {
    var higherSlice = Math.min(taxableAfterPA - 37700, 87440);
    incomeTax += higherSlice * 0.40;
  }
  if (taxableAfterPA > 125140 - Math.max(0, pa)) {
    incomeTax += (taxableAfterPA - (125140 - Math.max(0, pa))) * 0.45;
  }

  return {
    taxableIncome: Math.round(taxableIncome),
    personalAllowance: Math.round(pa),
    incomeTax: Math.round(incomeTax),
    takeHome: Math.round(grossIncome - incomeTax),
    effectiveRate: grossIncome > 0 ? ((incomeTax / grossIncome) * 100).toFixed(1) + '%' : '0%'
  };
}

/* ───────────────────────────────────────────────
   UK VAT Calculator
   ─────────────────────────────────────────────── */
function calculateUKVAT(netAmount, rate, action) {
  if (rate === undefined) rate = 0.20;
  if (action === undefined) action = 'add';
  var vat = 0;
  var gross = 0;
  var net = netAmount;

  if (action === 'add') {
    vat = netAmount * rate;
    gross = netAmount + vat;
  } else {
    gross = netAmount;
    net = netAmount / (1 + rate);
    vat = gross - net;
  }

  return {
    netAmount: Math.round(net * 100) / 100,
    vatAmount: Math.round(vat * 100) / 100,
    grossAmount: Math.round(gross * 100) / 100,
    rate: (rate * 100) + '%'
  };
}

/* ───────────────────────────────────────────────
   UK Capital Gains Tax Calculator
   2025/26: £3,000 annual exemption, 10%/20% rates
   ─────────────────────────────────────────────── */
function calculateUKCapitalGains(gain, otherIncome) {
  if (otherIncome === undefined) otherIncome = 0;
  var annualExemption = 3000;
  var taxableGain = Math.max(0, gain - annualExemption);
  var totalIncome = otherIncome + taxableGain;
  var cgtRate = totalIncome > 50270 ? 0.20 : 0.10;
  var cgt = taxableGain * cgtRate;

  return {
    annualExemption: annualExemption,
    totalGain: Math.round(gain),
    taxableGain: Math.round(taxableGain),
    cgtPayable: Math.round(cgt),
    rateUsed: (cgtRate * 100) + '%'
  };
}

/* ───────────────────────────────────────────────
   Australia Tax Return Estimator (Resident)
   2025-26 FY: tax-free threshold $18,200
   ─────────────────────────────────────────────── */
function calculateAustraliaTax(grossIncome, deductions) {
  if (deductions === undefined) deductions = 0;
  var taxableIncome = Math.max(0, grossIncome - deductions);
  var tax = 0;

  if (taxableIncome <= 18200) {
    tax = 0;
  } else if (taxableIncome <= 45000) {
    tax = (taxableIncome - 18200) * 0.16;
  } else if (taxableIncome <= 135000) {
    tax = 4288 + (taxableIncome - 45000) * 0.30;
  } else if (taxableIncome <= 190000) {
    tax = 31288 + (taxableIncome - 135000) * 0.37;
  } else {
    tax = 51638 + (taxableIncome - 190000) * 0.45;
  }

  var medicare = taxableIncome * 0.02;

  return {
    taxableIncome: Math.round(taxableIncome),
    incomeTax: Math.round(tax),
    medicareLevy: Math.round(medicare),
    totalTax: Math.round(tax + medicare),
    takeHome: Math.round(grossIncome - tax - medicare),
    effectiveRate: grossIncome > 0 ? (((tax + medicare) / grossIncome) * 100).toFixed(1) + '%' : '0%'
  };
}

/* ───────────────────────────────────────────────
   Australia Superannuation Calculator
   2025-26: concessional cap $30,000, SG 12%
   ─────────────────────────────────────────────── */
var CONCESSIONAL_CAP_2026 = 30000;

function calculateSuperContribution(grossIncome, contributionRate, voluntary) {
  if (contributionRate === undefined) contributionRate = 0.12;
  if (voluntary === undefined) voluntary = 0;
  var sgContribution = grossIncome * contributionRate;
  var totalConcessional = Math.min(sgContribution + voluntary, CONCESSIONAL_CAP_2026);
  var contribTax = totalConcessional * 0.15;

  return {
    sgContribution: Math.round(sgContribution),
    totalConcessional: Math.round(totalConcessional),
    contributionsTax: Math.round(contribTax),
    netAddedToSuper: Math.round(totalConcessional - contribTax),
    note: "Includes 15% contributions tax on concessional contributions"
  };
}

/* ───────────────────────────────────────────────
   Crypto Tax Calculator (General — US/UK/Australia)
   ─────────────────────────────────────────────── */
function calculateCryptoTax(purchasePrice, salePrice, holdingPeriodMonths, country, otherIncome) {
  if (otherIncome === undefined) otherIncome = 0;
  var gain = Math.max(0, salePrice - purchasePrice);
  var tax = 0;
  var rate = 0;
  var taxableGain = gain;

  if (country === 'UK') {
    var exemption = 3000;
    taxableGain = Math.max(0, gain - exemption);
    rate = otherIncome > 50270 ? 0.20 : 0.10;
    tax = taxableGain * rate;
  } else if (country === 'AU') {
    if (holdingPeriodMonths >= 12) {
      taxableGain = gain * 0.50;
      rate = 0.50;
    } else {
      taxableGain = gain;
      rate = 1.0;
    }
    tax = taxableGain * 0.30;
  } else {
    // US default
    rate = holdingPeriodMonths >= 12 ? 0.15 : 0.24;
    taxableGain = gain;
    tax = gain * rate;
  }

  return {
    capitalGain: Math.round(gain),
    taxableGain: Math.round(taxableGain),
    estimatedTax: Math.round(tax),
    rateDescription: country === 'AU' && holdingPeriodMonths >= 12 ? '50% CGT discount applied' : (rate * 100) + '% rate',
    holdingPeriod: holdingPeriodMonths >= 12 ? 'Long-term' : 'Short-term'
  };
}

/* ───────────────────────────────────────────────
   Self-Employed 401(k) / Solo 401(k) Calculator
   2026 limits: $24,500 employee deferral, $72,000 total
   ─────────────────────────────────────────────── */
var SOLO_401K_LIMITS_2026 = {
  employeeDeferral: 24500,
  catchUp50: 8000,
  superCatchUp60_63: 11250,
  overallLimit: 72000
};

function calculateSolo401k(netProfit, age) {
  return calculateSelfEmployed401k(netProfit, age);
}

function calculateSelfEmployed401k(netProfit, age) {
  if (age === undefined) age = 40;
  var is50Plus = age >= 50;
  var is60to63 = age >= 60 && age <= 63;

  var employee = Math.min(netProfit * 0.75, SOLO_401K_LIMITS_2026.employeeDeferral);
  if (is50Plus) {
    var catchUp = is60to63 ? SOLO_401K_LIMITS_2026.superCatchUp60_63 : SOLO_401K_LIMITS_2026.catchUp50;
    employee = Math.min(employee + catchUp, SOLO_401K_LIMITS_2026.employeeDeferral + catchUp);
  }

  var adjustedComp = netProfit * 0.9235;
  var employer = Math.min(adjustedComp * 0.25, SOLO_401K_LIMITS_2026.overallLimit - employee);

  var total = employee + employer;

  return {
    employeeContribution: Math.round(employee),
    employerContribution: Math.round(employer),
    totalContribution: Math.round(total),
    maxTotalContribution: Math.round(total),
    taxSavingsEstimate: Math.round(total * 0.32),
    remainingRoom: Math.round(SOLO_401K_LIMITS_2026.overallLimit - total),
    recommendation: total > 50000 ? "Excellent tax savings potential" : "Consider increasing contributions"
  };
}

/* ───────────────────────────────────────────────
   Self-Employed Retirement Plan Calculator
   Compares Solo 401(k) vs SEP IRA
   ─────────────────────────────────────────────── */
function calculateSelfEmployedRetirement(netProfit, age, planType) {
  return calculateSelfEmployedRetirementPlans(netProfit, age);
}

function calculateSelfEmployedRetirementPlans(netProfit, age) {
  if (age === undefined) age = 40;
  var solo = calculateSelfEmployed401k(netProfit, age);
  var sep = calculateSEPContribution(netProfit);

  return {
    netProfit: Math.round(netProfit),
    solo401kMax: solo.totalContribution,
    sepMax: sep.maxSEPContribution,
    maxSolo401k: solo.totalContribution,
    maxSEP: sep.maxSEPContribution,
    bestPlan: solo.totalContribution > sep.maxSEPContribution ? "Solo 401(k)" : "SEP IRA",
    bestOption: solo.totalContribution > sep.maxSEPContribution ? "Solo 401(k) allows higher contribution" : "SEP is simpler",
    maxTaxSavings: Math.round(Math.max(solo.totalContribution, sep.maxSEPContribution) * 0.35),
    advice: "Solo 401(k) is better if you want to contribute more than 25%. SEP is simpler to administer."
  };
}

/* ───────────────────────────────────────────────
   SEP IRA Contribution Calculator
   2026 max: $72,000, 25% of compensation
   ─────────────────────────────────────────────── */
function calculateSEPContribution(netProfit) {
  var adjustedNet = netProfit * 0.9235;
  var contribution = Math.min(adjustedNet * 0.25, 72000);

  return {
    maxContribution: Math.round(contribution),
    maxSEPContribution: Math.round(contribution),
    contributionRate: "25%",
    deadline: "Your tax filing deadline (including extensions)",
    taxDeduction: Math.round(contribution),
    effectiveRate: "25% of compensation (after adjustment)",
    note: "You can contribute up to 25% of your net self-employment income."
  };
}

/* ───────────────────────────────────────────────
   Self Employment Tax — Virginia (State + Federal)
   2026 SS wage base $184,500
   ─────────────────────────────────────────────── */
var SS_WAGE_BASE_2026 = 184500;

function calculateVirginiaSelfEmploymentTax(gross, expenses, filingStatus) {
  if (expenses === undefined) expenses = 0;
  if (filingStatus === undefined) filingStatus = 'single';
  var netProfit = Math.max(0, gross - expenses);

  var seBase = netProfit * 0.9235;
  var seTax = (Math.min(seBase, 184500) * 0.124) + (seBase * 0.029);

  var vaTax = 0;
  var vaBrackets = [
    {lower: 0, upper: 3000, rate: 0.02},
    {lower: 3000, upper: 5000, rate: 0.03},
    {lower: 5000, upper: 17000, rate: 0.05},
    {lower: 17000, upper: Infinity, rate: 0.0575}
  ];
  var remaining = netProfit;
  for (var i = 0; i < vaBrackets.length; i++) {
    var b = vaBrackets[i];
    if (remaining > 0) {
      var slice = Math.min(remaining, b.upper - b.lower);
      vaTax += slice * b.rate;
      remaining -= slice;
    }
  }

  return {
    netProfit: Math.round(netProfit),
    federalSETax: Math.round(seTax),
    virginiaStateTax: Math.round(vaTax),
    totalTaxEstimate: Math.round(seTax + vaTax),
    totalTax: Math.round(seTax + vaTax),
    takeHomePay: Math.round(netProfit - seTax - vaTax),
    takeHome: Math.round(netProfit - seTax - vaTax)
  };
}

/* ───────────────────────────────────────────────
   West Virginia Estimated State Taxes
   2026 rates (post-reduction): 2.1%–4.5% brackets
   ─────────────────────────────────────────────── */
function calculateWVEstimatedTaxes(projectedIncome, priorYearTax) {
  return calculateWVEstimatedStateTaxes(projectedIncome, priorYearTax);
}

function calculateWVEstimatedStateTaxes(projectedIncome, priorYearTax) {
  if (priorYearTax === undefined) priorYearTax = 0;
  var estimatedTax = 0;
  if (projectedIncome <= 10000) estimatedTax = projectedIncome * 0.021;
  else if (projectedIncome <= 25000) estimatedTax = 210 + (projectedIncome - 10000) * 0.028;
  else if (projectedIncome <= 40000) estimatedTax = 630 + (projectedIncome - 25000) * 0.032;
  else estimatedTax = 1110 + (projectedIncome - 40000) * 0.045;

  var requiredPayment = priorYearTax > 0 ? priorYearTax : estimatedTax;

  return {
    estimatedAnnualStateTax: Math.round(estimatedTax),
    estimatedAnnualTax: Math.round(estimatedTax),
    safeHarborAmount: Math.round(requiredPayment),
    quarterlyPayment: Math.ceil(requiredPayment / 4),
    dueDates: ["April 15", "June 15", "September 15", "January 15"],
    note: "Payments required if you expect to owe $500 or more."
  };
}

/* ───────────────────────────────────────────────
   WV Sales Tax Calculator
   State rate 6% + optional local up to ~1%
   ─────────────────────────────────────────────── */
var WV_STATE_SALES_TAX = 0.06;

function calculateWVSalesTax(amount, localRate) {
  if (localRate === undefined) localRate = 0.01;
  var totalRate = WV_STATE_SALES_TAX + localRate;
  var tax = amount * totalRate;

  return {
    netAmount: Math.round(amount),
    salesTax: Math.round(tax),
    totalWithTax: Math.round(amount + tax),
    combinedRate: (totalRate * 100) + '%'
  };
}

/* ───────────────────────────────────────────────
   Wisconsin Estimated State Taxes
   2026 progressive rates: 3.5%–7.65%
   ─────────────────────────────────────────────── */
function calculateWisconsinEstimatedTaxes(projectedIncome, deductions) {
  if (deductions === undefined) deductions = 0;
  var taxableIncome = Math.max(0, projectedIncome - deductions);

  var wiTax = 0;
  if (taxableIncome > 0) {
    wiTax += Math.min(taxableIncome, 12000) * 0.035;
    wiTax += Math.max(0, Math.min(taxableIncome - 12000, 24000)) * 0.0465;
    wiTax += Math.max(0, taxableIncome - 36000) * 0.0765;
  }

  return {
    estimatedAnnualWITax: Math.round(wiTax),
    estimatedAnnualTax: Math.round(wiTax),
    quarterlyPayment: Math.ceil(wiTax / 4),
    dueDates: ["April 15, 2026", "June 15, 2026", "September 15, 2026", "January 15, 2027"],
    threshold: "Required if you expect to owe $500+ in WI taxes.",
    thresholdNote: "Required if you expect to owe $500 or more on WI return."
  };
}

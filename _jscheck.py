import os, re

ROOT = r"C:\Users\Tanzeel\Downloads\adsense\FinanceTaxTools"
TOOL_DIR = os.path.join(ROOT, "tools")

def extract_scripts(filepath):
    """Extract all inline scripts from an HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = []
    pattern = re.compile(r'<script\b[^>]*>(.*?)</script>', re.IGNORECASE | re.DOTALL)
    for m in pattern.finditer(content):
        code = m.group(1).strip()
        if code and 'src=' not in m.group(0).lower():
            scripts.append(code)
    return content, scripts

def check_balance(code, name, filelabel):
    """Check bracket/parenthesis balance"""
    issues = []
    pairs = {'{': '}', '(': ')', '[': ']'}
    counts = {}
    for p in pairs:
        counts[p] = {'open': code.count(p), 'close': code.count(pairs[p])}
    
    for p, pair in pairs.items():
        if counts[p]['open'] != counts[p]['close']:
            issues.append(f"  UNBALANCED {p}{pair}: {counts[p]['open']} opening vs {counts[p]['close']} closing")
    
    return issues

def check_common_errors(code, name, filelabel):
    """Check for common JS errors"""
    issues = []
    
    # Check for "FreelanceTaxCalc.online" still in copy text
    if 'FreelanceTaxCalc.online' in code:
        count = code.count('FreelanceTaxCalc.online')
        issues.append(f"  OLD DOMAIN in copy text ({count}x): 'FreelanceTaxCalc.online' should be '.online'")
    
    # Check for "freelancetaxcalc.com" still in code
    if 'freelancetaxcalc.com' in code:
        issues.append(f"  OLD DOMAIN STILL in code: freelancetaxcalc.com")
    
    # Check for potential undefined variables
    # Look for assignment to undeclared variables
    lines = code.split('\n')
    for i, line in enumerate(lines, 1):
        line_stripped = line.strip()
        # Skip comments
        if line_stripped.startswith('//') or line_stripped.startswith('/*') or line_stripped.startswith('*'):
            continue
        
        # Check for assignment without var/let/const outside of known patterns
        # This is a simplified check - real linters are better
        if '=' in line_stripped and not line_stripped.startswith('var ') and not line_stripped.startswith('let ') and not line_stripped.startswith('const ') and not line_stripped.startswith('this.') and not line_stripped.startswith('return ') and 'for(' not in line_stripped and 'for (' not in line_stripped:
            # This catches many assignments but has false positives
            pass  # Too noisy, skip
    
    # Check for template literal issues
    if '${' in code:
        # Make sure template literals use backticks
        pass  # Hard to check without full parser
    
    return issues

def check_all_tools():
    total_issues = 0
    
    for fname in sorted(os.listdir(TOOL_DIR)):
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(TOOL_DIR, fname)
        
        # Skip state directories
        if os.path.isdir(fpath):
            continue
        
        content, scripts = extract_scripts(fpath)
        filelabel = f"tools/{fname}"
        
        if not scripts:
            print(f"  NO inline scripts: {filelabel}")
            continue
        
        all_issues = []
        
        for i, code in enumerate(scripts):
            label = f"{filelabel} script#{i+1}"
            
            # Check balance
            bal_issues = check_balance(code, label, filelabel)
            all_issues.extend(bal_issues)
            
            # Check common errors
            err_issues = check_common_errors(code, label, filelabel)
            all_issues.extend(err_issues)
        
        if all_issues:
            print(f"\n⚠  {filelabel}:")
            for iss in all_issues:
                print(f"   {iss}")
            total_issues += len(all_issues)
        else:
            print(f"✓ {filelabel}")
    
    print(f"\n\nTotal issues found: {total_issues}")
    return total_issues

# Also check deduction pages, nomad pages, state pages
def check_subpages():
    issues_found = 0
    subdirs = [
        os.path.join(ROOT, "deductions"),
        os.path.join(ROOT, "digital-nomad-tax"),
        os.path.join(ROOT, "tools/quarterly-tax-calculator"),
    ]
    
    for subdir in subdirs:
        if not os.path.isdir(subdir):
            continue
        for fname in sorted(os.listdir(subdir)):
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(subdir, fname)
            content, scripts = extract_scripts(fpath)
            
            if not scripts:
                continue
            
            rel = os.path.relpath(fpath, ROOT)
            all_issues = []
            
            for i, code in enumerate(scripts):
                label = f"{rel} script#{i+1}"
                bal_issues = check_balance(code, label, rel)
                all_issues.extend(bal_issues)
                err_issues = check_common_errors(code, label, rel)
                all_issues.extend(err_issues)
            
            if all_issues:
                print(f"\n⚠  {rel}:")
                for iss in all_issues:
                    print(f"   {iss}")
                issues_found += len(all_issues)
            else:
                print(f"✓ {rel}")
    
    return issues_found

if __name__ == '__main__':
    print("=== MAIN TOOL PAGES ===")
    main_issues = check_all_tools()
    print(f"\n=== SUBPAGES (deductions, nomad, states) ===")
    sub_issues = check_subpages()
    print(f"\n\n=== TOTAL: {main_issues + sub_issues} issues found ===")

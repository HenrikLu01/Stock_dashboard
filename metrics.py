def fcf_calc(netIncome, nonCashExpenses, deltaWorkingCapital, capEx):
    return netIncome + nonCashExpenses - deltaWorkingCapital - capEx

def cash_conversion_ratio(ocf, net_income):
    return ocf / net_income

def nopat(ebit, tax_rate):
    return ebit * (1 - tax_rate)
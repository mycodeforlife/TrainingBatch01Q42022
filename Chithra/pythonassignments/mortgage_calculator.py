class MortgageCalculator:
    principal_amount = 0
    interest_rate_year = 0
    loan_term_year = 0

    def __init__(self, principal, interest, term):
        self.principal_amount = principal
        self.interest_rate_year = interest
        self.loan_term = term

    def get_monthly_payment(self):
        interest_rate_month = (self.interest_rate_year / 100) / 12
        loan_term_months = self.loan_term * 12
        monthly_payment = self.principal_amount * (
                    (interest_rate_month * (1 + interest_rate_month) ** loan_term_months) / (
                        ((1 + interest_rate_month) ** loan_term_months) - 1))
        return monthly_payment


x = MortgageCalculator(100000,12,15)
print(x.get_monthly_payment())


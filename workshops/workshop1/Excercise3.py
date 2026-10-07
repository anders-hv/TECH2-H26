import numpy as np


def tax(income):
    """
    Return the taxes owed for a given income.

    Parameters
    ----------
    income
        Gross income

    Returns
    ----------
    Tax owed
    """

    if income <= 300_000:
        taxes = 0
    elif 300_000 < income <= 700_000:
        taxes = 0.2 * (income - 300_000)
    else:
        taxes = 0.2 * (700_000 - 300_000) + 0.35 * (income - 700_000)

    return taxes


# Create 13 candidate income levels for testing
incomes = np.linspace(0, 1_200_000, 13)

taxes_loop = []

for income in incomes:
    # Compute the taxes for current income level
    taxes = tax(incomes)
    # Append to list
    taxes_loop.append(taxes)
    # Income after tax
    net_income = income - taxes

print(f'Gross income: {income:10.0f};'
      f'Taxes: {taxes:10.0f};'
      f'Net income {net_income:10.0f}')


import datetime
from FormatValues import *

HST_RATE = 0.15
LICENSE_FEE_UNDER_15K = 75.00
LICENSE_FEE_OVER_15K = 165.00
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
MAX_PRICE = 50000.00
FINANCE_RATE = 39.99

while True:
    first_name = input("Enter customer FIRST name (or END to quit): ").title()
    if first_name.upper() == "END":
        break

    last_name = input("Enter customer LAST name: ").title()
    while not last_name:
        last_name = input("Last name required: ").title()

    phone = input("Enter 10-digit phone number: ")
    while not (phone.isdigit() and len(phone) == 10):
        phone = input("Phone must be 10 digits: ")

    plate = input("Enter license plate (6 characters): ").upper()
    while len(plate) != 6:
        plate = input("Plate must be 6 characters: ").upper()

    make = input("Enter car make: ").title()
    model = input("Enter car model: ").title()
    year = input("Enter car year: ")

    price = float(input("Enter selling price (max $50,000): "))
    while price > MAX_PRICE:
        price = float(input("Selling price too high, re-enter: "))

    trade = float(input("Enter trade-in amount: "))
    while trade > price:
        trade = float(input("Trade-in can't exceed selling price. Re-enter: "))

    salesperson = input("Enter salesperson name: ").title()
    while not salesperson:
        salesperson = input("Salesperson name required: ").title()

    invoice_date = datetime.date.today()
    receipt_id = FormatReceiptID(first_name[0], last_name, plate, phone)

    price_after_trade = price - trade
    license_fee = LICENSE_FEE_UNDER_15K if price <= 15000 else LICENSE_FEE_OVER_15K
    transfer_fee = price * TRANSFER_FEE_RATE
    if price > 20000:
        transfer_fee += price * LUXURY_TAX_RATE

    subtotal = price_after_trade + license_fee + transfer_fee
    hst = subtotal * HST_RATE
    total_price = subtotal + hst

    print("-" * 72)
    print(f"Honest Harry Car Sales       Invoice Date: {FDateS(invoice_date)}")
    print("Used Car Sale and Receipt    Receipt No:", receipt_id)
    print("Sale price:".ljust(35), FDollar2(price))
    print("Sold to:", f"{first_name[0]}. {last_name}".ljust(25), "Trade Allowance:", FDollar2(trade))
    print("-" * 72)
    print(f"Phone: {FPhone(phone)}")
    print("Car Details:", f"{year} {make} {model}")
    print("Price after Trade:".ljust(35), FDollar2(price_after_trade))
    print("License Fee:".ljust(35), FDollar2(license_fee))
    print("Transfer Fee:".ljust(35), FDollar2(transfer_fee))
    print("Subtotal:".ljust(35), FDollar2(subtotal))
    print("HST (15%):".ljust(35), FDollar2(hst))
    print("Total Sales Price:".ljust(35), FDollar2(total_price))
    print("-" * 72)

    print("Financing Options")
    print("Years".ljust(8), "#Payments".ljust(12), "Fee".ljust(12), "Total Price".ljust(16), "Monthly")
    print("-" * 60)
    for years in range(1, 5):
        months = years * 12
        finance_fee = years * FINANCE_RATE
        total_with_finance = total_price + finance_fee
        monthly = total_with_finance / months
        print(str(years).ljust(8), str(months).ljust(12), FDollar2(finance_fee).ljust(12),
              FDollar2(total_with_finance).ljust(16), FDollar2(monthly))

    today = datetime.date.today()
    if today.day >= 25:
        months_ahead = 2
    else:
        months_ahead = 1
    year = today.year + ((today.month + months_ahead - 1) // 12)
    month = (today.month + months_ahead - 1) % 12 + 1
    first_payment = datetime.date(year, month, 1)
    print("-" * 72)
    print("First payment date:", first_payment.strftime("%d-%b-%y"))
    print("Best used cars at the best prices!")
    print("-" * 72)

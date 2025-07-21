
import datetime

def FDollar2(DollarValue):
    return "${:,.2f}".format(DollarValue)

def FDollar0(DollarValue):
    return "${:,.0f}".format(DollarValue)

def FComma2(Value):
    return "{:,.2f}".format(Value)

def FComma0(Value):
    return "{:,.0f}".format(Value)

def FNumber0(Value):
    return "{:.0f}".format(Value)

def FDateS(DateValue):
    return DateValue.strftime("%a %b %d, %Y")

def FPhone(Phone):
    return f"({Phone[:3]}) {Phone[3:6]}-{Phone[6:]}"

def FormatReceiptID(first_initial, last_name, plate, phone):
    return f"{first_initial.upper()}{last_name[0].upper()}-{plate[-3:]}-{phone[-4:]}"

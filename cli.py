import argparse

from colorama import Fore

from bot.orders import place_order

from bot.validators import validate_order


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)

parser.add_argument("--side", required=True)

parser.add_argument("--type", required=True)

parser.add_argument("--quantity", type=float, required=True)

parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print(Fore.CYAN + "\nORDER SUMMARY\n")

    print("Symbol :", args.symbol)

    print("Side :", args.side)

    print("Type :", args.type)

    print("Quantity :", args.quantity)

    if args.type == "LIMIT":
        print("Price :", args.price)

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print(Fore.GREEN + "\nSUCCESS\n")

    print("Order ID :", order["orderId"])

    print("Status :", order["status"])

    print("Executed Qty :", order["executedQty"])

except Exception as e:

    print(Fore.RED + str(e))
from qdk import qsharp as qs
import json
import argparse
import string

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = "!@#$%^&*"


def main() -> None:
    args = parse_args()
    chars = LETTERS + DIGITS + (SYMBOLS if not args.no_symbols else "")

    qs.init(project_root="./.")
    qs.eval(
        f"PasswordGenerator.GeneratePassword({args.length}, {json.dumps(list(chars))})"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="qpass", description="Quantum Password Generator"
    )

    parser.add_argument("-l", "--length", type=int, default=24)
    parser.add_argument("-n", "--no-symbols", action="store_true")

    return parser.parse_args()

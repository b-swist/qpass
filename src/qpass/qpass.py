import qdk
import argparse

VERSION = "1.0.0"


def main() -> None:
    args = parse_args()
    qdk.init(project_root="./.")

    match args.command:
        case "generate":
            qdk.code.Main.Generate(args.length, args.no_symbols)
        case "check":
            qdk.code.Main.Check(list(args.password))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quantum Password Generator")
    parser.add_argument("-v", "--version", action="version", version=VERSION)

    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("-l", "--length", type=int, default=24, help="set generated password length")
    generate_parser.add_argument("-n", "--no-symbols", action="store_true", help="exclude symbols from the password")
    check_parser = subparsers.add_parser("check", help="check password entropy")
    check_parser.add_argument("password", type=str, help="password to be checke")

    return parser.parse_args()

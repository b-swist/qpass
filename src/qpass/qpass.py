import qdk
import argparse

VERSION = "1.0.0"


def main() -> None:
    args, help = parse_args()
    qdk.init(project_root="./.")

    match args.command:
        case "generate":
            qdk.code.Main.Generate(args.length, args.no_symbols)
        case "check":
            qdk.code.Main.Check(list(args.password))
        case None:
            print(help)


def parse_args() -> tuple[argparse.Namespace, str]:
    parser = argparse.ArgumentParser(description="Quantum Password Generator")
    parser.add_argument("-v", "--version", action="version", version=VERSION)

    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="check password entropy")
    check_parser.add_argument("password", type=str, help="password to be checke")

    generate_parser = subparsers.add_parser("generate", help="generate new password")
    generate_parser.add_argument(
        "-l", "--length", type=int, default=24, help="set password length"
    )
    generate_parser.add_argument(
        "-n",
        "--no-symbols",
        action="store_true",
        help="exclude symbols from the password",
    )

    return parser.parse_args(), parser.format_help()

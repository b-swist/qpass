import qdk
import argparse
from pathlib import Path

VERSION = "1.0.0"


def project_root() -> str:
    path = Path(__file__).resolve().parent
    return str(path)


def length(s: str) -> int:
    n = int(s)
    if not 1 <= n <= 128:
        raise argparse.ArgumentTypeError("length must be between 1 and 128")
    return n


def main() -> None:
    parser = new_parser()
    qdk.init(project_root=project_root())

    args = parser.parse_args()
    match args.command:
        case "generate":
            qdk.code.Main.Generate(args.length, args.no_symbols)
        case "check":
            qdk.code.Main.Check(list(args.password))
        case _:
            parser.print_help()


def new_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Quantum Password Generator")
    parser.add_argument("-v", "--version", action="version", version=VERSION)

    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("check", help="check password entropy")
    check_parser.add_argument("password", type=str, help="password to be checked")

    generate_parser = subparsers.add_parser("generate", help="generate new password")
    generate_parser.add_argument(
        "-l", "--length", type=length, default=24, help="set password length"
    )
    generate_parser.add_argument(
        "-n",
        "--no-symbols",
        action="store_true",
        help="exclude symbols from the password",
    )

    return parser

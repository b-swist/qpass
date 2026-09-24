from qdk import qsharp as qs
import json
import argparse

VERSION = "1.0.0"


def char_list(s: str) -> list[str]:
    return json.dumps(list(s))


def bool_to_str(b: bool) -> str:
    return "true" if b else "false"


def main() -> None:
    args = parse_args()

    qs.init(project_root="./.")
    qs.eval(f"Main.Generate({args.length}, {bool_to_str(not args.no_symbols)})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quantum Password Generator")
    parser.add_argument("-v", "--version", action="version", version=VERSION)

    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument("-l", "--length", type=int, default=24, help="set generated password length")
    generate_parser.add_argument("-n", "--no-symbols", action="store_true", help="exclude symbols from the password")

    return parser.parse_args()

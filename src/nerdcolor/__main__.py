import argparse
import sys

from nerdcolor.nerdcolor import SCHEMES, VERSION, Colorscheme


def print_colorschemes():
    for key in SCHEMES.keys():
        scheme = Colorscheme([key], "true", delimiter="char", bold=True)
        print(scheme.colorize(key))


def print_examples():
    string = (
        "Full versions:\n\n\t"
        "1) nerdcolor --ansi --delimiter line --bold --palette red green blue\n\t"
        "2) nerdcolor --true --delimiter word --palette dracula\n\t"
        '3) nerdcolor --true --delimiter char --palette "#EFFFFB" "#50D890" "#4F98CA" "#7874F2"\n\n'
        "Shortened versions:\n\n\t"
        "1) nerdcolor -a -b -p red green blue\n\t"
        "2) nerdcolor -t -d word -p dracula\n\t"
        '3) nerdcolor -t -d char -p "#EFFFFB" "#50D890" "#4F98CA" "#7874F2"'
    )

    print(string)


def main():
    parser = argparse.ArgumentParser(
        prog="nerdcolor",
        description="A simple CLI colorizer.",
        epilog="Project home page: https://github.com/0xHaru/Nerd-Color",
    )
    parser.version = VERSION
    parser.add_argument(
        "-a",
        "--ansi",
        help="use ANSI colors",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-t",
        "--true",
        help="use true colors",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-d",
        "--delimiter",
        type=str,
        help="set the delimiter",
        default="line",
    )
    parser.add_argument(
        "-b", "--bold", help="use bold text", action="store_true", default=False
    )
    parser.add_argument(
        "-p",
        "--palette",
        type=str,
        help="set the color palette",
        nargs="+",
    )
    parser.add_argument(
        "-c",
        "--colorschemes",
        help="show available color schemes",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-e",
        "--examples",
        help="show usage examples",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-v", "--version", help="show program's version", action="version"
    )

    args = parser.parse_args()

    if args.colorschemes:
        print_colorschemes()
        exit(0)

    if args.examples:
        print_examples()
        exit(0)

    if not args.palette:
        print("Error: missing palette")
        exit(1)

    if not args.ansi and not args.true:
        print("Error: --ansi or --true must be set")
        exit(1)

    if args.ansi and args.true:
        print("Error: --ansi and --true cannot both be set")
        exit(1)

    color_type = "ansi" if args.ansi else "true"
    scheme = Colorscheme(
        args.palette, color_type, delimiter=args.delimiter, bold=args.bold
    )

    print(scheme.colorize(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()

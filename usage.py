from nerdcolor.nerdcolor import (
    BOLD_COLORS,
    COLORS,
    SCHEMES,
    Colorscheme,
    hex_to_rgb,
    rgb_to_hex,
)

# ANSI Colors
green = COLORS["green"]
bold_green = BOLD_COLORS["green"]
bold_blue = BOLD_COLORS["blue"]
end = COLORS["end"]

print(f"{bold_blue}ANSI Colors:{end}\n")

print(f"\t{green}This is green.{end}")
print(f"\t{bold_green}This is bold green.{end}\n")

# Available Color Schemes
print(f"{bold_blue}Available Color Schemes:{end}\n")

for key in SCHEMES.keys():
    scheme = Colorscheme([key], "true", delimiter="word")
    string = f"\t{key}: {SCHEMES[key]}"
    print(scheme.colorize(string))

# Color Schemes
string = """\tLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
\tUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
\tDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
\tExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

scheme_1 = Colorscheme(["red", "green", "blue"], "ansi", delimiter="line")
scheme_2 = Colorscheme(["dracula"], "true", delimiter="word", bold=True)

colors = [
    "#EFFFFB",
    "#50D890",
    "#4F98CA",
    "#7874F2",
]

scheme_3 = Colorscheme(colors, "true", delimiter="char", bold=True)

print(f"\n{bold_blue}Examples:{end}\n")

print(scheme_1.colorize(string), "\n")
print(scheme_2.colorize(string), "\n")
print(scheme_3.colorize(string), "\n")

# Utils
rgb = hex_to_rgb("#EFFFFB")
hex_ = rgb_to_hex((239, 255, 251))

print(f"{bold_blue}Utils:{end}\n")

print(f"\tHEX: #EFFFFB - RGB: {rgb}")
print(f"\tRGB: (239, 255, 251) - HEX: {hex_}")

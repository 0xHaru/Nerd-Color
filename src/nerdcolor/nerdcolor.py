import itertools
import re

VERSION = "0.1.0"


class Colorscheme:
    def __init__(self, palette, color_type, **kwargs):
        self.palette = palette
        self.color_type = color_type
        self.delimiter = kwargs.get("delimiter", "line")
        self.bold = kwargs.get("bold", False)

    def __repr__(self):
        return (
            f"Colorscheme({self.palette}, {self.color_type}, "
            f"{self.delimiter}, {self.bold})"
        )

    def __str__(self):
        return (
            f"Palette: {self.palette} - Color_type: {self.color_type} - "
            f"Delimiter: {self.delimiter} - Bold: {self.bold}"
        )

    def _str_to_list(self, string):
        if self.delimiter == "line":
            return string.splitlines(keepends=True)

        if self.delimiter == "word":
            lines = string.splitlines(keepends=True)
            bidim_list = [re.split(" ", line) for line in lines]
            bidim_list = [_intersperse(list_, " ") for list_ in bidim_list]
            return list(itertools.chain(*bidim_list))

        if self.delimiter == "char":
            return list(string)

    def _true_color(self, rgb, string):
        if self.bold:
            return f"\x1b[1;38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}\x1b[0m"

        return f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}\x1b[0m"

    def _true_colorize(self, string):
        i = 0
        output = []
        palette = self.palette

        if palette[0][0] != "#":
            palette = SCHEMES[palette[0]]

        plen = len(palette)
        list_ = self._str_to_list(string)

        for element in list_:
            if element == "\n" or element.isspace():
                output.append(element)
            else:
                hex_code = palette[i % plen]
                rgb = hex_to_rgb(hex_code)

                text = self._true_color(rgb, element)
                output.append(text)

                i += 1

        if output[-1] != "\n" and output[-1].isspace():
            output.append("\n")

        return "".join(output)

    def _ansi_colorize(self, string):
        i = 0
        output = []
        colors_dict = BOLD_COLORS if self.bold else COLORS

        plen = len(self.palette)
        list_ = self._str_to_list(string)

        for element in list_:
            if element == "\n" or element.isspace():
                output.append(element)
            else:
                color = self.palette[i % plen]
                output.append(f"{colors_dict[color]}{element}{colors_dict['end']}")
                i += 1

        if output[-1] != "\n" and output[-1].isspace():
            output.append("\n")

        return "".join(output)

    def colorize(self, string):
        if self.color_type == "ansi":
            return self._ansi_colorize(string)

        if self.color_type == "true":
            return self._true_colorize(string)


# Utils
def _intersperse(list_, element):
    result = [element] * (len(list_) * 2 - 1)
    result[0::2] = list_
    return result


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    hlen = len(hex_code)

    return tuple(
        int(hex_code[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)
    )


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])


# Colors and Color Schemes

# 16 colors (4-bit) - ANSI Escape Codes
COLORS = {
    "white": "\x1b[97m",
    "light-gray": "\x1b[37m",
    "dark-gray": "\x1b[90m",
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "yellow": "\x1b[33m",
    "green": "\x1b[32m",
    "magenta": "\x1b[35m",
    "blue": "\x1b[34m",
    "cyan": "\x1b[36m",
    "light-red": "\x1b[91m",
    "light-yellow": "\x1b[93m",
    "light-green": "\x1b[92m",
    "light-magenta": "\x1b[95m",
    "light-blue": "\x1b[94m",
    "light-cyan": "\x1b[96m",
    "foreground": "\x1b[39m",
    "end": "\x1b[0m",
}

# 16 colors (4-bit) - ANSI Escape Codes - Bold
BOLD_COLORS = {
    "white": "\x1b[1;97m",
    "light-gray": "\x1b[1;37m",
    "dark-gray": "\x1b[1;90m",
    "black": "\x1b[1;30m",
    "red": "\x1b[1;31m",
    "yellow": "\x1b[1;33m",
    "green": "\x1b[1;32m",
    "magenta": "\x1b[1;35m",
    "blue": "\x1b[1;34m",
    "cyan": "\x1b[1;36m",
    "light-red": "\x1b[1;91m",
    "light-yellow": "\x1b[1;93m",
    "light-green": "\x1b[1;92m",
    "light-magenta": "\x1b[1;95m",
    "light-blue": "\x1b[1;94m",
    "light-cyan": "\x1b[1;96m",
    "foreground": "\x1b[1;39m",
    "end": "\x1b[0m",
}

# True Colors (24-bit)
SCHEMES = {
    "aurora": [
        "#BF616A",
        "#D08770",
        "#EBCB8B",
        "#A3BE8C",
        "#B48EAD",
    ],
    "autumn": [
        "#FFF9E0",
        "#F1C550",
        "#F1C550",
        "#FF6600",
        "#CE2525",
    ],
    "bluloco": [
        "#FF6480",
        "#FF936A",
        "#CE9887",
        "#F9C859",
        "#3FC56B",
        "#10B1FE",
        "#3691FF",
        "#7A82DA",
        "#9F7EFE",
        "#FF78F8",
    ],
    "bright": [
        "#ECA3F5",
        "#FDBAF8",
        "#B0EFEB",
        "#EDFFA9",
    ],
    "chalk": [
        "#F58E8E",
        "#A9D3AB",
        "#FED37E",
        "#7AABD4",
        "#D6ADD5",
        "#79D4D5",
        "#D4D4D4",
    ],
    "code-dark": [
        "#9CDCFE",
        "#569CD6",
        "#4EC9B0",
        "#608B4E",
        "#B5CEA8",
        "#DCDCAA",
        "#D7BA7D",
        "#CE9178",
        "#D16969",
        "#F44747",
        "#C586C0",
        "#646695",
    ],
    "cold": [
        "#7579E7",
        "#9AB3F5",
        "#A3D8F4",
        "#B9FFFC",
    ],
    "dark": [
        "#232931",
        "#393E46",
        "#4ECCA3",
        "#85CFCB",
    ],
    "darker": [
        "#2C2828",
        "#3B2C85",
        "#219897",
        "#85CFCB",
    ],
    "dracula": [
        "#6272A4",
        "#8BE9FD",
        "#50FA7B",
        "#FFB86C",
        "#FF79C6",
        "#BD93F9",
        "#FF5555",
        "#F1FA8C",
    ],
    "frost": [
        "#8FBCBB",
        "#88C0D0",
        "#81A1C1",
        "#5E81AC",
    ],
    "gatito": [
        "#E15A60",
        "#99C794",
        "#FAC863",
        "#6699CC",
        "#C594C5",
        "#5FB3B3",
    ],
    "monokai": [
        "#FF6188",
        "#FC9867",
        "#FFD866",
        "#A9DC76",
        "#78DCE8",
        "#AB9DF2",
    ],
    "neon": [
        "#E33962",
        "#6930C3",
        "#64DFDF",
        "#80FFDB",
    ],
    "one-dark": [
        "#E06C75",
        "#98C379",
        "#E5C07B",
        "#61AFEF",
        "#C678DD",
        "#56B6C2",
    ],
    "pastel": [
        "#A8D8EA",
        "#AA96DA",
        "#FCBAD3",
        "#FFFFD2",
    ],
    "retro": [
        "#A2DE96",
        "#3CA59D",
        "#774898",
        "#E79C2A",
    ],
    "sakura": [
        "#FFB7C5",
        "#FFEBEB",
        "#FF8080",
        "#D0EED5",
        "#FFA6BE",
    ],
    "spring": [
        "#98DDCA",
        "#D5ECC2",
        "#FFD3B4",
        "#FFAAA7",
    ],
    "summer": [
        "#FF75A0",
        "#FCE38A",
        "#EAFFD0",
        "#95E1D3",
    ],
    "sunset": [
        "#FB92B8",
        "#A9A7EB",
        "#A9A7EB",
        "#7772B6",
        "#F98D94",
        "#F7987F",
        "#F7AF7E",
        "#FB877E",
        "#EA5768",
        "#904756",
    ],
    "tokyo-night": [
        "#F7768E",
        "#FF9E64",
        "#E0AF68",
        "#9ECE6A",
        "#73DACA",
        "#B4F9F8",
        "#2AC3DE",
        "#7DCFFF",
        "#7AA2F7",
        "#BB9AF7",
    ],
    "vintage": [
        "#75C8AE",
        "#785741",
        "#FFECB4",
        "#E5771E",
        "#F4A127",
    ],
    "warm": [
        "#FF4646",
        "#FF8585",
        "#FFB396",
        "#FFF5C0",
    ],
    "winter": [
        "#EFFFFB",
        "#50D890",
        "#4F98CA",
        "#7874F2",
    ],
}

<div align="center">
<h1>Nerd-Color</h1>
</div>

![](https://raw.githubusercontent.com/0xHaru/Nerd-Color/master/media/screenshot.png)

A simple CLI colorizer.

## Description

Nerd-Color can be used as command line interface application or as a library to colorize text using the standard 16 colors (ANSI escape codes) or using true colors.

The former uses colors such as "red", "green, "blue" and will respect the terminal color scheme.

The latter uses colors such as "#FF0000" "00FF00" "#0000FF" and will display them regardless of the terminal color scheme.

More info here:

-   [stackoverflow.com/list-of-ansi-color-escape-sequences](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
-   [github.com/XVilka/TrueColour.md](https://gist.github.com/XVilka/8346728)

## Prerequisites

-   Linux

-   To use the true color option a terminal that supports true colors is required.

    More info here:

    -   [github.com/XVilka/TrueColour.md#now-supporting-true-color](https://gist.github.com/XVilka/8346728#now-supporting-true-color)

## Installation

`pip install Nerd-Color`

## Usage

### CLI

#### Basic usage:

`<text> | nerdcolor <parameters>`

#### Example:

`cat dummy.txt | nerdcolor -t -d word -p dracula`

#### Other examples:

```shell
Full versions:

	1) nerdcolor --ansi --delimiter line --bold --palette red green blue
	2) nerdcolor --true --delimiter word --palette dracula
	3) nerdcolor --true --delimiter char --palette "#8FBCBB" "#88C0D0" "#81A1C1" "#5E81AC"

Shortened versions:

	1) nerdcolor -a -b -p red green blue
	2) nerdcolor -t -d word -p dracula
	3) nerdcolor -t -d char -p "#8FBCBB" "#88C0D0" "#81A1C1" "#5E81AC"
```

### Library

Full usage: [usage.py](https://github.com/0xHaru/Nerd-Color/blob/master/usage.py)

```py
from nerdcolor.nerdcolor import Colorscheme

string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

scheme_1 = Colorscheme(["red", "green", "blue"], "ansi", delimiter="line")
scheme_2 = Colorscheme(["dracula"], "true", delimiter="word", bold=True)

colors = [
    "#EFFFFB",
    "#50D890",
    "#4F98CA",
    "#7874F2",
]

scheme_3 = Colorscheme(colors, "true", delimiter="char", bold=True)

print(scheme_1.colorize(string), "\n")
print(scheme_2.colorize(string), "\n")
print(scheme_3.colorize(string))
```

## Config

To add custom color schemes the user has to add them to the `SCHEMES` dictionary in `nerdcolor.py`.

This command will output the full path of the file:

`pip show Nerd-Color | grep 'Location' | grep -o -E '[/].+' | xargs printf '%s/nerdcolor/nerdcolor.py\n'`

## Color schemes

Nerd-Color currently has 25 predefined color schemes.

You can print them using this snippet:

```py
from nerdcolor.nerdcolor import SCHEMES, Colorscheme

for key in SCHEMES.keys():
    scheme = Colorscheme([key], "true", delimiter="word")
    string = f"{key}: {SCHEMES[key]}"
    print(scheme.colorize(string))
```

![](https://raw.githubusercontent.com/0xHaru/Nerd-Color/master/media/colorschemes.png)

### Links

[github.com/uloco/theme-bluloco-dark](https://github.com/uloco/theme-bluloco-dark)

[github.com/dracula/dracula-theme](https://github.com/dracula/dracula-theme)

[github.com/pawelgrzybek/gatito-theme](https://github.com/pawelgrzybek/gatito-theme)

[github.com/Mayccoll/Gogh](https://github.com/Mayccoll/Gogh)

[github.com/arcticicestudio/nord](https://github.com/arcticicestudio/nord)

[github.com/Binaryify/OneDark-Pro](https://github.com/Binaryify/OneDark-Pro)

[github.com/enkia/tokyo-night-vscode-theme](https://github.com/enkia/tokyo-night-vscode-theme)

[github.com/tomasiser/vim-code-dark](https://github.com/tomasiser/vim-code-dark)

[code.visualstudio.com](https://code.visualstudio.com)

[monokai.pro](https://monokai.pro)

[colorhunt.co/palettes](https://colorhunt.co/palettes)

## License

This project uses the following license: [GPLv3](https://github.com/0xHaru/Nerd-Color/blob/master/LICENSE).

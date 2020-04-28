# Yaru-Anycolor

This repository contains a script that modifies [Ubuntu's Yaru Theme](https://github.com/ubuntu/yaru) to use colors of your choice. The idea for this project came from using the [Yaru-Colors](https://github.com/Jannomag/Yaru-Colors) project.

## Preparations

Clone this repository and initialize the yaru submodule:

```
git clone <TODO> --recurse-submodules
cd <TODO>
```

Install dependencies needed to build yaru (for more details, see yaru's [CONTRIBUTING.md](https://github.com/ubuntu/yaru/blob/master/CONTRIBUTING.md)):

```
sudo apt install libgtk-3-dev git meson sassc inkscape optipng ruby
```

## Configuration

Open the `color_theme.py` file and edit the constants at the top to suit your needs. The default values are as follows:

```
THEME_NAME = "YaruBlue"
COLOR_BRIGHT = "#208fe9"       # orange in yaru
COLOR_DARK = "#255074"         # purple in yaru
BG_COLOR_TERMINAL = "#0e1d30"
```

## Apply colors to the yaru submodule

Execute the `color_theme.py` script. This will update colors in various places, including some icons.

```
python3 color_theme.py
```

You can use `git diff` in the submodule folder to see what values were updated by the script.

## Build the theme

Build the theme just like the original yaru theme is built (for more details, see yaru's [CONTRIBUTING.md](https://github.com/ubuntu/yaru/blob/master/CONTRIBUTING.md)):

```
cd yaru
meson build
cd build
sudo ninja install
```

## Select the theme

The theme can now be selected, either using the gnome tweaks GUI or by using the following commands:

```
gsettings set org.gnome.desktop.interface gtk-theme <YOUR_THEME_NAME>
gsettings set org.gnome.desktop.interface icon-theme <YOUR_THEME_NAME>
```
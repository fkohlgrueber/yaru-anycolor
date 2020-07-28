
from pathlib import Path
import re
import subprocess

THEME_NAME = "YaruBlue"
COLOR_BRIGHT = "#208fe9"       # orange in yaru
COLOR_MID = "#3c6b93"          # aubergine in yaru
COLOR_DARK = "#255074"         # purple in yaru
BG_COLOR_TERMINAL = "#0e1d30"


def replace_in_file(path: Path, search, repl, num_replacements=1):
    # search is a regex pattern
    content = path.read_text()
    (content_new, n_repl) = re.subn(search, repl, content, flags=re.MULTILINE|re.S|re.I)
    if n_repl != num_replacements:
        raise Exception(f"Expected a {num_replacements} replacement(s), found {n_repl} replacement(s).")
    path.write_text(content_new)

# reset submodule
print("Resetting submodule before performing adaptions (`git reset --hard`)...")
subprocess.run(["git", "reset", "--hard"], cwd="yaru")
print("Done.")

# ----------------------------------------------------------------------------
# project build file
# ----------------------------------------------------------------------------
print("Updating theme name...")
replace_in_file(
    Path("yaru/meson.build"),
    "project\('Yaru',", 
    f"project('{THEME_NAME}',"
)
print("Done.")

# ----------------------------------------------------------------------------
# gtk-2
# ----------------------------------------------------------------------------
print("Updating gtk2-dark...")
gtk2_folder = Path("yaru/gtk/src/dark/gtk-2.0")

# replace orange
replace_in_file(
    gtk2_folder / "gtkrc",
    "#E95420", 
    COLOR_BRIGHT,
    num_replacements=1
)
print("Done.")

print("Updating gtk2-default...")
gtk2_folder = Path("yaru/gtk/src/default/gtk-2.0")

# replace orange
replace_in_file(
    gtk2_folder / "gtkrc",
    "#E95420", 
    COLOR_BRIGHT,
    num_replacements=1
)
print("Done.")

print("Updating gtk2-light...")
gtk2_folder = Path("yaru/gtk/src/light/gtk-2.0")

# replace orange
replace_in_file(
    gtk2_folder / "gtkrc",
    "#E95420", 
    COLOR_BRIGHT,
    num_replacements=1
)
print("Done.")



# ----------------------------------------------------------------------------
# gtk-3
# ----------------------------------------------------------------------------
print("Updating gtk3...")
gtk3_folder = Path("yaru/gtk/src/default/gtk-3.20")

# replace orange
replace_in_file(
    gtk3_folder / "_ubuntu-colors.scss", 
    "\$orange: #E95420;", 
    f"$orange: {COLOR_BRIGHT};"
)

# replace purple
replace_in_file(
    gtk3_folder / "_ubuntu-colors.scss", 
    "\$purple: #762572;", 
    f"$purple: {COLOR_DARK};"
)

# replace aubergine
replace_in_file(
    gtk3_folder / "_ubuntu-colors.scss", 
    "\$aubergine: #924D8B;", 
    f"$aubergine: {COLOR_MID};"
)

# replace terminal background color
replace_in_file(
    gtk3_folder / "_apps.scss",
    "\$_terminal_bg_color: #300A24;", 
    f"$_terminal_bg_color: {BG_COLOR_TERMINAL};"
)

print("Done.")


# ----------------------------------------------------------------------------
# gnome-shell
# ----------------------------------------------------------------------------
print("Updating gnome-shell...")

# replace orange
replace_in_file(
    Path("yaru/gnome-shell/src/gnome-shell-sass/_ubuntu-colors.scss"), 
    "\$orange: #E95420;", 
    f"$orange: {COLOR_BRIGHT};"
)

# replace purple
replace_in_file(
    Path("yaru/gnome-shell/src/gnome-shell-sass/_ubuntu-colors.scss"), 
    "\$purple: #762572;", 
    f"$purple: {COLOR_DARK};"
)

# replace aubergine
replace_in_file(
    Path("yaru/gnome-shell/src/gnome-shell-sass/_ubuntu-colors.scss"), 
    "\$aubergine: #924D8B;", 
    f"$aubergine: {COLOR_MID};"
)

# replace `Yaru` aliases in gresource schema
replace_in_file(
    Path("yaru/gnome-shell/src/data/gnome-shell-theme.gresource.xml"), 
    "Yaru", 
    THEME_NAME,
    num_replacements=4
)


print("Done.")

# ----------------------------------------------------------------------------
# gnome-shell-icons
# ----------------------------------------------------------------------------
gnome_shell_icon_folder = Path("yaru/gnome-shell/src")
print("Updating gnome-shell-icons...")

# replace aubergine color in checkboxes and toggles
replace_in_file(
    gnome_shell_icon_folder / "checkbox-dark.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=2
)
replace_in_file(
    gnome_shell_icon_folder / "checkbox-focused-dark.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=1
)
replace_in_file(
    gnome_shell_icon_folder / "checkbox-focused.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=1
)
replace_in_file(
    gnome_shell_icon_folder / "checkbox-off-focused-dark.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=1
)
replace_in_file(
    gnome_shell_icon_folder / "checkbox-off-focused.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=1
)
replace_in_file(
    gnome_shell_icon_folder / "checkbox.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=2
)
replace_in_file(
    gnome_shell_icon_folder / "toggle-on-hc.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=2
)
replace_in_file(
    gnome_shell_icon_folder / "toggle-on-intl.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=1
)
replace_in_file(
    gnome_shell_icon_folder / "toggle-on.svg",
    "#924d8b", 
    COLOR_MID,
    num_replacements=4
)
replace_in_file(
    gnome_shell_icon_folder / "toggle-on-dark.svg",
    "#7c436f", 
    COLOR_MID,
    num_replacements=2
)

print("Done.")


# ----------------------------------------------------------------------------
# icons
# ----------------------------------------------------------------------------
icon_folder = Path("yaru/icons/src/fullcolor")
print("Updating icons...")

# replace colors of desktop icon
replace_in_file(
    icon_folder / "places/user-desktop.svg",
    "stop-color:#fb7c38", 
    f"stop-color:{COLOR_BRIGHT}"
)
replace_in_file(
    icon_folder / "places/user-desktop.svg",
    "stop-color:#9b33ae", 
    f"stop-color:{COLOR_DARK}"
)

# replace colors for folders icon
replace_in_file(
    icon_folder / "places/folders.svg",
    """<stop
         style="stop-color:#2c001e.*<stop
         style="stop-color:#e65524;stop-opacity:1"
         offset="1"
         id="stop36439" />""",
    f"""
      <stop
         style="stop-color:{COLOR_DARK};stop-opacity:1"
         offset="0"
         id="stop36437" />
      <stop
         style="stop-color:{COLOR_BRIGHT};stop-opacity:1"
         offset="1"
         id="stop36439" />"""
)

# replace colors for emblem-symbolic-link icon
replace_in_file(
    icon_folder / "emblems/emblem-symbolic-link.svg",
    "#7d2b51",
    COLOR_DARK,
    num_replacements=6
)


print("Done.")

# render modified icons
print("Rendering modified icons...")
subprocess.run(["python3", "render-bitmaps.py", "folders"], cwd="yaru/icons/src/fullcolor")
subprocess.run(["python3", "render-bitmaps.py", "user-desktop"], cwd="yaru/icons/src/fullcolor")
subprocess.run(["python3", "render-bitmaps.py", "emblem-symbolic-link"], cwd="yaru/icons/src/fullcolor")

print("Done.")

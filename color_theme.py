
from pathlib import Path
import re
import subprocess

THEME_NAME = "YaruBlue"
COLOR_BRIGHT = "#208fe9"       # orange in yaru
COLOR_DARK = "#255074"         # purple in yaru
BG_COLOR_TERMINAL = "#0e1d30"


def replace_in_file(path: Path, search, repl):
    # search is a regex pattern
    content = path.read_text()
    (content_new, n_repl) = re.subn(search, repl, content, flags=re.MULTILINE|re.S)
    if n_repl != 1:
        raise Exception(f"Expected a single replacement, found {n_repl} replacements.")
    path.write_text(content_new)

# reset submodule
print("Resetting submodule before performing adaptions (`git reset --hard`)...")
subprocess.run(["git", "reset", "--hard"], cwd="yaru")
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


print("Done.")

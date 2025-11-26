#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)

from configs.config import *
from configs.util import *
from configs.term import *
from configs.menu_builder import *
import os
import sys
import re
import webbrowser
import subprocess

try:
    import requests
except Exception as e:
    General_Error(e)
    exit()


tool_path = os.path.dirname(os.path.abspath(__file__))
scripts_path = os.path.join(tool_path, "scripts")

line_len = os.get_terminal_size().columns
t_len = (line_len // 3) - 2

# activating venv
if os_name == "Linux":
    venv_python = os.path.join(tool_path, ".venv", "bin", "python3")
else:
    venv_python = os.path.join(tool_path, ".venv", "Scripts", "python.exe")

if not os.path.exists(venv_python):
    print("#>  Please run the setup.py")
elif sys.executable != venv_python:
    os.execv(venv_python, [venv_python] + sys.argv)

# internal tools
int_h = [
    (0, "venv Test ($ env)"),
    (0, "formating test ($ text)"),
]

# ---------------------------------------------------------------------
# BUILD OPTIONS (LIST-BASED)
# ---------------------------------------------------------------------
def build_options(scripts_path):
    # interne Tools hartkodiert
    internal = [
        (0, "venv Test ($ env)"),
        (0, "formating test ($ text)")
    ]

    # Scripts sammeln
    by_header = {}  # header -> [(funct,name),...]
    for file in os.listdir(scripts_path):
        full = os.path.join(scripts_path, file)
        if not os.path.isfile(full):
            continue
        if "_" not in file or "-" not in file:
            print(f"[WARN] invalid filename: {file}")
            continue
        try:
            id_part, name = file.split("_", 1)
            name = name.replace("-", " ")
            name = name[:-3] if name.endswith(".py") else name
            header, funct = id_part.split("-")
            header, funct = int(header), int(funct)
        except:
            print(f"[WARN] not parsable: {file}")
            continue

        if header not in by_header:
            by_header[header] = []
        by_header[header].append((funct, name))

    # Header sortieren
    ordered_headers = sorted(by_header.keys())

    # Page-Struktur aufbauen (3 Tabs pro Page)
    pages = []

    # Page 0 vorbereiten (Internal auf Tab 0)
    page0 = [internal, [], []]
    current_page = page0
    tab_index = 1  # Tab 0 belegt durch internal

    for header in ordered_headers:
        if header == 0:
            continue  # interne bereits drin

        # Funktionen innerhalb des Tabs nach funct sortieren
        by_header[header].sort(key=lambda x: x[0])

        # wenn Tab voll → neue Page
        if tab_index > 2:
            pages.append(current_page)
            current_page = [[], [], []]
            tab_index = 0

        # ganzen header-block in aktuellen Tab schieben
        current_page[tab_index] = by_header[header]

        tab_index += 1

    # letzte Page anhängen
    pages.append(current_page)

    return pages

options = build_options(scripts_path)

def get_tool_script_name(id: str):
    try:
        r_str, i_str = id.split("-")
        r, i = int(r_str), int(i_str)
    except:
        return None

    page_index = r // 3
    tab_index = r % 3

    if page_index >= len(options):
        return None
    page = options[page_index]
    if tab_index >= len(page):
        return None
    tab = page[tab_index]

    if i <= 0 or i > len(tab):
        return None

    funct, name = tab[i - 1]
    if funct == 0:
        return None

    filename_name = name.replace(" ", "-")
    filename = f"{r}-{i}_{filename_name}.py"
    return filename


def StartScript(script_file=str, cwd=tool_path):
    if script_file is None:
        return
    env = os.environ.copy()
    env["PYTHONPATH"] = tool_path
    command = [sys.executable, os.path.join(tool_path, "scripts", script_file)]
    subprocess.run(command, env=env, cwd=cwd)


men_h_txt = [
    [" Intern ", " Network Scanner ", " Osint "],
    [" Utilities ", " Games ", " Social Media "],
    [" Common ", " Math "]
]


def menu_head_builder(menu_index):
    categorys = men_h_txt[menu_index]
    if menu_index == 0:
        start_txt, end_txt = INFO_TXT, NEXT_TXT
    elif menu_index + 1 == len(options):
        start_txt, end_txt = BACK_TXT, END_TXT
    else:
        start_txt, end_txt = BACK_TXT, NEXT_TXT

    rendered_tabs = []
    for cat in categorys:
        l = len(cat)
        a, b, c = f"┌{'─' * l}┐", f"┤{cat}├", f"└{'─' * l}┘"
        blub = t_len - len(a)
        mod = blub % 2
        spacea, spaceb = (blub // 2) - 1, (blub // 2) + mod
        rendered_tabs.append([
            " " * (spacea + 1) + a + " " * spaceb,
            "┬" + "─" * spacea + b + "─" * spaceb,
            "│" + " " * spacea + c + " " * spaceb
        ])

    outa = "".join(tab[0] for tab in rendered_tabs)
    outb = "".join(tab[1] for tab in rendered_tabs)
    outc = "".join(tab[2] for tab in rendered_tabs)

    txt_len = len(start_txt[0])
    outa = "   " + outa
    outb = "   " + outb
    outc = "   " + outc
    outa = start_txt[0] + outa[txt_len:-txt_len] + end_txt[0]
    outb = start_txt[1] + outb[txt_len:-txt_len] + end_txt[1]
    outc = start_txt[2] + outc[txt_len:-txt_len] + end_txt[2]

    return StyleText(" .\n" + outa + "\n" + outb + "\n" + outc, True)


def menu_builder(menu_index):
    menu = "   "
    site_tabs = len(options[menu_index])
    biggest_tab_len = len(max(options[menu_index], key=len))
    for i in range(biggest_tab_len):
        for ti in range(site_tabs):
            options_count = len(options[menu_index][ti])
            if not i >= options_count:
                if i + 1 == options_count:
                    sym = "└"
                else:
                    sym = "├"

                id, option_name = options[menu_index][ti][i]

                if not id == 0:
                    id_str = str(ti + menu_index * 3) + "-" + str(id)
                else:
                    id_str = ".."

                option_string = f"{sym}─ [{id_str}] {option_name}"
                spaces = ' ' * (t_len - len(option_string))
                menu += option_string + spaces
            else:
                menu += "-".center(t_len)
        menu += "\n   "
    return StyleText(menu, True)


# REDTIGER
rt_detected = os.path.exists(os.path.join(scripts_path, "RedTiger-Tools"))
if rt_detected:
    options[0][0].append((0, "RedTiger ($ rt)"))

# UPDATE
v = ""
try:
    new_version = re.search(r'version\s*=\s*"([^"]+)"', requests.get(config_url).text).group(1)
    if version != new_version:
        options[0][0].append((0, "Update available! ($ up)"))
        v = f"New Version: {version} -> {new_version}"
        Clear()
    else:
        v = version
except:
    v = version


menu_index = 0
if __name__ == "__main__":
    while True:
        Clear()
        Title(f"Menu {menu_index}")
        print(StyleText(CenterMultilineText(banner,line_len)))
        print(StyleText(CenterMultilineText("Version: "+v,line_len)))
        print(menu_head_builder(menu_index))
        print(menu_builder(menu_index))

        choice = input(
            StyleText(
                f""" ┌──(user@{tool_name})─[~/{os_name}/Menu-{menu_index}]\n └─$ """,
                True,
                " └┌─()[]~",
            )
            + color.RESET
        )

        if choice in ["N", "n", "NEXT", "Next", "next"]:
            menu_index = (menu_index + 1) % len(options)
        elif choice in ["B", "b", "BACK", "Back", "back"]:
            menu_index = (menu_index - 1) % len(options)

        elif choice in ["Q", "q", "exit", "quit"]:
            exit()

        elif "-" in choice:
            StartScript(get_tool_script_name(choice))

        elif choice == "rt":
            if rt_detected:
                print(StyleText("Launching RedTiger..."))
                StartScript(os.path.join(tool_path, "scripts", "RedTiger-Tools", "Setup.py"))
            else:
                print(rt_error)
            Continue()

        elif choice in ["I", "i", "INFO", "Info", "info"]:
            StartScript(os.path.join("intscripts", "info.py"))
            Continue()

        elif choice == "env":
            print(f"Inside {tool_name}:", sys.executable)
            StartScript(os.path.join("intscripts", "env-check.py"))
            Continue()

        elif choice == "text":
            StartScript(os.path.join("intscripts", "text-style-check.py"))
            Continue()

        elif choice == "up":
            if new_version:
                print(f"{Pre('!')} Please install new version: {version} -> {new_version}")
                if "y" in input(f"{Pre('>')} Open GitHub? (y/n): "):
                    webbrowser.open(github_url)
            else:
                print(f"{Pre('!')} No update.")
            Continue()

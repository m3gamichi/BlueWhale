#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)
from configs.util import *
from configs.term import *
from configs.config import *

try:
    import tkinter as tk
    from tkinter import filedialog
except Exception as e:
    General_Error(e)

Title("Search DataBase")

try:

    def ChooseFolder():
        try:
            print(
                f"\n{Pre(">")} Enter database folder path -> {color.RESET}"
            )
            if sys.platform.startswith("win"):
                root = tk.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "incon.ico"))
                root.withdraw()
                root.attributes("-topmost", True)
                folder_database = filedialog.askdirectory(
                    parent=root, title=f"{name_tool} {version} - Choose a folder"
                )
            elif sys.platform.startswith("linux"):
                folder_database = filedialog.askdirectory(
                    title=f"{name_tool} {version} - Choose a folder"
                )
            print(
                f"{Pre("!")} Folder path: {color.WHITE + folder_database}"
            )
        except:
            folder_database = input(
                f"{Pre(">")} Enter database folder path -> {color.RESET}"
            )

        return folder_database

    folder_database = ChooseFolder()
    search = input(f"{Pre(">")} Search -> {color.RESET}")

    print(f"{Pre("~")} Search in DataBase..")

    def TitleSearch(files_searched, element):
        Title(f"Search DataBase - File Total: {files_searched} - File: {element}")

    try:
        files_searched = 0

        def Check(folder):
            global files_searched
            results_found = False
            folder = os.path.join(folder)
            print(
                f"{Pre("~")} Search in {color.WHITE}{folder}"
            )
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    Check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, "r", encoding="utf-8") as file:
                            line_number = 0
                            files_searched += 1
                            TitleSearch(files_searched, element)
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(
                                        search, f"{color.YELLOW}{search}{color.WHITE}"
                                    )
                                    print(
                                        f"""{color.BLUE}
- Folder : {color.WHITE}{folder}{color.BLUE}
- File   : {color.WHITE}{element}{color.BLUE}
- Line   : {color.WHITE}{line_number}{color.BLUE}
- Result : {color.WHITE}{line_info}
    """
                                    )
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, "r", encoding="latin-1") as file:
                                files_searched += 1
                                line_number = 0
                                TitleSearch(files_searched, element)
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(
                                            search, f"{color.YELLOW}{search}{color.WHITE}"
                                        )
                                        print(
                                            f"""{color.BLUE}
- Folder : {color.WHITE}{folder}{color.BLUE}
- File   : {color.WHITE}{element}{color.BLUE}
- Line   : {color.WHITE}{line_number}{color.BLUE}
- Result : {color.WHITE}{line_info}
    """
                                        )
                        except Exception as e:
                            print(
                                f'{Pre("x",color.RED)} Error reading file "{color.WHITE}{element}{color.BLUE}": {color.WHITE}{e}'
                            )
                    except Exception as e:
                        print(
                            f'{Pre("x",color.RED)} Error reading file "{color.WHITE}{element}{color.BLUE}": {color.WHITE}{e}'
                        )
            return results_found

        results_found = Check(folder_database)
        if not results_found:
            print(
                f'{Pre("!")} No result found for "{color.WHITE}{search}{color.BLUE}".'
            )

        print(
            f"{Pre("!")} Total files searched: {color.WHITE}{files_searched}"
        )

    except Exception as e:
        print(
            f"{Pre("x",color.RED)} Error during search: {color.WHITE}{e}"
        )

    Continue()

except Exception as e:
    General_Error(e)

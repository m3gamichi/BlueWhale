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
    import rarfile
    import pyzipper
    import string
    import tkinter
    from tkinter import filedialog
    from concurrent.futures import ThreadPoolExecutor
except Exception as e:
    General_Error(e)

Title(f"Password Zip Cracked Attack")

try:

    def ChooseZipRarFile():
        try:
            print(
                f"\n{Pre(">")} Enter the path to the .zip or .rar file -> {color.RESET}"
            )
            if sys.platform.startswith("win"):
                root = tkinter.Tk()
                root.iconbitmap(os.path.join(tool_path, "Img", "incon.ico"))
                root.withdraw()
                root.attributes("-topmost", True)
                file = filedialog.askopenfilename(
                    parent=root,
                    title=f"{name_tool} {version} - Choose an icon (.zip / .rar)",
                    filetypes=[
                        ("ZIP/RAR files", "*.zip;*.rar"),
                        ("ZIP files", "*.zip"),
                        ("RAR files", "*.rar"),
                    ],
                )
            elif sys.platform.startswith("linux"):
                file = filedialog.askopenfilename(
                    title=f"{name_tool} {version} - Choose an icon (.ico)",
                    filetypes=[("ICO files", "*.ico")],
                )
            print(
                f"{Pre("!")} File path: {color.WHITE + file}"
            )
            return file
        except:
            return input(
                f"{Pre(">")} Enter the path to the .zip or .rar file -> {color.RESET}"
            )

    def CountEncryptedFiles(file):
        count = 0
        try:
            if file.lower().endswith(".zip"):
                with pyzipper.AESZipFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=b"wrongpassword")
                        except RuntimeError:
                            count += 1
            elif file.lower().endswith(".rar"):
                with rarfile.RarFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd="wrongpassword")
                        except rarfile.BadPassword:
                            count += 1
            return count
        except:
            return count

    def CheckPassword(file, password_test):
        global password_found
        try:
            if file.lower().endswith(".zip"):
                with pyzipper.AESZipFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=password_test.encode())
                            password_found += 1
                            print(
                                f"{Pre("+",color.RED)} File: {color.WHITE + filename} {color.BLUE}Password: {color.WHITE + password_test + color.RESET}"
                            )
                        except:
                            pass
            elif file.lower().endswith(".rar"):
                with rarfile.RarFile(file) as archive:
                    for filename in archive.namelist():
                        try:
                            archive.extract(filename, pwd=password_test.encode())
                            password_found += 1
                            print(
                                f"{Pre("+",color.RED)} File: {color.WHITE + filename} {color.BLUE}Password: {color.WHITE + password_test + color.RESET}"
                            )
                        except:
                            pass
            return password_found > 0
        except:
            return False

    def RandomCharacter(count):
        global generated_passwords, password_found
        try:
            threads_number = int(
                input(
                    f"{Pre(">")} Threads Number -> {color.RESET}"
                )
            )
            characters_number_min = int(
                input(
                    f"{Pre(">")} Password Characters Number Min -> {color.RESET}"
                )
            )
            characters_number_max = int(
                input(
                    f"{Pre(">")} Password Characters Number Max -> {color.RESET}"
                )
            )
        except:
            General_Error("NumberError")

        generated_passwords = set()
        password_found = 0
        all_characters = string.ascii_letters + string.digits + string.punctuation

        def GeneratePassword():
            return "".join(
                random.choice(all_characters)
                for _ in range(
                    random.randint(characters_number_min, characters_number_max)
                )
            )

        def TestCracked():
            global generated_passwords, password_found
            while password_found < count:
                password_test = GeneratePassword()
                if password_test not in generated_passwords:
                    generated_passwords.add(password_test)
                    if CheckPassword(file, password_test):
                        if password_found == count:
                            Continue()

        def Request():
            with ThreadPoolExecutor(max_workers=threads_number) as executor:
                executor.map(lambda _: TestCracked(), range(threads_number))

        print(
            f"{Pre("~")} Brute force password cracking in progress.. (It can be long){color.RESET}"
        )
        while password_found < count:
            Request()

    def WorldList():
        global password_found
        path_folder_worldlist = os.path.join(tool_path, "2-Input", "WorldList")
        files = [
            f
            for f in os.listdir(path_folder_worldlist)
            if os.path.isfile(os.path.join(path_folder_worldlist, f))
        ]
        password_found = 0
        print(
            f"{Pre("!")} Add more list in folder: {color.WHITE + path_folder_worldlist}"
        )
        print(
            f"{Pre("~")} Password cracking by world list in progress.. (It can be long){color.RESET}"
        )

        for file_list in files:
            try:
                with open(
                    os.path.join(path_folder_worldlist, file_list),
                    "r",
                    encoding="utf-8",
                ) as f:
                    for line in f:
                        if CheckPassword(file, line.strip()):
                            if password_found == count:
                                Continue()

            except:
                pass

        if not password_found:
            print(
                f"{Pre("!")} The entire world list has been checked and no passwords match."
            )
            Continue()

    print(decrypted_banner)
    file = ChooseZipRarFile()

    count = CountEncryptedFiles(file)
    print(
        f"{Pre("!")} Number of files protected by password: {color.WHITE + str(count)}"
    )
    if count == 0:
        Continue()

    Title(f"Password Zip Cracked Attack - File: {file}")

    print(
        f"""
 {BEFORE}01{AFTER + color.WHITE} Random Character
 {BEFORE}02{AFTER + color.WHITE} World List
 """
    )

    method = input(f"{Pre(">")} Method -> {color.WHITE}")

    if method in ["01", "1"]:
        RandomCharacter(count)
    elif method in ["02", "2"]:
        WorldList()
    else:
        General_Error("ChoiceError")

except Exception as e:
    General_Error(e)

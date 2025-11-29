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
    import bcrypt
    import hashlib
    import random
    import string
    from concurrent.futures import ThreadPoolExecutor
    import time
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    General_Error(e)

Title(f"Password Decrypted")

try:

    def ErrorDecrypted():
        encryption_map = {
            "1": "BCRYPT",
            "2": "MD5",
            "3": "SHA-1",
            "4": "SHA-256",
            "5": "PBKDF2 (SHA-256)",
            "6": "Base64 Decode",
        }
        encryption = encryption_map.get(choice, "Unknown")
        print(
            f'{Pre("x",color.RED)} The encryption "{color.WHITE + encrypted_password + color.RED}" is not accepted by "{color.WHITE + encryption + color.RED}".'
        )
        Continue()

    def CheckPassword(password_test):
        global salt
        try:
            methods = {
                "1": lambda pwd: bcrypt.checkpw(
                    pwd.encode("utf-8"), encrypted_password.encode("utf-8")
                ),
                "2": lambda pwd: hashlib.md5(pwd.encode("utf-8")).hexdigest()
                == encrypted_password,
                "3": lambda pwd: hashlib.sha1(pwd.encode("utf-8")).hexdigest()
                == encrypted_password,
                "4": lambda pwd: hashlib.sha256(pwd.encode("utf-8")).hexdigest()
                == encrypted_password,
                "5": lambda pwd: pbkdf2_hmac(
                    "sha256", pwd.encode("utf-8"), salt, 100000
                ).hex()
                == encrypted_password,
                "6": lambda pwd: base64.b64decode(
                    encrypted_password.encode("utf-8")
                ).decode("utf-8")
                == pwd,
            }
            return methods.get(choice, lambda _: False)(password_test)
        except:
            ErrorDecrypted()

    def RandomCharacter():
        global password, salt
        try:
            threads_number = int(
                input(
                    f"{Pre(">")} Threads Number -> {color.WHITE}"
                )
            )
            characters_number_min = int(
                input(
                    f"{Pre(">")} Password Characters Number Min -> {color.WHITE}"
                )
            )
            characters_number_max = int(
                input(
                    f"{Pre(">")} Password Characters Number Max -> {color.WHITE}"
                )
            )
        except:
            General_Error("NumberError")

        password = False
        generated_passwords = set()
        salt = "this_is_a_salt".encode("utf-8")
        all_characters = string.ascii_letters + string.digits + string.punctuation

        def GeneratePassword():
            return "".join(
                random.choices(
                    all_characters,
                    k=random.randint(characters_number_min, characters_number_max),
                )
            )

        def TestDecrypted():
            global password
            while not password:
                password_test = GeneratePassword()
                if password_test not in generated_passwords:
                    generated_passwords.add(password_test)
                    if CheckPassword(password_test):
                        password = True
                        time.sleep(0.5)
                        print(
                            f"{Pre("+",color.RED)} Password: {color.WHITE + password_test + color.RESET}"
                        )
                        time.sleep(1)
                        Continue()

        def Request():
            try:
                with ThreadPoolExecutor(max_workers=threads_number) as executor:
                    executor.map(lambda _: TestDecrypted(), range(threads_number))
            except Exception:
                General_Error("NumberError")

        print(
            f"{Pre("~")} Brute force password cracking in progress.. (It can be long){color.RESET}"
        )
        while not password:
            Request()

    def WorldList():
        path_folder_worldlist = os.path.join(scripts_path, "data", "worldlists")
        print(
            f"{Pre("!")} Add more list in folder: {color.WHITE + path_folder_worldlist}"
        )
        print(
            f"{Pre("~")} Password cracking by world list in progress.. (It can be long){color.RESET}"
        )

        for file in os.listdir(path_folder_worldlist):
            try:
                file_path = os.path.join(path_folder_worldlist, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if CheckPassword(line.strip()):
                            print(
                                f"{Pre("+",color.RED)} Password: {color.WHITE + line.strip() + color.RESET}"
                            )
                            Continue()

                            return
            except:
                pass

        print(
            f"{Pre("!")} The entire world list has been checked and no passwords match."
        )
        Continue()

    print(
        f"""{decrypted_banner}
 {color.BLUE}[{color.WHITE}01{AFTER + color.WHITE} BCRYPT
 {color.BLUE}[{color.WHITE}02{AFTER + color.WHITE} MD5
 {color.BLUE}[{color.WHITE}03{AFTER + color.WHITE} SHA-1
 {color.BLUE}[{color.WHITE}04{AFTER + color.WHITE} SHA-256
 {color.BLUE}[{color.WHITE}05{AFTER + color.WHITE} PBKDF2 (SHA-256)
 {color.BLUE}[{color.WHITE}06{AFTER + color.WHITE} Base64 Decode
    """
    )

    choice = input(f"{Pre(">")} Method -> {color.RESET}")

    if choice not in ["1", "01", "2", "02", "3", "03", "4", "04", "5", "05", "6", "06"]:
        General_Error("ChoiceError")

    encrypted_password = input(
        f"{Pre(">")} Encrypted Password -> {color.WHITE}"
    )
    Title(f"Password Decrypted - Encrypted Password: {encrypted_password}")

    print(
        f"""
 {color.BLUE}[{color.WHITE}01{AFTER + color.WHITE} Random Character
 {color.BLUE}[{color.WHITE}02{AFTER + color.WHITE} World List
 """
    )

    method = input(
        f"{Pre(">")} Brute Force Method -> {color.WHITE}"
    )

    if method in ["01", "1"]:
        RandomCharacter()
    elif method in ["02", "2"]:
        WorldList()
    else:
        General_Error("ChoiceError")

except Exception as e:
    General_Error(e)

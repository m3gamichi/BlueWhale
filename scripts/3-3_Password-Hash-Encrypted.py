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
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    General_Error(e)

Title(f"Password Encrypted")
try:
    print(
        f"""{encrypted_banner}
 {color.BLUE}[{color.WHITE}01{color.BLUE}]{color.WHITE} BCRYPT
 {color.BLUE}[{color.WHITE}02{color.BLUE}]{color.WHITE} MD5
 {color.BLUE}[{color.WHITE}03{color.BLUE}]{color.WHITE} SHA-1
 {color.BLUE}[{color.WHITE}04{color.BLUE}]{color.WHITE} SHA-256
 {color.BLUE}[{color.WHITE}05{color.BLUE}]{color.WHITE} PBKDF2 (SHA-256)
 {color.BLUE}[{color.WHITE}06{color.BLUE}]{color.WHITE} Base64 Decode
    """
    )

    choice = input(
        f"{Pre(">")} Encryption Method -> {color.RESET}"
    )

    if choice not in ["1", "01", "2", "02", "3", "03", "4", "04", "5", "05", "6", "06"]:
        General_Error("ChoiceError")

    password = input(
        f"{Pre(">")} Password to Encrypt -> {color.WHITE}"
    )

    def EncryptPassword(choice, password):
        encrypt_methods = {
            "1": lambda p: bcrypt.hashpw(p.encode("utf-8"), bcrypt.gensalt()).decode(
                "utf-8"
            ),
            "2": lambda p: hashlib.md5(p.encode("utf-8")).hexdigest(),
            "3": lambda p: hashlib.sha1(p.encode("utf-8")).hexdigest(),
            "4": lambda p: hashlib.sha256(p.encode("utf-8")).hexdigest(),
            "5": lambda p: pbkdf2_hmac(
                "sha256", p.encode("utf-8"), "this_is_a_salt".encode("utf-8"), 100000
            ).hex(),
            "6": lambda p: base64.b64encode(p.encode("utf-8")).decode("utf-8"),
        }

        try:
            return encrypt_methods.get(choice, lambda p: None)(password)
        except Exception as e:
            print(
                f"{Pre("x",color.RED)} Error during encryption: {e}"
            )
            return None

    encrypted_password = EncryptPassword(choice, password)
    if encrypted_password:
        print(
            f"{Pre("+",color.RED)} Encrypted Password: {color.WHITE}{encrypted_password}{color.RESET}"
        )
        Continue()


except Exception as e:
    General_Error(e)

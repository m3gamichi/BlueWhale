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
    import requests
except Exception as e:
    General_Error(e)

Title("Roblox User Info")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    print(
        f"\n{Pre("!")} Selected User-Agent: {color.WHITE + user_agent}"
    )
    username_input = input(
        f"{Pre(">")} Username -> {color.RESET}"
    )
    print(
        f"{Pre("~")} Information Recovery..{color.RESET}"
    )

    try:
        response = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            headers=headers,
            json={"usernames": [username_input], "excludeBannedUsers": "true"},
        )

        data = response.json()

        user_id = data["data"][0]["id"]

        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        api = response.json()

        userid = api.get("id", "None")
        display_name = api.get("displayName", "None")
        username = api.get("name", "None")
        description = api.get("description", "None")
        created_at = api.get("created", "None")
        is_banned = api.get("isBanned", "None")
        external_app_display_name = api.get("externalAppDisplayName", "None")
        has_verified_badge = api.get("hasVerifiedBadge", "None")

        print(
            f"""
    {Pre("+",color.BLUE)} Username       : {color.WHITE}{username}{color.BLUE}
    {Pre("+",color.BLUE)} Id             : {color.WHITE}{userid}{color.BLUE}
    {Pre("+",color.BLUE)} Display Name   : {color.WHITE}{display_name}{color.BLUE}
    {Pre("+",color.BLUE)} Description    : {color.WHITE}{description}{color.BLUE}
    {Pre("+",color.BLUE)} Created        : {color.WHITE}{created_at}{color.BLUE}
    {Pre("+",color.BLUE)} Banned         : {color.WHITE}{is_banned}{color.BLUE}
    {Pre("+",color.BLUE)} External Name  : {color.WHITE}{external_app_display_name}{color.BLUE}
    {Pre("+",color.BLUE)} Verified Badge : {color.WHITE}{has_verified_badge}{color.BLUE}
    """
        )
        Continue()

    except:
        General_Error("UsernameError")
except Exception as e:
    General_Error(e)

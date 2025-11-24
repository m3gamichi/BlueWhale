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

Title("Discord Server Info")

try:
    print(discord_banner)
    invite = input(
        f"{Pre(">")} Server Invitation -> {color.RESET}"
    )
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code == 200:
        api = response.json()

        type_value = api.get("type", "None")
        code_value = api.get("code", "None")
        inviter_info = api.get("inviter", {})
        inviter_id = inviter_info.get("id", "None")
        inviter_username = inviter_info.get("username", "None")
        inviter_avatar = inviter_info.get("avatar", "None")
        inviter_discriminator = inviter_info.get("discriminator", "None")
        inviter_public_flags = inviter_info.get("public_flags", "None")
        inviter_flags = inviter_info.get("flags", "None")
        inviter_banner = inviter_info.get("banner", "None")
        inviter_accent_color = inviter_info.get("accent_color", "None")
        inviter_global_name = inviter_info.get("global_name", "None")
        inviter_banner_color = inviter_info.get("banner_color", "None")
        expires_at = api.get("expires_at", "None")
        flags = api.get("flags", "None")
        server_info = api.get("guild", {})
        server_id = server_info.get("id", "None")
        server_name = server_info.get("name", "None")
        server_icon = server_info.get("icon", "None")
        server_features = server_info.get("features", "None")
        if server_features != "None":
            server_features = " / ".join(server_features)
        server_verification_level = server_info.get("verification_level", "None")
        server_nsfw_level = server_info.get("nsfw_level", "None")
        server_descritpion = server_info.get("description", "None")
        server_nsfw = server_info.get("nsfw", "None")
        server_premium_subscription_count = server_info.get(
            "premium_subscription_count", "None"
        )
        channel_info = api.get("channel", {})
        channel_id = channel_info.get("id", "None")
        channel_type = channel_info.get("type", "None")
        channel_name = channel_info.get("name", "None")
    else:
        General_Error("UrlError")

    print(
        f"""{color.BLUE}
    Invitation Information:
    {Pre("+",color.BLUE)} Invitation         : {color.WHITE}{invite}{color.BLUE}
    {Pre("+",color.BLUE)} Type               : {color.WHITE}{type_value}{color.BLUE}
    {Pre("+",color.BLUE)} Code               : {color.WHITE}{code_value}{color.BLUE}
    {Pre("+",color.BLUE)} Expired            : {color.WHITE}{expires_at}{color.BLUE}
    {Pre("+",color.BLUE)} Server ID          : {color.WHITE}{server_id}{color.BLUE}
    {Pre("+",color.BLUE)} Server Name        : {color.WHITE}{server_name}{color.BLUE}
    {Pre("+",color.BLUE)} Channel ID         : {color.WHITE}{channel_id}{color.BLUE}
    {Pre("+",color.BLUE)} Channel Name       : {color.WHITE}{channel_name}{color.BLUE}
    {Pre("+",color.BLUE)} Channel Type       : {color.WHITE}{channel_type}{color.BLUE}
    {Pre("+",color.BLUE)} Server Description : {color.WHITE}{server_descritpion}{color.BLUE}
    {Pre("+",color.BLUE)} Server Icon        : {color.WHITE}{server_icon}{color.BLUE}
    {Pre("+",color.BLUE)} Server Features    : {color.WHITE}{server_features}{color.BLUE}
    {Pre("+",color.BLUE)} Server NSFW Level  : {color.WHITE}{server_nsfw_level}{color.BLUE}
    {Pre("+",color.BLUE)} Server NSFW        : {color.WHITE}{server_nsfw}{color.BLUE}
    {Pre("+",color.BLUE)} Flags              : {color.WHITE}{flags}{color.BLUE}
    {Pre("+",color.BLUE)} Server Verification Level         : {color.WHITE}{server_verification_level}{color.BLUE}
    {Pre("+",color.BLUE)} Server Premium Subscription Count : {color.WHITE}{server_premium_subscription_count}{color.BLUE}
"""
    )

    if inviter_info:
        print(
            f"""    {color.BLUE}Inviter Information:
    {Pre("+",color.BLUE)} ID            : {color.WHITE}{inviter_id}{color.BLUE}
    {Pre("+",color.BLUE)} Username      : {color.WHITE}{inviter_username}{color.BLUE}
    {Pre("+",color.BLUE)} Global Name   : {color.WHITE}{inviter_global_name}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar        : {color.WHITE}{inviter_avatar}{color.BLUE}
    {Pre("+",color.BLUE)} Discriminator : {color.WHITE}{inviter_discriminator}{color.BLUE}
    {Pre("+",color.BLUE)} Public Flags  : {color.WHITE}{inviter_public_flags}{color.BLUE}
    {Pre("+",color.BLUE)} Flags         : {color.WHITE}{inviter_flags}{color.BLUE}
    {Pre("+",color.BLUE)} Banner        : {color.WHITE}{inviter_banner}{color.BLUE}
    {Pre("+",color.BLUE)} Accent Color  : {color.WHITE}{inviter_accent_color}{color.BLUE}
    {Pre("+",color.BLUE)} Banner Color  : {color.WHITE}{inviter_banner_color}{color.BLUE}
    """
        )
    Continue()

except Exception as e:
    General_Error(e)

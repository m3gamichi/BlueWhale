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


Title("Discord Webhook Info")

try:

    def info_webhook(webhook_url):
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get(webhook_url, headers=headers)
        webhook_info = response.json()

        webhook_id = webhook_info.get("id", "None")
        webhook_token = webhook_info.get("token", "None")
        webhook_name = webhook_info.get("name", "None")
        webhook_avatar = webhook_info.get("avatar", "None")
        webhook_type = "bot" if webhook_info.get("type") == 1 else "webhook utilisateur"
        channel_id = webhook_info.get("channel_id", "None")
        guild_id = webhook_info.get("guild_id", "None")

        print(
            f"""
    {Pre("+",color.BLUE)} ID         : {color.WHITE}{webhook_id}{color.BLUE}
    {Pre("+",color.BLUE)} Token      : {color.WHITE}{webhook_token}{color.BLUE}
    {Pre("+",color.BLUE)} Name       : {color.WHITE}{webhook_name}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar     : {color.WHITE}{webhook_avatar}{color.BLUE}
    {Pre("+",color.BLUE)} Type       : {color.WHITE}{webhook_type}{color.BLUE}
    {Pre("+",color.BLUE)} Channel ID : {color.WHITE}{channel_id}{color.BLUE}
    {Pre("+",color.BLUE)} Server ID  : {color.WHITE}{guild_id}{color.BLUE}
    """
        )

        if "user" in webhook_info:
            user_info = webhook_info["user"]

            user_id = user_info.get("id", "None")
            username = user_info.get("username", "None")
            display_name = user_info.get("global_name", "None")
            discriminator = user_info.get("discriminator", "None")
            user_avatar = user_info.get("avatar", "None")
            user_flags = user_info.get("flags", "None")
            accent_color = user_info.get("accent_color", "None")
            avatar_decoration = user_info.get("avatar_decoration_data", "None")
            banner_color = user_info.get("banner_color", "None")

            print(
                f"""
    {color.BLUE}User information associated with the Webhook:
    {Pre("+",color.BLUE)} ID          : {color.WHITE}{user_id}{color.BLUE}
    {Pre("+",color.BLUE)} Name        : {color.WHITE}{username}{color.BLUE}
    {Pre("+",color.BLUE)} DisplayName : {color.WHITE}{display_name}{color.BLUE}
    {Pre("+",color.BLUE)} Number      : {color.WHITE}{discriminator}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar      : {color.WHITE}{user_avatar}{color.BLUE}
    {Pre("+",color.BLUE)} Flags       : {color.WHITE}{user_flags} Publique: {user_flags}{color.BLUE}
    {Pre("+",color.BLUE)} Color       : {color.WHITE}{accent_color}{color.BLUE}
    {Pre("+",color.BLUE)} Decoration  : {color.WHITE}{avatar_decoration}{color.BLUE}
    {Pre("+",color.BLUE)} Banner      : {color.WHITE}{banner_color}{color.BLUE}
    """
            )

    webhook_url = input(
        f"\n{Pre(">")} Webhook URL -> {color.RESET}"
    )
    if CheckWebhook(webhook_url) == False:
        General_Error("WebhookError")
    info_webhook(webhook_url)
    Continue()

except Exception as e:
    General_Error(e)

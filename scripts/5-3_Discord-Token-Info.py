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
    from datetime import datetime, timezone
except Exception as e:
    General_Error(e)

def Choice1TokenDiscord():
    def CheckToken(token_number, token):
        response = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={"Authorization": token, "Content-Type": "application/json"},
        )

        if response.status_code == 200:
            user = requests.get(
                "https://discord.com/api/v8/users/@me", headers={"Authorization": token}
            ).json()
            username_discord = user["username"]
            token_sensur = token[:-25] + "." * 3
            print(
                f" {BEFORE}{token_number}{AFTER} -> {color.BLUE}Status: {color.WHITE}Valid{color.BLUE} | User: {color.WHITE}{username_discord}{color.BLUE} | Token: {color.WHITE}{token_sensur}"
            )
        else:
            print(
                f" {BEFORE}{token_number}{AFTER} -> {color.BLUE}Status: {color.WHITE}Invalid{color.BLUE} | {color.BLUE}Token: {color.WHITE}{token}"
            )

    file_token_discord_relative = "\\2-Input\\TokenDisc\\TokenDisc.txt"
    file_token_discord = os.path.join(
        tool_path, "2-Input", "TokenDisc", "TokenDisc.txt"
    )

    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, "r") as file_token:
        print(
            f"{Pre("!")} Token Discord ({color.WHITE}{file_token_discord_relative}{color.BLUE}):\n"
        )
        for line in file_token:
            if not line.strip() or line.isspace():
                continue

            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    if not tokens:
        print(
            f"{Pre("!")} No Token Discord in file: {color.WHITE}{file_token_discord_relative}{color.BLUE} Please add tokens to the file."
        )
        Continue()

        return None

    try:
        selected_token_number = int(
            input(
                f"\n{Pre(">")} Token Number -> {color.RESET}"
            )
        )
    except:
        General_Error("ChoiceError")

    selected_token = tokens.get(selected_token_number)
    if selected_token:
        r = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={
                "Authorization": selected_token,
                "Content-Type": "application/json",
            },
        )
        if r.status_code == 200:
            pass
        else:
            General_Error("TokenError")
    else:
        General_Error("ChoiceError")
    return selected_token


Title("Discord Token Info")

try:
    print(discord_banner)
    token_discord = Choice1TokenDiscord()
    print(
        f"{Pre("~")} Information Recovery..{color.RESET}"
    )
    try:
        api = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={"Authorization": token_discord},
        ).json()

        response = requests.get(
            "https://discord.com/api/v8/users/@me",
            headers={
                "Authorization": token_discord,
                "Content-Type": "application/json",
            },
        )

        if response.status_code == 200:
            status = "Valid"
        else:
            status = "Invalid"

        username_discord = (
            api.get("username", "None") + "#" + api.get("discriminator", "None")
        )
        display_name_discord = api.get("global_name", "None")
        user_id_discord = api.get("id", "None")
        email_discord = api.get("email", "None")
        email_verified_discord = api.get("verified", "None")
        phone_discord = api.get("phone", "None")
        mfa_discord = api.get("mfa_enabled", "None")
        country_discord = api.get("locale", "None")
        avatar_discord = api.get("avatar", "None")
        avatar_decoration_discord = api.get("avatar_decoration_data", "None")
        public_flags_discord = api.get("public_flags", "None")
        flags_discord = api.get("flags", "None")
        banner_discord = api.get("banner", "None")
        banner_color_discord = api.get("banner_color", "None")
        accent_color_discord = api.get("accent_color", "None")
        nsfw_discord = api.get("nsfw_allowed", "None")

        try:
            created_at_discord = datetime.fromtimestamp(
                ((int(api.get("id", "None")) >> 22) + 1420070400000) / 1000,
                timezone.utc,
            )
        except:
            created_at_discord = "None"

        try:
            if api.get("premium_type", "None") == 0:
                nitro_discord = "False"
            elif api.get("premium_type", "None") == 1:
                nitro_discord = "Nitro Classic"
            elif api.get("premium_type", "None") == 2:
                nitro_discord = "Nitro Boosts"
            elif api.get("premium_type", "None") == 3:
                nitro_discord = "Nitro Basic"
            else:
                nitro_discord = "False"
        except:
            nitro_discord = "None"

        try:
            avatar_url_discord = (
                f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif"
                if requests.get(
                    f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif"
                ).status_code
                == 200
                else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"
            )
        except:
            avatar_url_discord = "None"

        try:
            linked_users_discord = api.get("linked_users", "None")
            linked_users_discord = " / ".join(linked_users_discord)
            if not linked_users_discord.strip():
                linked_users_discord = "None"
        except:
            linked_users_discord = "None"

        try:
            bio_discord = "\n" + api.get("bio", "None")
            if not bio_discord.strip() or bio_discord.isspace():
                bio_discord = "None"
        except:
            bio_discord = "None"

        try:
            authenticator_types_discord = api.get("authenticator_types", "None")
            authenticator_types_discord = " / ".join(authenticator_types_discord)
        except:
            authenticator_types_discord = "None"

        try:
            guilds_response = requests.get(
                "https://discord.com/api/v9/users/@me/guilds?with_counts=true",
                headers={"Authorization": token_discord},
            )
            if guilds_response.status_code == 200:
                guilds = guilds_response.json()
                try:
                    guild_count = len(guilds)
                except:
                    guild_count = "None"
                try:
                    owner_guilds = [guild for guild in guilds if guild["owner"]]
                    owner_guild_count = f"({len(owner_guilds)})"
                    owner_guilds_names = []
                    if owner_guilds:
                        for guild in owner_guilds:
                            owner_guilds_names.append(
                                f"{guild['name']} ({guild['id']})"
                            )
                        owner_guilds_names = "\n" + "\n".join(owner_guilds_names)
                except:
                    owner_guild_count = "None"
                    owner_guilds_names = "None"
        except:
            owner_guild_count = "None"
            guild_count = "None"
            owner_guilds_names = "None"

        try:
            billing_discord = requests.get(
                "https://discord.com/api/v6/users/@me/billing/payment-sources",
                headers={"Authorization": token_discord},
            ).json()
            if billing_discord:
                payment_methods_discord = []

                for method in billing_discord:
                    if method["type"] == 1:
                        payment_methods_discord.append("CB")
                    elif method["type"] == 2:
                        payment_methods_discord.append("Paypal")
                    else:
                        payment_methods_discord.append("Other")
                payment_methods_discord = " / ".join(payment_methods_discord)
            else:
                payment_methods_discord = "None"
        except:
            payment_methods_discord = "None"

        try:
            friends = requests.get(
                "https://discord.com/api/v8/users/@me/relationships",
                headers={"Authorization": token_discord},
            ).json()
            if friends:
                friends_discord = []
                for friend in friends:
                    unprefered_flags = [64, 128, 256, 1048704]
                    data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})"

                    if len("\n".join(friends_discord)) + len(data) >= 1024:
                        break

                    friends_discord.append(data)

                if len(friends_discord) > 0:
                    friends_discord = "\n" + " / ".join(friends_discord)
                else:
                    friends_discord = "None"
            else:
                friends_discord = "None"
        except:
            friends_discord = "None"

        try:
            gift_codes = requests.get(
                "https://discord.com/api/v9/users/@me/outbound-promotions/codes",
                headers={"Authorization": token_discord},
            ).json()
            if gift_codes:
                codes = []
                for gift_codes_discord in gift_codes:
                    name = gift_codes_discord["promotion"]["outbound_title"]
                    gift_codes_discord = gift_codes_discord["code"]
                    data = f"Gift: {name}\nCode: {gift_codes_discord}"
                    if len("\n\n".join(gift_codes_discord)) + len(data) >= 1024:
                        break
                    gift_codes_discord.append(data)
                if len(gift_codes_discord) > 0:
                    gift_codes_discord = "\n\n".join(gift_codes_discord)
                else:
                    gift_codes_discord = "None"
            else:
                gift_codes_discord = "None"
        except:
            gift_codes_discord = "None"

    except Exception as e:
        print(
            f"{Pre("x",color.RED)} Error when retrieving information: {color.WHITE}{e}"
        )

    print(
        f"""
    {Pre("+",color.BLUE)} Status       : {color.WHITE}{status}{color.BLUE}
    {Pre("+",color.BLUE)} Token        : {color.WHITE}{token_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Username     : {color.WHITE}{username_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Display Name : {color.WHITE}{display_name_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Id           : {color.WHITE}{user_id_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Created      : {color.WHITE}{created_at_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Country      : {color.WHITE}{country_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Email        : {color.WHITE}{email_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Verified     : {color.WHITE}{email_verified_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Phone        : {color.WHITE}{phone_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Nitro        : {color.WHITE}{nitro_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Linked Users : {color.WHITE}{linked_users_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar Decor : {color.WHITE}{avatar_decoration_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar       : {color.WHITE}{avatar_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Avatar URL   : {color.WHITE}{avatar_url_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Accent Color : {color.WHITE}{accent_color_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Banner       : {color.WHITE}{banner_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Banner Color : {color.WHITE}{banner_color_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Flags        : {color.WHITE}{flags_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Public Flags : {color.WHITE}{public_flags_discord}{color.BLUE}
    {Pre("+",color.BLUE)} NSFW         : {color.WHITE}{nsfw_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Multi-Factor Authentication : {color.WHITE}{mfa_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Authenticator Type          : {color.WHITE}{authenticator_types_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Billing      : {color.WHITE}{payment_methods_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Gift Code    : {color.WHITE}{gift_codes_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Guilds       : {color.WHITE}{guild_count}{color.BLUE}
    {Pre("+",color.BLUE)} Owner Guilds : {color.WHITE}{owner_guild_count}{owner_guilds_names}{color.BLUE}
    {Pre("+",color.BLUE)} Bio          : {color.WHITE}{bio_discord}{color.BLUE}
    {Pre("+",color.BLUE)} Friend       : {color.WHITE}{friends_discord}{color.BLUE}
    """
    )
    Continue()

except Exception as e:
    General_Error(e)

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

Title("Ip Lookup")

try:
    print(map_banner)
    ip = input(f"\n{Pre(">")} Ip -> {color.RESET}")
    print(f"{Pre("~")} Search for information..")

    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip}")
        api = response.json()

        ip = api.get("ip")
        status = api.get("status")
        country = api.get("country")
        country_code = api.get("country_code")
        region = api.get("region")
        region_code = api.get("region_code")
        zip = api.get("zip")
        city = api.get("city")
        latitude = api.get("latitude")
        longitude = api.get("longitude")
        timezone = api.get("timezone")
        isp = api.get("isp")
        org = api.get("org")
        as_host = api.get("as")

    except:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valid" if api.get("status") == "success" else "Invalid"
        country = api.get("country", "None")
        country_code = api.get("countryCode", "None")
        region = api.get("regionName", "None")
        region_code = api.get("region", "None")
        zip = api.get("zip", "None")
        city = api.get("city", "None")
        latitude = api.get("lat", "None")
        longitude = api.get("lon", "None")
        timezone = api.get("timezone", "None")
        isp = api.get("isp", "None")
        org = api.get("org", "None")
        as_host = api.get("as", "None")

    print(
        f"""    
    {Pre("+",color.BLUE)} Status    : {color.WHITE}{status}{color.BLUE}
    {Pre("+",color.BLUE)} Country   : {color.WHITE}{country} ({country_code}){color.BLUE}
    {Pre("+",color.BLUE)} Region    : {color.WHITE}{region} ({region_code}){color.BLUE}
    {Pre("+",color.BLUE)} Zip       : {color.WHITE}{zip}{color.BLUE}
    {Pre("+",color.BLUE)} City      : {color.WHITE}{city}{color.BLUE}
    {Pre("+",color.BLUE)} Latitude  : {color.WHITE}{latitude}{color.BLUE}
    {Pre("+",color.BLUE)} Longitude : {color.WHITE}{longitude}{color.BLUE}
    {Pre("+",color.BLUE)} Timezone  : {color.WHITE}{timezone}{color.BLUE}
    {Pre("+",color.BLUE)} Isp       : {color.WHITE}{isp}{color.BLUE}
    {Pre("+",color.BLUE)} Org       : {color.WHITE}{org}{color.BLUE}
    {Pre("+",color.BLUE)} As        : {color.WHITE}{as_host}{color.BLUE}{color.RESET}
    """
    )

    Continue()

except Exception as e:
    General_Error(e)

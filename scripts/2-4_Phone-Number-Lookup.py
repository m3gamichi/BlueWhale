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
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
    General_Error(e)


Title("Phone Number Lookup")

try:
    phone_number = input(
        f"\n{Pre(">")} Phone Number -> {color.RESET}"
    )
    print(
        f"{Pre("~")} Information Recovery..{color.RESET}"
    )
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            status = "Valid"
        else:
            status = "Invalid"

        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3]
        else:
            country_code = "None"
        try:
            operator = carrier.name_for_number(parsed_number, "fr")
        except:
            operator = "None"

        try:
            type_number = (
                "Mobile"
                if phonenumbers.number_type(parsed_number)
                == phonenumbers.PhoneNumberType.MOBILE
                else "Fixe"
            )
        except:
            type_number = "None"

        try:
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
        except:
            timezone_info = "None"

        try:
            country = phonenumbers.region_code_for_number(parsed_number)
        except:
            country = "None"

        try:
            region = geocoder.description_for_number(parsed_number, "fr")
        except:
            region = "None"

        try:
            formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL
            )
        except:
            formatted_number = "None"

        print(
            f"""
    {Pre("+",color.BLUE)} Phone        : {color.WHITE}{phone_number}{color.BLUE}
    {Pre("+",color.BLUE)} Formatted    : {color.WHITE}{formatted_number}{color.BLUE}
    {Pre("+",color.BLUE)} Status       : {color.WHITE}{status}{color.BLUE}
    {Pre("+",color.BLUE)} Country Code : {color.WHITE}{country_code}{color.BLUE}
    {Pre("+",color.BLUE)} Country      : {color.WHITE}{country}{color.BLUE}
    {Pre("+",color.BLUE)} Region       : {color.WHITE}{region}{color.BLUE}
    {Pre("+",color.BLUE)} Timezone     : {color.WHITE}{timezone_info}{color.BLUE}
    {Pre("+",color.BLUE)} Operator     : {color.WHITE}{operator}{color.BLUE}
    {Pre("+",color.BLUE)} Type Number  : {color.WHITE}{type_number}{color.BLUE}
    """
        )
        Continue()

    except:
        print(f"{Pre("!")} Invalid Format !")
        Continue()

except Exception as e:
    General_Error(e)

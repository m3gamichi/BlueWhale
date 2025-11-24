from configs.util import *
from configs.term import *
from configs.config import *
from os import system, path

Title("Info")
try:
    import webbrowser

    print(
        f"\n{Pre("~")} Information Recovery..{color.RESET}"
    )

    w_str = ""
    for w in Websites:
        w_str += f"   - {w}\n"
    print(
        f"""
    {Pre("+",color.BLUE)} Tool Name:  {color.WHITE}{tool_name}
    {Pre("+",color.BLUE)} Tool Type:  {color.WHITE}{type_tool}
    {Pre("+",color.BLUE)} Version  :  {color.WHITE}{version}
    {Pre("+",color.BLUE)} Platform :  {color.WHITE}{platform}
    {Pre("+",color.BLUE)} Github   :  {color.WHITE}{github_url}
    {Pre("+",color.BLUE)} License  :  {color.WHITE}{license}

    {Pre("+",color.BLUE)} Main-Dev :  {color.WHITE}{main_dev}
    {Pre("+",color.BLUE)} creator  :  {color.WHITE}{creator}
    Websites:
    {w_str}
    """
    )

    license_read = input(
        f"{Pre(">")} Open 'LICENSE' ? (y/n) -> {color.RESET}"
    )
    if license_read in ["y", "Y", "Yes", "yes", "YES"]:
        if os_name == "Linux":
            system("sdg-open "+path.join(tool_path,license))
        else:
            system("start "+path.join(tool_path,license))


except Exception as e:
    General_Error(e)

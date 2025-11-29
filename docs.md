# How to write your own Tools for BlueWhale


## Basic Script Sctructure:
```
from configs.util import *
from configs.term import *
from configs.config import *

try:
    [SCRIPT DEPENDENCYS]
except Exception as e:
    General_Error(e)

Title("Website Scanner")

try:
    [YOUR CODE]
except Exception as e:
    General_Error(e)
```


## Helper function you can use:
- ### from utils.py
    1. `Continue()` -> prompts the user to press a key to continue
    2. `current_time_day_hour()` -> current time in format "%Y-%m-%d %H:%M:%S"
    3. `current_time_hour()` -> current time in format "%H:%M:%S"
    4. `Title(str)` -> sets the title in the terminal.
    5. `Clear()` -> clears the terminal (platform undependent)
    4. `GeneralError(Exception)` -> handles errors (implements general errors and Custom error:
    > - ChoiceError
    > - IdError
    > - UrlError
    > - TokenError
    > - NumberError
    > - UsernameError
    > - PlatformError)
    5. `Pre(info_str)` -> returns a string with the current Time and colored in. example use: print(Pre("x",color.RED)+"Something went wrong"), u can find various examples for symbols below:
    > - INPUT = ">"
    > - INFO  = "!"
    > - ERROR = "x"
    > - ADD   = "+"
    > - WAIT  = "~"
    > - NOTE  = "NOTE"
    > those are simmilar to the RedTiger theme
- ### from term.py
    1. `create_gradient(color1:tuple, color2:tuple, steps:int)` returns a tuple of r,g,b integers. if u want to make the default gradient use `accent_color_a` and `accent_color_a` from the config.py with 15 steps
    2. `StyleText(string)` and `UnStyleText(string)` will return a colored string in the BlueWhale theme, simply print it with `print()`
    3. `CenterMultilineText(string)` does what it says


## Colors
colorc can be acessed via the color object. (u dont need to import colorama).
some example colors for formating your text output are:
- color.GREEN
- color.BLUE
- color.RED
- color.GREEN
- color.YELLOW
- color.WHITE
- color.RESET
> a reset resets the colors to the terminal defalut colors, it is recommended to put a reset at the end of a input statement.



## Banners
u can print some banner using print():
- tor_banner
- discord_banner
- dox_banner
- osint_banner
- wifi_banner
- phishing_banner
- decrypted_banner
- encrypted_banner
- scan_banner
- sql_banner
- map_banner
- virus_banner

## usefull variables
- util.py
    1. `os_name` is "Linux","Windows" or "Unknown"
    2. `tool_path` the absolute path of the BlueWhale folder
    3. `scripts_path` tool_path + "scripts"
- config.py
    1. general variables: `tool_name`, `version`, `github_url`, `config_url`, `main_dev`, `license`
    2. `accent_color_a` and `accent_color_a` as rgb tuples
    3. `banner` the BlueWhale banner


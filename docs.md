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
5. Pre(info_str) -> returns a string with the current Time and colored in. example use: print(Pre("x",color.RED)+"Something went wrong"), u can find various examples for symbols below:
> - INPUT = ">"
> - INFO  = "!"
> - ERROR = "x"
> - ADD   = "+"
> - WAIT  = "~"
> - NOTE  = "NOTE"
> those are simmilar to the RedTiger theme


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
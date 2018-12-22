db-banner-script 
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
--------------------------
A python script for generating community award banners for devbest.com

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample50_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample525_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample389_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample999_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample366_.png)


Variables to config in `script.py`
```python
# Fill these values
CONFIG["USER"] = "Griimnak"
CONFIG["AWARD"] = "Friendliest User"

CONFIG["OPEN_WHEN_COMPLETE"] = True
# Should I open the image when done? True or False

# These default values should be okay.
CONFIG["AWARD_YEAR_TEXT"] = "2018 Community Awards"
CONFIG["DEVBEST_TEXT"] = "DevBest.com"

CONFIG["USER_X_POS"] = 50
CONFIG["USER_Y_POS"] = 15

CONFIG["AWARD_X_POS"] = 50
CONFIG["AWARD_Y_POS"] = 31

CONFIG["AWARD_YEAR_X_POS"] = 350
CONFIG["AWARD_YEAR_Y_POS"] = 15

CONFIG["DEVBEST_TEXT_X_POS"] = 418
CONFIG["DEVBEST_TEXT_Y_POS"] = 31

CONFIG["BORDER"] = True
CONFIG["BORDER_OUTER_COLOR"] = "black"
CONFIG["BORDER_INNER_COLOR"] = "white"

# Assets
CONFIG["MEDAL_IMAGE"] = "assets/medal2.png"
CONFIG["BG_IMAGE"] = "assets/bg.png"

CONFIG["STANDARD_TTF"] = "assets/Roboto-Regular.ttf"
CONFIG["BOLD_TTF"] = "assets/Roboto-Bold.ttf"
```


Usage:
```sh
$ pip install Pillow
```

```sh
$ python script.py
```

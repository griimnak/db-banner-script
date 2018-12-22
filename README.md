db-banner-script 
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
--------------------------
A python script for generating community award banners for devbest.com

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample366_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample389_.png)

![Alt Text](https://github.com/griimnak/db-banner-script/blob/master/samples/banner_sample371_.png)

Variables to config in `script.py`
```python
# Fill these values
USER = "Griimnak"
AWARD = "Friendliest User"


# These default values should be okay.
AWARD_YEAR_TEXT = "2018 Community Awards"
DEVBEST_TEXT = "DevBest.com"

USER_X_POS = 50
USER_Y_POS = 15

AWARD_X_POS = 50
AWARD_Y_POS = 31

AWARD_YEAR_X_POS = 350
AWARD_YEAR_Y_POS = 15

DEVBEST_TEXT_X_POS = 419
DEVBEST_TEXT_Y_POS = 31

# Assets
MEDAL_IMAGE = "assets/medal.png"
BG_IMAGE = "assets/bg2.png"

STANDARD_TTF = "assets/Roboto-Regular.ttf"
BOLD_TTF = "assets/Roboto-Bold.ttf"
```


Usage:
```sh
$ pip install Pillow
```

```sh
$ python script.py
```

db-banner-script
--------------------------
A python script for generating community award banners for devbest.com

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

""" pip install Pillow """
import os
import random
from PIL import Image, ImageDraw, ImageFont
CONFIG = {}

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


""" Do not modify anything below unless you know what you're doing. """

def show_all_options():
    """ Prints all options to console """
    os.system('cls' if os.name == 'nt' else 'clear')

    for key in CONFIG:
        print(key + "  = ", CONFIG[key])

def main():
    """ Creates the image """
    image = Image.open(CONFIG["BG_IMAGE"]).convert("RGBA")
    std = ImageFont.truetype(CONFIG["STANDARD_TTF"], 12)
    bld = ImageFont.truetype(CONFIG["BOLD_TTF"], 12)
    try:
        layer1 = ImageDraw.Draw(image)
        if CONFIG["BORDER"] is True:
            layer1.rectangle(
                ((1, 1), (498, 58)),
                width=1,
                outline=CONFIG["BORDER_INNER_COLOR"])
            layer1.rectangle(
                ((0, 0), (499, 59)),
                width=1,
                outline=CONFIG["BORDER_OUTER_COLOR"])

        medal = Image.open(CONFIG["MEDAL_IMAGE"]).convert("RGBA")
        image.paste(medal, (10, 15), medal)

        layer1.text(
            (CONFIG["AWARD_YEAR_X_POS"], CONFIG["AWARD_YEAR_Y_POS"]),
            CONFIG["AWARD_YEAR_TEXT"],
            fill=(255, 255, 255),
            font=bld)

        layer1.text(
            (CONFIG["DEVBEST_TEXT_X_POS"], CONFIG["DEVBEST_TEXT_Y_POS"]),
            CONFIG["DEVBEST_TEXT"],
            fill=(255, 255, 255),
            font=std)

        layer1.text(
            (CONFIG["USER_X_POS"], CONFIG["USER_Y_POS"]),
            CONFIG["USER"],
            fill=(255, 255, 255),
            font=bld)

        layer1.text(
            (CONFIG["AWARD_X_POS"], CONFIG["AWARD_Y_POS"]),
            CONFIG["AWARD"],
            fill=(255, 255, 255),
            font=std)

    except Exception as error:
        print(str(error))
        exit()
    finally:
        out = 'samples/banner_sample%s_.png' % random.randint(0, 1000)
        image.save(out)
        if CONFIG["OPEN_WHEN_COMPLETE"] is True:
            image.show(open(out, 'rb'))

    show_all_options()
    print("\n~ ./%s generated." % out)

if __name__ == '__main__':
    main()

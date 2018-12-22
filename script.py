import random

""" pip install Pillow """
from PIL import Image, ImageDraw, ImageFont

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

DEVBEST_TEXT_X_POS = 418
DEVBEST_TEXT_Y_POS = 31

# Assets
MEDAL_IMAGE = "assets/medal2.png"
BG_IMAGE = "assets/bg3.png"

STANDARD_TTF = "assets/Roboto-Regular.ttf"
BOLD_TTF = "assets/Roboto-Bold.ttf"


def main():
    """ Script start """
    image = Image.open(BG_IMAGE).convert("RGBA")
    std = ImageFont.truetype(STANDARD_TTF, 12)
    bld = ImageFont.truetype(BOLD_TTF, 12)
    try:
        layer1 = ImageDraw.Draw(image)
        medal = Image.open(MEDAL_IMAGE).convert("RGBA")
        image.paste(medal, (10, 15), medal)

        layer1.text(
            (AWARD_YEAR_X_POS, AWARD_YEAR_Y_POS),
            AWARD_YEAR_TEXT,
            fill=(255, 255, 255),
            font=bld)

        layer1.text(
            (DEVBEST_TEXT_X_POS, DEVBEST_TEXT_Y_POS),
            DEVBEST_TEXT,
            fill=(255, 255, 255),
            font=std)

        layer1.text((USER_X_POS, USER_Y_POS), USER, fill=(255, 255, 255), font=bld)
        layer1.text((AWARD_X_POS, AWARD_Y_POS), AWARD, fill=(255, 255, 255), font=std)
    except Exception as error:
        print(str(error))
        exit()
    finally:
        out = 'samples/banner_sample%s_.png' % random.randint(0,1000)
        image.save(out)
    print("~ ./%s generated." % out)

if __name__ == '__main__':
    main()

import argparse
from il_kino_apps.ilkino import Ilkino
from il_kino_apps.ilkino import Kiosk
from il_kino_apps.ilkino import Gift

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-gift')
    args = parser.parse_args()
    gift_left_list= args.gift.split(',')
    gift_right_list = gift_left_list.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(gift_left_list)
    right.add_gifts(gift_right_list)

    ilkino = Ilkino()
    ilkino.set_up(left, right)

    kiosk = Kiosk()
    kiosk.run(ilkino)
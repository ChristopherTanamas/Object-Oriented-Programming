from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift
from tests.ilkino_dummy import SpecialSeat

def test_gift_randomly_assigned_left():
    left_gifts = ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cutepencil']
    right_gifts = left_gifts.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(left_gifts)
    right.add_gifts(right_gifts)

    cinema = Ilkino()
    cinema.set_up(left, right)

    left_special_seats = cinema.get_left_special_seats()

    current = []

    for seat_num in left_special_seats:
        seat = cinema.get_all_seats()[seat_num - 1]
        if isinstance(seat, SpecialSeat):
            gift = seat.get_gift()
            if gift:
                current.append(True)

    expected = [True] * len(left_special_seats)

    assert current == expected, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_gift_randomly_assigned_left()
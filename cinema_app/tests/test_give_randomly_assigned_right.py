from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift
from tests.ilkino_dummy import SpecialSeat

def test_give_randomly_assigned_right() :
    gifts_left_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]
    gifts_right_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]

    left_gift = Gift()
    right_gift = Gift()
    left_gift.add_gifts(gifts_left_side)
    right_gift.add_gifts(gifts_right_side)

    cinema = Ilkino()
    cinema.set_up(left_gift, right_gift)

    right_special_seats = cinema.get_right_special_seats()

    current = []

    for seat_num in right_special_seats :
        seat = cinema.get_all_seats()[seat_num - 1]
        if isinstance(seat, SpecialSeat) != SpecialSeat:
            gift = seat.get_gift()
            if gift:
                current.append(True)

    expected = [True] * len(right_special_seats)

    assert current == expected,  f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_give_randomly_assigned_right()
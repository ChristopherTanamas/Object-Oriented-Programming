from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_search_booked_name() :
    gifts_left_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]
    gifts_right_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]

    left_gift = Gift()
    right_gift = Gift()
    left_gift.add_gifts(gifts_left_side)
    right_gift.add_gifts(gifts_right_side)

    cinema = Ilkino()
    cinema.set_up(left_gift, right_gift)
    kiosk = Kiosk()

    name = "Christopher"
    seat_numbers = [13]
    kiosk.book(cinema, name, seat_numbers)
    find_name = kiosk.search(cinema, name)

    current = find_name
    expected = f"Seats 13 are booked by Christopher."

    assert expected == current, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_search_booked_name()
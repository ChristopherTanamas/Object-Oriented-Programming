from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_book_booked_seat() :
    gifts_left_side = ["chocolate", "pack_of_candy", "teddy_bear","key_hanger", "cutepencil"]
    gifts_right_side = ["chocolate", "pack_of_candy", "teddy_bear","key_hanger", "cutepencil"]

    left_gift = Gift()
    right_gift = Gift()
    left_gift.add_gifts(gifts_left_side)
    right_gift.add_gifts(gifts_right_side)

    cinema = Ilkino()
    cinema.set_up(left_gift, right_gift)
    kiosk = Kiosk()

    name = "Jemima Alithia"
    seat_numbers = [14]
    kiosk.book(cinema, name, seat_numbers)

    name_2 = "Grace Callista"
    seat_numbers_2 = [14]
    second_book = kiosk.book(cinema, name_2, seat_numbers_2)

    current = second_book
    expected = f"Seats 14 have been booked or are not available."

    assert expected == current, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_book_booked_seat()
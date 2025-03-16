from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift
from datetime import datetime

def test_get_book_by_hour() :
    gifts_left_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]
    gifts_right_side = ["chocolate", "pack_of_candy", "teddy_bear", "key_hanger", "cutepencil"]

    left_gift = Gift()
    right_gift = Gift()
    left_gift.add_gifts(gifts_left_side)
    right_gift.add_gifts(gifts_right_side)

    cinema = Ilkino()
    cinema.set_up(left_gift, right_gift)
    kiosk = Kiosk()

    name = "Samuel ReValdo"
    seat_numbers = [12, 22]
    kiosk.book(cinema, name, seat_numbers)
    booking_hours_list = cinema.get_booked_by_hour()

    current_time = str(datetime.now().time().strftime('%H')) + ':00'

    current = booking_hours_list
    expected = {current_time:2}
    
    assert expected == current, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_get_book_by_hour()
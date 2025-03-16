from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_book_seat_with_gift():
    left_gifts = ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cutepencil']
    right_gifts = left_gifts.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(left_gifts)
    right.add_gifts(right_gifts)

    cinema = Ilkino()  
    cinema.set_up(left, right)  

    kiosk = Kiosk()

    special_seat_numbers = cinema.get_left_special_seats() + cinema.get_right_special_seats()

    current1 = kiosk.book(cinema, "Icel", [special_seat_numbers[0]])

    current2 = cinema.get_all_seats()[special_seat_numbers[0] - 1].get_gift()

    expect1 = [special_seat_numbers[0]]
    expect2 = ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cutepencil']
    assert current1 == expect1, f"Expect : {expect1}, but get Current : {current1}"
    assert current2 in expect2, f"Expect : {expect2}, but get Current : {current2}"

if __name__ == '__main__':
    test_book_seat_with_gift()
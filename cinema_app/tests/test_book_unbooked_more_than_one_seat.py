from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_book_unbooked_more_than_one_seat():
    left_gifts = ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cutepencil']
    right_gifts = left_gifts.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(left_gifts)
    right.add_gifts(right_gifts)

    ilkino = Ilkino()
    ilkino.set_up(left, right)
    kiosk = Kiosk()
    #book more than 1 seat a/n Christopher
    kiosk.book(ilkino, "Christopher", [12,17,1,3,5])
    find = kiosk.search(ilkino, "Christopher")
    expected = f"Seats 1, 3, 5, 12, 17 are booked by Christopher."

    current = find

    assert current == expected, f"Expect : {current}, but get Current : {expected}"

if __name__ == '__main__':
    test_book_unbooked_more_than_one_seat()
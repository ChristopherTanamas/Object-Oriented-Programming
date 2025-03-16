from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_book_unbooked_seat():
    gifts_odd = ["Teddy_bear", "panda", "pikachu", "candy", "iron_man"]
    gifts_even = gifts_odd.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(gifts_odd)
    right.add_gifts(gifts_even)
    cinema = Ilkino()
    cinema.set_up(left, right)
    kiosk = Kiosk()
    # akan book seat 28 atas nama stephen
    current = kiosk.book(cinema, "Nathan", [28])
    expected = [28]

    assert current == expected, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_book_unbooked_seat()
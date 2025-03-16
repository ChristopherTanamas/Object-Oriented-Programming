from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_search_unbooked_name():
    gifts_odd = ["Teddy_bear", "panda", "pikachu", "candy", "iron_man"]
    gifts_even = ["Teddy_bear", "panda", "pikachu", "candy", "iron_man"]
    
    left_gift = Gift()
    left_gift.add_gifts(gifts_odd)
    
    right_gift = Gift()
    right_gift.add_gifts(gifts_even)

    cinema = Ilkino()  # Assuming you have a constructor that accepts gifts_odd and gifts_even
    cinema.set_up(left_gift, right_gift)  # Pass instances of Gift class

    kiosk = Kiosk()

    # Book a seat for Stephen
    kiosk.book(cinema, "stephen", [28])

    # Search for an unbooked name
    current = kiosk.search(cinema, "upin")
    expected = f"No bookings found for upin."

    assert current == expected, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_search_unbooked_name()
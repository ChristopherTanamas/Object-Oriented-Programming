from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift
from tests.ilkino_dummy import Seat
from tests.ilkino_dummy import SpecialSeat

def test_get_all_distributed_gifts():
    left_gifts = ["Teddy_bear", "panda", "pikachu", "candy", "iron_man"]
    right_gifts = left_gifts.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(left_gifts)
    right.add_gifts(right_gifts)

    cinema = Ilkino()
    cinema.set_up(left, right)

    kiosk = Kiosk()

    special_seat_numbers = cinema.get_left_special_seats() + cinema.get_right_special_seats()
    normal_seat_numbers = []

    for seat in cinema.get_all_seats():
        if isinstance(seat, SpecialSeat) == False:
            normal_seat_numbers.append(seat.number)


    booked_special_seat = kiosk.book(cinema, "stephen", [special_seat_numbers[0]])
    booked_normal_seat = kiosk.book(cinema, "nathan", [normal_seat_numbers[0]])

    gifts_list = cinema.get_all_distributed_gifts()

    distributed_gifts = []
    distributed_seats = []

    for seat_num, gift in gifts_list:
        distributed_gifts.append(gift)
        distributed_seats.append(seat_num)

    valid_gifts = ["Teddy_bear", "panda", "pikachu", "candy", "iron_man"]

    all_gifts_valid = True

    for gift in distributed_gifts:
        if gift not in valid_gifts:
            all_gifts_valid = False
            break

    assert all_gifts_valid

    assert booked_special_seat == [special_seat_numbers[0]], f"Expect : {booked_special_seat}, but get Current : {[special_seat_numbers[0]]}"
    assert booked_normal_seat == [normal_seat_numbers[0]], f"Expect : {booked_normal_seat}, but get Current : {[normal_seat_numbers[0]]}"

if __name__ == '__main__':
    test_get_all_distributed_gifts()
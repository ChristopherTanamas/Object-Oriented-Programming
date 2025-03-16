from tests.ilkino_dummy import Ilkino
from tests.ilkino_dummy import Kiosk
from tests.ilkino_dummy import Gift

def test_exit_program():
    left_gifts = ['pack_of_candy', 'key_hanger', 'teddy_bear', 'chocolate', 'cutepencil']
    right_gifts = left_gifts.copy()

    left = Gift()
    right = Gift()
    left.add_gifts(left_gifts)
    right.add_gifts(right_gifts)

    ilkino = Ilkino()
    ilkino.set_up(left, right)
    kiosk = Kiosk()

    number = '4'

    current = kiosk.run(ilkino,number)
    expected = "Closing program..."
    
    assert expected == current, f"Expect : {expected}, but get Current : {current}"

if __name__ == '__main__':
    test_exit_program()
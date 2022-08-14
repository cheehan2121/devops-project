from App import keypad
def test_keypad():

    keypad.key_pressed(1)
    keypad.key_pressed(2)
    keypad.key_pressed(3)
    result=keypad.key_pressed(4)
    assert (result == True)
from App import keypad


def test_keypad1():

    keypad.key_pressed(1)
    keypad.key_pressed(2)
    keypad.key_pressed(3)
    result=keypad.key_pressed(4)
    assert (result == True)
def test_keypad2():

    keypad.key_pressed(2)
    keypad.key_pressed(3)
    keypad.key_pressed(4)
    result=keypad.key_pressed(5)
    assert (result == True)
def test_keypad3():

    keypad.key_pressed(3)
    keypad.key_pressed(4)
    keypad.key_pressed(5)
    result=keypad.key_pressed(6)
    assert (result == True)


def test_keypad4():
    keypad.key_pressed(4)
    keypad.key_pressed(5)
    keypad.key_pressed(6)
    result = keypad.key_pressed(7)
    assert (result == True)
def test_keypadfail():
    keypad.key_pressed(2)
    keypad.key_pressed(1)
    keypad.key_pressed(0)
    result = keypad.key_pressed(2)
    assert (result == "Fail")
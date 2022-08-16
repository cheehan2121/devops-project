from App import passcheck

def test_keypad1():
    arr=[1,2,3,4]
    result=passcheck.test_password1(arr)
    assert (result == True)
def test_keypad2():
    arr=[2,3,4,5]
    result=passcheck.test_password2(arr)
    assert (result == True)
def test_keypad3():
    arr=[3,4,5,6]
    result=passcheck.test_password3(arr)
    assert (result == True)
def test_keypad4():
    arr=[4,5,6,7]
    result=passcheck.test_password4(arr)
    assert (result == True)
def test_RFID():
    RFID = '1052230762465'
    result=passcheck.test_RFID(RFID)
    assert(result==True)
def test_RFID_fail():
    RFID= '123456789'
    result=passcheck.test_RFID_fail(RFID)
    assert(result==False)
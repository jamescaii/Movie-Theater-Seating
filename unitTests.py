from theaterSeating import Theater

def test_check_first_open():
    thea = Theater(5, 5)
    assert thea.check_first_open("R001", 4) == 1, "Should be 1"
    assert thea.check_first_open("R002", 6) == 0, "Should be 0"
    assert thea.check_first_open("R003", 10) == 0, "Should be 0"
    # tests that check_first_open works correctly in the base case
    thea2 = Theater(3, 5)
    thea2.check_first_open("R001", 4)
    assert thea2.seating == [["f","f","f","f","f"],["f","f","f","f","e"],["e","e","e","e","e"]]
    thea2.check_first_open("R002", 3)
    assert thea2.seating == [["f","f","f","f","f"],["f","f","f","f","e"],["f","f","f","f","f"]]
    thea2.check_first_open("R003", 1)
    assert thea2.seating == [["f","f","f","f","f"],["f","f","f","f","f"],["f","f","f","f","f"]]
    assert thea2.check_first_open("R004", 1) == 0, "Should be 0"
    assert thea2.seating == [["f","f","f","f","f"],["f","f","f","f","f"],["f","f","f","f","f"]]
    #tests that the function works correctly where there are too many people for one row
    thea3 = Theater(3, 5)
    thea3.check_first_open("R001", 6)
    assert thea3.seating == [["e","e","e","e","e"],["e","e","e","e","e"],["e","e","e","e","e"]]

def test_autofill():
    #tests when a group is too big
    thea = Theater(3, 5)
    assert thea.autofill("R001", 26) == 0, "Should be 0"
    #tests a group that is larger than one row
    thea2 = Theater(3, 5)
    assert thea2.autofill("R002", 8) == 1, "Should be 1"
    assert thea2.seating == [["f","f","f","f","f"],["f","f","f","f","f"],["f","f","f","f","f"]]
    #tests spliting a group up
    thea3 = Theater(3, 5)
    assert thea3.check_first_open("R001", 3) == 1, "Should be 1"
    assert thea3.check_first_open("R002", 1) == 1, "Should be 1"
    assert thea3.check_first_open("R003", 4) == 0, "Should be 0"
    assert thea3.seating == [["f","f","f","f","f"],["f","f","f","f","f"],["e","e","e","f","e"]]
    assert thea3.autofill("R003", 4) == 1, "Should be 1"
    assert thea3.seating == [["f","f","f","f","f"],["f","f","f","f","f"],["f","f","f","f","f"]]

if __name__ == '__main__':
    test_check_first_open()
    test_autofill()
    print("All tests passed")

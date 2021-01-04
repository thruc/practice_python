from unit_test_module import cluc

def test_add_num_and_double():
    cal = cluc.Culc()
    assert cal.add_and_doubel(1, 1) == 4



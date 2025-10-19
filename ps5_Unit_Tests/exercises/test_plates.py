from plates import is_valid



def test_lenght():
  assert is_valid("CD") == True
  assert is_valid("T") == False
  assert is_valid("CSS4445") == False

def test_start_two_letters():
  assert is_valid("1ABC") == False
  assert is_valid("CS") == True


def test_after_numeric_go_on_numeric():
  assert is_valid("CSR50O") == False
  assert is_valid("CSR500") == True

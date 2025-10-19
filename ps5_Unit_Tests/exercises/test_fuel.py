from fuel import convert, gauge




def test_convert():
  assert convert("1/2") == 50
  assert convert("3/4") == 75


def test_gauge():
  assert gauge(1) == "E"
  assert gauge(0.5) == "E"
  assert gauge(99) == "F"
  assert gauge(99.1) == "F"
  assert gauge(50) == "50%"
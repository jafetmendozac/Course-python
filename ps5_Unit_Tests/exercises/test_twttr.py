from twttr import shorten




def test_lower_word():
  assert shorten("Hello") == "Hll"



def test_upper_word():
  assert shorten("HELLO") == "HELLO"
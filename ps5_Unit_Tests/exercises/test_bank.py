from bank import value


def test_greeting_hello():
  assert value("hello bro") == "$0"

def test_greeting_with_h():
  assert value("hi bro") == "$20"

def test_greeting_without_H():
  assert value("What's up bro?") == "$100"

#Each word must be low
def test_erros():
  assert value("Hello") == "$0"
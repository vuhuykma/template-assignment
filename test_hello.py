import pytest
import hello


def test_hello():
  assert hello.greet() == "Hello"

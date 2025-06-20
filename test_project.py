import pytest
from project import starting, get_help, get_response


def test_starting():
    assert starting() == None


def test_starting():
    with pytest.raises(TypeError):
        starting(2)

def test_get_help():
    assert get_help(1) == None

def test_get_help():
    with pytest.raises(TypeError):
        get_help()


def test_get_response():
    with pytest.raises(TypeError):
        get_response(1)

# Am i being lazy here?? actually no i didnt made my function that are isnide another function or class take any argument so its not possible to check
# them atleast for now i cant i tried various thing and this is the last thing that worked evne if my project might seem like childs play
# But it took me multiple whole days so yeah , Thank you ig this was CS 50 introduction to programming with python

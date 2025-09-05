
import pytest

#@pytest.fixture(scope="session")
#def browser():
#    print("Браузер!")

#    yield

#   print("Закрываем браузер!")


@pytest.fixture()
def login_page(browser):
     print("Логин пейдж!")
     pass

@pytest.fixture()
def user():
    print("Юзер!")
    return "username", "password"


def test_login(login_page,user):
    username, password = user
    assert  username == "username"
    assert  password == "password"

def test_login1(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"



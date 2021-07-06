import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/tests/chromedriver')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('asrfwer@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zaq1')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-deck .card-title')
    pytest.driver.implicitly_wait(10)
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
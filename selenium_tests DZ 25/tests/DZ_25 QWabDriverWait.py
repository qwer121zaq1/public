from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    pytest.driver.find_element_by_id('pass').send_keys('zaq12wsx')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Проверяем, что мы оказались на странице пользователя
    assert pytest.driver.find_element_by_tag_name('h2').text == "asrfwer"


def test_all_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('asrfwer@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zaq1')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Количество питомцев в статистике
    number = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]')
    num = number.text.split()
    # Ждем загрузки таблицы питомцев
    wait = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))
    # Ищем и сохраняем имена всех питомцев
    names = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > td:nth-of-type(1)')
    # Проверяем, что отображаются все питомцы
    assert len(names) == int(num[2])


def test_photo():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('asrfwer@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zaq1')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Количество питомцев в статистике
    number = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]')
    num = number.text.split()
    # Ищем всех питомцев с фото, сораняем в список
    photo = pytest.driver.find_elements_by_css_selector('img[src*="data"]')
    # Проверяем, что хотя бы у половины питомцев есть фото
    assert len(photo) >= int(num[2]) / 2


def test_descriptions():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('asrfwer@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zaq1')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Ищем и сохраняем возраст всех питомцев
    ages = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > td:nth-of-type(3)')
    # Ищем и сохраняем породу всех питомцев
    breeds = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > td:nth-of-type(2)')
    # Ищем и сохраняем имена всех питомцев
    names = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > td:nth-of-type(1)')
    # Проверяем, что у всех питомцев есть имя, возраст и порода.
    for i in range(len(names)):
        assert ages[i].text != ''
        assert names[i].text != ''
        assert breeds[i].text != ''


def test_names():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('asrfwer@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('zaq1')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # Ищем и сохраняем имена всех питомцев
    names = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > td:nth-of-type(1)')
    # Проверяем, что у всех питомцев разные имена.
    name = [name for name in names]
    for i in range(len(names)):
        name[i] = names[i].text
    setnames = list(set(name))
    assert len(name) == len(setnames)

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/GoogleDriver/chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    pytest.driver.find_element_by_id('email').send_keys('Engibp@mail.ru')
    time.sleep(2)
    pytest.driver.find_element_by_id('pass').send_keys('Gblfnjh128500')
    time.sleep(2)
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(3)
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

for i in range(len(names)):
    assert images[i].get_attribute('src') != ''
    assert names[i].text != ''
    assert descriptions[i].text != ''
    assert ', ' in descriptions[i]
    parts = descriptions[i].text.split(", ")
    assert len(parts[0]) > 0
    assert len(parts[1]) > 0

def test_all_pets_have_diffrent_name():
    names = pytest.driver.find_element(By.XPATH, '(//tboby/tr/td[1]')
    list_names = []
    for x in names:
        unique_names = x.text
        print('klichki', unique_names)
        list_names.append(unique_names)
    print(list_names)


def test_check_photo_of_pets():
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    photo = pytest.driver.find_element(By.CSS_SELECTOR, 'th>img')
    uploded_photo = 0

    for y in range(len(photo)):
        if photo[y].get_atribute('src') != "":
            uploded_photo += 1
        else:
            uploded_photo += 0

    print("\nКоличество питомцев с фото", uploded_photo)


def test_pets_unique():
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    pets = pytest.driver.find_element(By.XPATH, '(//*[@id="all_my_pets"]/table/tbody/t)')

    for z in pets:
         pets = z.text.replace(' ', ' ')
         pets_new = pets.replace('z', ' ')
         print(pets_new)


 def test_all_pets_different_(self, setup):
        pytest.driver.find_element_by_id('email').send_keys('Engibp@mail.ru')
        time.sleep(2)
        pytest.driver.find_element_by_id('pass').send_keys('Gblfnjh128500')
        time.sleep(2)
        pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(3)
        browser_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=browser_options)
        images = driver.find_elements(By.XPATH, "//tbody/tr/th/img")
        names = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
        descriptions = driver.find_elements(By.XPATH, "//tbody/tr/td[2]" and "//tbody/tr/td[3]")
        for r in range(len(names)):
            assert images[r].get_attribute('src') != ''
            assert names[r].text != ''
            assert descriptions[r].text != ''
            assert ', ' in descriptions[r].text
            parts = descriptions[r].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
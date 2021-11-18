import time

def test_find_element_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    form_basket = browser.find_element_by_id('add_to_basket_form')
    isset_button = form_basket.find_element_by_css_selector('[type="submit"]')

    #Чтобы успеть убедиться, что язык верный
    time.sleep(3)

    #Если кнопка существует, то тест будет отмечен как PASSED
    assert isset_button
   
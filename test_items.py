def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/"
    browser.get(link)
    form_basket = browser.find_element_by_id('#add_to_basket_form')
    form_basket.find_element_by_css_selector('[type="submit"]')
    print(form_basket)
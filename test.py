from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    url = "https://www.amazon.in/s/ref=sr_pg_7?fst=as%3Aoff&rh=n%3A1350387031%2Ck%3Awatches%2Cp_89%3ATITAN%7CTitan&page=7&bbn=1350387031&keywords=watches&ie=UTF8&qid=1534497340"
    browser.visit(url)
    while browser.url != url :
        print('LoGiN PlEaSe!!!!')
    # browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    # documentation for apis
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html#api-docs
    button = browser.find_by_css('[data-asin]').first
    brands = []
    for key, value in button:
        print(key,': ',value )
        # brands.append(_.text)
    # Interact with elements
    # button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
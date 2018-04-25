from splinter import Browser
import scrape

with Browser('chrome') as browser:
    # Visit URL
    url = "https://jira.rax.io/issues/?filter=-1"
    browser.visit(url)
    while browser.url != url :
        print('LoGiN PlEaSe!!!!')
    _scrape()
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK')
    print(button)
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
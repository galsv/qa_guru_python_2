import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def configure_desktop_browser():
    """Устанавливает десктопное соотношение сторон браузера"""
    browser.config.window_width = 800
    browser.config.window_height = 600


def test_find_selene_first(configure_desktop_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_find_selene_second(configure_desktop_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('e1essssssdasdsdasd12123').press_enter()
    browser.element('[id="search"]').should_not(have.text('Selene - User-oriented Web UI browser tests in Python'))

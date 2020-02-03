from selenium import webdriver


class TestCase:

    @classmethod
    def setup_class(cls):
        print("setting up TestCase CLASS {0}".format(cls.__name__))
        cls.options = webdriver.ChromeOptions()
        cls.capabilities = {
            "build": "Python PyTest by Amir",
            "name": "Python PyTest",
            "platform": "MacOS Catalina",
            "browserName": "Chrome",
            "version": "79.0",
            "selenium_version": "3.13.0",
            "chrome.driver": "78.0"
        }
        cls.command_executor = 'http://selenium-hub:4444/wd/hub'
        cls.driver = webdriver.Remote(
            command_executor=cls.command_executor,
            desired_capabilities=cls.capabilities,
            options=cls.options
        )

    @classmethod
    def teardown_class(cls):
        print("tearing down TestCase CLASS {0}\n".format(cls.__name__))
        cls.driver.quit()

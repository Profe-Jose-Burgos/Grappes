from selenium import webdriver as wd
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

driver = wd.Edge(executable_path="./Edge_driver/msedgedriver")
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://web.whatsapp.com/")

with open('./whatsapp_session.txt', 'w') as text_file:
    text_file.write("{}\n".format(executor_url))
    text_file.write(session_id)

def new_command_execute(self, command, params=None):
    if command == "newSession":
        return {"succes":0, "value":None, "sessionId":session_id}
    else:
        return org_command_execute(self, command, params)

def create_driver_session(session_id, executor_url):
    org_command_execute = RemoteWebDriver.execute
    RemoteWebDriver.execute = new_command_execute
    new_driver = wd.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id
    RemoteWebDriver.execute = org_command_execute
    return new_driver

def start_keep_session():
    driver2 = create_driver_session(session_id, executor_url)


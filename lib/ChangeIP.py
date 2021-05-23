from selenium import webdriver
import os
import time

class ChangeIP:
    def __init__(self, password, port):
        self.password = password
        self.port = port
        self.change = '/etc/init.d/tor restart'
        self.p = 'chmod +x ChangeIP'

    def SetProfile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', self.port)

        profile.update_preferences()

        return profile

    def Change(self):
        os.popen("sudo -S %s" % (self.change), 'w').write(self.password)
        time.sleep(1)

    def GiveP(self):
        os.popen("sudo -S %s" % (self.p), 'w').write(self.password)
        time.sleep(1)
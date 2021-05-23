import getpass


class Get:
    def __init__(self):
        self.password = ''
        self.port = 0

    def GetPassword(self):
        password = getpass.getpass('Input password: ')
        self.password = password
        return self.password

    def GetPort(self):
        port = str(input('Input port(default: 9050): '))
        if port == '':
            self.port = 9050
        else:
            self.port = int(port)
        return self.port
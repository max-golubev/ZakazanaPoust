class Part:
    def __init__(self, name):
        self.name = name
        self.all_parts = [Part("propeller"), Part("engine"), Part("navigator"), Part("rudder")]

    def get_all_parts(self):
        return self.all_parts


class Technology:
    def __init__(self, name):
        self.name = name
        self.owner = None

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner

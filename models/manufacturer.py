class Manufacturer:

    def __init__(self, name, deactivated, id = None):
        self.name = name
        self.deactivated = deactivated
        self.id = id

    def mark_deactivated(self):
        self.deactivated = True
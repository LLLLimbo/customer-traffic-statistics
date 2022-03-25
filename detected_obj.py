import json


class DetectedObj:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True)

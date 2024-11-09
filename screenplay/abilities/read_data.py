import json

class ReadData:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
        return data

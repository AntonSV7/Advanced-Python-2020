from typing import Any, Dict


class Storage(object):
    def init(self, data: Dict[str, Any]):
        self._data = data
        self._reserve_data = {"potato": 100}
        self._secret_data = {"supplier": "secret word"}

    def getitem(self, search):
        if search in self._data.keys():
            array = self._data
        elif search in self._reserve_data.keys():
            array = self._reserve_data
        else:
            raise KeyError

        for key in array.keys():
            if key == search:
                print(array[key])

    def getattribute(self, name):
        if name.startswith('_secret'):
            raise AttributeError
        else:
            return self.getattribute(self, name)
from test_my_dict_common import TestMyDictCommon
from main import MyDict
class TestMyDict(TestMyDictCommon):
    def getDict(self):
        return MyDict()
                
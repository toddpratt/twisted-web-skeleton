from util.jsonresource import JsonResource

class TestList(JsonResource):
    def getJsonData(self, request):
        return {"A":["LEnt 1", "LEnt 2", "LEnt 3", "LEnt 4", "LEnt 5"]}

testList = TestList()


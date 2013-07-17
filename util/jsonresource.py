#! /usr/bin/env python

import json

from twisted.web import resource

class JsonResource(resource.Resource):
    def render(self, request):
        return json.dumps(self.getJsonData(request))


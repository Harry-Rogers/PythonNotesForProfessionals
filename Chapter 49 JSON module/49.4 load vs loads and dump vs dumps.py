# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:16:07 2020

@author: Harry
"""

import json
from io import StringIO
data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data)
load = json.loads(json_string)
print(load)

json_file = StringIO()
json.dump(data, json_file)
json_file.seek(0)
json_file_content = json_file.read()

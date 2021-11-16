import json
def store(var, filename):
    json.dump(json.dumps(var), open(filename, "w"))

def retrieve(filename):
    var = json.loads(json.load(open(filename, "r")))
    return var


import json

def find_sfsSeq(json_str):
    result = []
    data = json.loads(json_str)
    for item in data:
        if 'sfsSeq' in item:
            result.append(item)
    return result
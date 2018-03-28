import json

def write_to_json(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile,sort_keys=True, indent=4,separators=(',',':'), ensure_ascii=False)

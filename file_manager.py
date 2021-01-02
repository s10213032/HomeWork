import json

def read_json(filename,default_data):
    try:
        with open(filename,"r",encoding="utf8") as file:
            f = json.load(file)
            return f
    except:
        return default_data

def write_json(filename,data):
    
    with open(filename,'w',encoding="utf8") as file:
        json.dump(data,file)
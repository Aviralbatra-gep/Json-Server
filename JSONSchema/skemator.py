a = {
    "productId": 1,
    "productName": "An ice sculpture",
    "price": 12.50,
    "tags": ["cold", "ice"],
    "dimensions": {
        "length": 7.0,
        "width": 12.0,
        "height": 9.5
    },
    "warehouseLocation": {
        "latitude": -78.75,
        "longitude": 20.4
    }
}


b = {
    "StudentDetails": [{
        "name": "John",
        "marks": [{
            "maths": [{
                "statists": "70",
                "algebra": "80"
            }],
            "English": [{
                "grammar": "90",
                "other": [{
                    "speech": "80%"
                }]
            }]
        }]
    },
        {
        "name": "Teena",
        "marks": [{}]
    },
        {
        "name": "Roy",
        "marks": [{
            "English": [{
                "grammar": "90"
            }]
        }]
    }]
}

sc = {}

sc["$id"] = "http://json-schema.org"
sc["$schema"] = "https://json-schema.org/draft/2020-12/schema"
sc["title"] = "Schema"

required = ['productId', 'productName', 'price', 'tags', 'dimensions', 'length', 'width', 'height', 'warehouseLocation', 'latitude', 'longitude']


nodes = []

def typeof(i):
    s = ""
    if type(i) == dict:
        s = "object"
    elif type(i) == list:
        s = "array"
    elif type(i) == int:
        s = "integer"
    elif type(i) == float:
        s = "number"
    elif type(i) == str:
        s = "string"
    
    return s

def generate(node,sc):
    sc["type"] = typeof(node)
    if type(node) == dict:
        t = {}
        for key,value in node.items():
            nodes.append(key)
            d = {}
            if type(value) not in [list,dict]:
                d["type"] = typeof(value)
            elif type(value) == dict:
                generate(value,d)
            elif type(value) == list:
                generate(value,d)
                
            t[key] = d
    elif type(node) == list:
        t = []
        for i in range(len(node)):
            d = {}
            if type(node[i]) not in [list,dict]:
                d["type"] = typeof(node[i])
            elif type(node[i]) == dict:
                nodes.append(node[i])
                generate(node[i],d)
            elif type(node[i]) == list:
                nodes.append(node[i])
                generate(node[i],d)
                
            t.append(d)
    if type(node) == dict:
        sc["properties"] = t
    elif type(node) == list:
        sc["items"] = t
    
    
            
            
# generate(a,sc)
# print(sc)
# print(nodes)

generate(b,sc)
print(sc)
print(nodes)

def change(sc,required):
    if type(sc) == dict:
        a = []
        for key, value in sc.items():
            if key == "properties":
                change(value,required)
            else:
                if key in required:
                    a.append(key)   
            sc["required"] = a
    elif type(sc) == list 
            
        
        
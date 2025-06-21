import json

input_filename = "resources/faves.json"
output_filename = "resources/out_faves.json"

def read_json(file=input_filename):
    with open(file, 'r') as f:
        data = json.load(f)  #python obj
        return data

def write_to_json(data, file=output_filename, indent=4):
    with open(file, 'w') as f:
        json.dump(data, f, indent=indent)

mydata = read_json()
print(f"Fave number => {mydata['faves'].get('number')}")
print(f"Fave song is '{mydata['faves'].get('song')}' and your fave movie is '{mydata['faves'].get('movie')}'")
print(f"Fave drink => {mydata['faves']['foods'].get('drinks')}")

foods = {k:v for (k,v) in mydata['faves']['foods'].items()}
print(f"Total food items => {len(foods)}")

print(mydata['faves']['foods'].get('snacks', "Not listed!"))

mydata['faves']['number']=12
print(f"Fave number => {mydata['faves'].get('number')}")

write_to_json(mydata)









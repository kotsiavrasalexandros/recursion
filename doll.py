doll_one = {
    "size": 5, 
    "inner_doll": None
}
# Expected output: 5
doll_two = {
    "size": 12, 
    "inner_doll": {
        "size": 7, 
        "inner_doll": None
    }
}
# Expected output: 7
doll_three = {
    "size": 20, 
    "inner_doll": {
        "size": 15, 
        "inner_doll": {
            "size": 10, 
            "inner_doll": {
                "size": 3, 
                "inner_doll": None
            }
        }
    }
}
# Expected output: 3

def open_doll(x):
    if x['inner_doll'] != None:
        return open_doll(x['inner_doll'])
    else:
        return x['size']

print(open_doll(doll_three))
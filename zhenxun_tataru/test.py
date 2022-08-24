item_dict = {}
with open("tools/item_dict.json", "r",encoding = "UTF-8") as f_r:
    for line in f_r.readlines():
        item_dict = eval(line)
print(line)
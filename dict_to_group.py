import json

loaded = 1
temp_dict = {}
content = []
group = 1
done_group = []
with open("output_dict.json", encoding="UTF-8") as file_object:
    done = json.load(file_object)
for dict_item in done:
    if loaded == 1:
        temp_dict["group"] = group
        temp = dict_item["1"]
        content.append(dict_item)
        loaded = loaded + 1
    else:
        if temp in dict_item["1"]:
            temp = dict_item["1"]
            content.append(dict_item)
            loaded = loaded + 1
        else:
            temp_dict["content"] = content
            done_group.append(temp_dict)
            temp_dict = {}
            content = []
            loaded = 1
            group = group + 1
            temp_dict["group"] = group
            temp = dict_item["1"]
            content.append(dict_item)
            loaded = loaded + 1
print(done_group)
with open("output_group.json", "w", encoding="UTF-8") as outfile:
    json.dump(done_group, outfile, ensure_ascii=False)

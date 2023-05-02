import json

store_state = 0
srt_number = 1
done = []
temp_dict ={}
read_line = 1

with open("input.srt",encoding="UTF-8") as file_object:
    for line in file_object:
        line = line.strip()
        if line == "":
            store_state = 0
            srt_number = srt_number + 1
            done.append(temp_dict)
            temp_dict = {}
            read_line = 1
        if line == str(srt_number):
            store_state = 1
            #read_line = read_line + 1
        else:
            if store_state == 1:
                temp_dict["srt_number"] = srt_number
                if read_line == 1:
                    temp_dict["time"] = line
                    read_line = read_line + 1
                else:
                    temp_dict[str(read_line-1)] = line
                    read_line = read_line + 1
add_dict = {"srt_number":0,"time":"0","1":"temp_dict"}
add_dict["srt_number"] = srt_number
done.append(add_dict)
print(done)
with open("output_dict.json", "w",encoding="UTF-8") as outfile:
    json.dump(done, outfile, ensure_ascii=False)
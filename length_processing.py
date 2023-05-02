import json

char_list = [chr(i) for i in range(33, 127)]
char_list.append(" ")
#char_list.append('　')

done = []


def length_counting(input_count):
    half_length = 0
    if isinstance(input_count, str):
        for a in input_count:
            if a in char_list:
                half_length = half_length + 1
        output = len(input_count) * 2 - half_length
        return output
    else:
        return 0


def all_length(input_dict):
    if isinstance(input_dict, dict):
        count = 1
        length = 0
        while count <= len(input_dict) - 2:
            a = length_counting(input_dict[str(count)])
            if a >= length:
                length = a
                count = count + 1
            elif a < length:
                count = count + 1
        return length
    else:
        return 0


def srt_filling(input_srt, srt_length):
    if isinstance(input_srt, str) == True and isinstance(srt_length, int) == True:
        while length_counting(input_srt) < srt_length - 1:
            input_srt = input_srt + "　"
        input_srt = input_srt + ""
        return input_srt
    else:
        return 0


with open("output_group.json", encoding="UTF-8") as file_object:
    done_group = json.load(file_object)
for temp_dict in done_group:
    temp_dict_content = temp_dict["content"]  # _content:list
    temp_dict_content_a = temp_dict_content[0]
    length = all_length(temp_dict["content"][-1])
    print(str(length))
    # print(temp_dict_content)
    for srt_dict in temp_dict_content:
        # print(srt_dict)
        # print(str(len(srt_dict)))
        processed = 1
        while processed <= len(srt_dict) - 2:
            print(srt_filling(input_srt=srt_dict[str(processed)], srt_length=length))
            srt_dict[str(processed)] = srt_filling(input_srt=srt_dict[str(processed)], srt_length=length)
            processed = processed + 1
        done.append(srt_dict)
print(done)
with open("output_processed.json", "w", encoding="UTF-8") as outfile:
    json.dump(done, outfile, ensure_ascii=False)

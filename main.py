import json
from colorama import Fore, Back, init
import time
import os

store_state = 0
srt_number = 1
done = []
temp_dict = {}
read_line = 1

init(autoreset=False)
os.system("color 0f")
os.system("chcp 65001")
os.system("cls")
os.system("title SRTformat tool v0.1")


def length_counting(input_count):
	half_length = 0
	if isinstance(input_count, str):
		for a in input_count:
			if a in char_list:
				half_length = half_length + 1
		output = len(input_count) * 2 - half_length
		print(Back.BLUE + "Function(length_counting)", end="")
		print(Back.CYAN + "input_count=", end="")
		print(Back.MAGENTA + input_count, end="")
		print(Back.CYAN + "output=", end="")
		print(Back.RESET + str(output))
		time.sleep(0.02)
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
		print(Back.BLUE + "Function(all_length)", end="")
		print(Back.CYAN + "input_dict=", end="")
		print(Back.MAGENTA + str(input_dict), end="")
		print(Back.CYAN + "length=", end="")
		print(Back.RESET + str(length))
		time.sleep(0.02)
		return length
	else:
		print(Back.RED + "ERROR:INPUT NOT A DICT.RETURN 0")
		return 0


def srt_filling(input_srt, srt_length):
	if isinstance(input_srt, str) == True and isinstance(srt_length, int) == True:
		while length_counting(input_srt) < srt_length - 1:
			input_srt = input_srt + " "
		# input_srt = input_srt + "."
		print(Back.BLUE + "Function(srt_filling)", end="")
		print(Back.CYAN + "input_srt=", end="")
		print(Back.MAGENTA + input_srt, end="")
		print(Back.CYAN + "srt_length=", end="")
		print(Back.MAGENTA + str(srt_length), end="")
		print(Back.CYAN + "output=", end="")
		print(Back.RESET + input_srt)
		time.sleep(0.02)
		return input_srt
	else:
		print(Back.RED + "ERROR:INPUT DATA ERROR.RETURN 0")
		return 0


srt_file_path = input("要求输入要文件的SRT文件的路径\n注意：您需要使用绝对路径，最好符合python的路径规范。\n请输入：")
try:
	with open(srt_file_path, encoding="UTF-8") as f:
		inputsrt_original = f.read()
	inputsrt_original = inputsrt_original + "\n\n"
	done_path = srt_file_path + "_processed.srt"
	output_path = srt_file_path + "_output.srt"
	with open(done_path, "w", encoding="UTF-8") as f:
		f.write(inputsrt_original)
except FileNotFoundError:
	print(Back.RED + "您输入的似乎不是一个有效的路径，请重试！")
	print(Back.BLACK + "")
	os.system("pause")
	exit()

os.system("title SRTformat tool v0.1  1/4 SRT to dict")

with open(done_path, encoding="UTF-8") as file_object:
	for line in file_object:
		line = line.strip()
		line.replace("\u3000","  ")
		line.replace('\u0200b',"")#去除零宽字符
		if line == "":
			store_state = 0
			srt_number = srt_number + 1
			done.append(temp_dict)
			print(Back.GREEN + "Done  1/4  SRT -> dict:", end="")
			print(Back.RESET + str(temp_dict))
			time.sleep(0.1)
			temp_dict = {}
			read_line = 1
		if line == str(srt_number):
			store_state = 1
		# read_line = read_line + 1
		else:
			if store_state == 1:
				temp_dict["srt_number"] = srt_number
				if read_line == 1:
					temp_dict["time"] = line
					read_line = read_line + 1
				else:
					temp_dict[str(read_line - 1)] = line
					read_line = read_line + 1
add_dict = {"srt_number": 0, "time": "0", "1": "temp_dict"}
add_dict["srt_number"] = srt_number
done.append(add_dict)

time.sleep(1)
os.system("title SRTformat tool v0.1  2/4 dict to group")

loaded = 1
temp_dict = {}
content = []
group = 1
done_group = []
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
			print(Back.GREEN + "Done  2/4  dict -> group  group_number=" + str(group) + ":", end="")
			print(Back.RESET + str(temp_dict))
			time.sleep(0.1)
			temp_dict = {}
			content = []
			loaded = 1
			group = group + 1
			temp_dict["group"] = group
			temp = dict_item["1"]
			content.append(dict_item)
			loaded = loaded + 1

		
time.sleep(1)
os.system("title SRTformat tool v0.1  3/4 length processing")

char_list = [chr(i) for i in range(33, 127)]
char_list.append(" ")
char_list.append("「")
char_list.append("…")

done = []

for temp_dict in done_group:
	temp_dict_content = temp_dict["content"]  # _content:list
	temp_dict_content_a = temp_dict_content[0]
	length = all_length(temp_dict["content"][-1])
	# print(str(length))
	# print(temp_dict_content)
	for srt_dict in temp_dict_content:
		# print(srt_dict)
		# print(str(len(srt_dict)))
		processed = 1
		while processed <= len(srt_dict) - 2:
			srt_dict[str(processed)] = srt_filling(input_srt=srt_dict[str(processed)], srt_length=length + 2)
			srt_dict[str(processed)] = srt_dict[str(processed)] + "."
			processed = processed + 1
		done.append(srt_dict)
		print(Back.GREEN + "Done  3/4  dict -> group:", end="")
		print(Back.RESET + str(srt_dict))
		time.sleep(0.1)

time.sleep(1)
os.system("title SRTformat tool v0.1  4/4 dict to SRT")
srt = ""

for a in done:
	srt = srt + str(a["srt_number"]) + "\n" + a["time"] + "\n"
	line = 1
	while line <= len(a) - 2:
		srt = srt + a[str(line)] + "\n"
		line = line + 1
		print(Back.GREEN + "Done  4/4  dict -> SRT:", end="")
		print(Back.RESET + a[str(line - 1)])
		time.sleep(0.1)
	srt = srt + "\n"

with open(output_path, "w", encoding="UTF-8") as file_object:
	file_object.write(srt)

print(Back.BLACK + "\n\n")
print(Back.GREEN + "处理完成！输出文件保存在" + output_path,end="")
print(Back.BLACK + "\n")
os.system("pause")

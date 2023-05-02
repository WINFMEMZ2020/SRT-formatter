import json

with open("output_processed.json", encoding="UTF-8") as file_object:
    done = json.load(file_object)
srt = ""

for a in done:
    srt = srt + str(a["srt_number"]) + "\n" + a["time"] + "\n"
    line = 1
    while line <= len(a) -2:
        srt = srt + a[str(line)] + "\n"
        line = line + 1
    srt = srt + "\n"
print(srt)
with open("output.srt","w",encoding="UTF-8") as file_object:
    file_object.write(srt)
# SRTformatter
This is SRTformatter
# 这是什么？
这是一个可以将srt字幕格式化的工具。
<br>
由于大部分网站的CC字幕默认是将字幕底部居中的，所以像这样的字幕：
```
1
00:00:01,000 --> 00:00:02,000
This is

2
00:00:02,145 --> 00:00:03,123
This is a test text.
```
这样写SRT，字幕内容会随着视频一起逐渐出现，看起来很酷！
<br>
但是视频平台显示字幕会底部居中显示，导致字幕中心不停移动，这样反而不大好看（？）
<br>
这个脚本可以再同一组字幕内（如上述字幕1、2为同一组）将未显示完全的字幕（如上述字幕1）用全角空格填充（这样不会被平台识别成空格去掉）。

# 怎么使用？
1.将脚本与字幕放在同一目录下，将字幕命名为"input.srt"
<br>
2.运行srt_to_dict.py，如果运行成功，会生成output_dict.json
<br>
3.运行dict_to_group.py，如果运行成功，会生成output_group.json
<br>
4.运行length_processing.py，如果运行成功，会生成output_processed.json
<br>
5.运行dict_to_srt.py，如果运行成功，会生成output.srt
<br>
至此处理完成！

# 已知问题
1.输入的input.srt最后一行必须是空格，如果最后一行有内容会导致处理完的字幕的最后一行缺失！

# 没有一键处理的脚本吗？
已经在写了

# 还有其它bug？
请在issues提出，本项目也欢迎大家fork！

Edit:2023.05.02

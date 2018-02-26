#!/usr/bin/python3

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "w")

# 写入文件，覆盖原有的内容
f.write( "我在学习python语言。\n" )

# 关闭打开的文件
f.close()

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "a")

# 写入文件，在原有的内容上追加
f.write( "\n这是追加的内容。\n" )

# 关闭打开的文件
f.close()

"""
我在学习python语言。

这是追加的内容。
"""

# -------------------------------------

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "r+")

# 从开头写入文件，覆盖现有的内容，后边的内容不变
f.write( "我在学习python语言2。\n" )

# 关闭打开的文件
f.close()


"""
我在学习python语言2。

这是追加的内容。
"""

# -------------------------------------

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "w+")

# 从开头写入文件，覆盖所有的内容
f.write( "我在学习python语言3。\n" )

# 关闭打开的文件
f.close()


"""
我在学习python语言3。
"""

# -------------------------------------

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "r")

# 读入文件，覆盖所有的内容
print(f.read())

# 关闭打开的文件
f.close()

"""
我在学习python语言3。

[Finished in 0.2s]
"""

# -------------------------------------

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "r",encoding= 'utf-8')

# 读入一行
print(f.readline())

print(f.readline(2))

# 关闭打开的文件
f.close()

"""
我在学习python。

你在
[Finished in 0.2s]
"""

# -------------------------------------

# 打开一个文件
f = open("C:\\Users\\geek\\Desktop\\python.txt", "r",encoding= 'utf-8')

# 返回所有行
print(f.readlines())

# 关闭打开的文件
f.close()

"""
['我在学习python。\n', '你在学什么？']
[Finished in 0.2s]
"""

# -------------------------------------
"""
总结：
	
	1.凡是带有 + 的均可用于读和写，没有 + 的只有一个功能，非读即写。

	2.凡是带有 b 的都是以二进制的格式。

	3.w 是覆盖写入， a 是追加写入。
"""


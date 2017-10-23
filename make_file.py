#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random

def genSizeFile(fileName, fileSize):
	#file path
	filePath=fileName+".txt"
	
	# 生成固定大小的文件
	# date size
	ds=0
	with open(filePath, "w", encoding="utf8") as f:
		while ds<fileSize:
			f.write(str(random.randint(0,10)))
			ds=os.path.getsize(filePath)
	# print(os.path.getsize(filePath))

# start here.
genSizeFile("rsa_origin_file",(16*1024)+7)
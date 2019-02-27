Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> TempStr = input("请输入带有符号的温度值：")
请输入带有符号的温度值：82f
>>> if TempStr[-1] in ['F','f']:
	C = (eval(TempStr[0:-1])-32)/1.8
	print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
	print("输入格式错误")
	

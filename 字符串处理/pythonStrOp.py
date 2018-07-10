import os

# 源字符串 是否包含 操作字符串 index找不到抛出异常 find找不到返回-1
def ContainStr(originStr,opStr):
    result = originStr.index(opStr)
    result = originStr.find(opStr)
    return result

# 求 操作字符串 长度
def StrLen(opStr):
    return len(opStr)

#
def upOrlowStr(opStr):
    return opStr.upper()
    #return opStr.lower()

#返回 子串 在源串中出现的次数
originStr.count(childStr)

#把迭代对象里的字符串起来 中间用onestr分隔
onestr.join(strList)

#去掉左边的指定chars
originStr.lstrip("0")
#去掉右边指定的chars
originStr.rstrip("0")
#去掉空格字符ch
originStr.strip('ch')

#替代 把字符串中 A 替换成 B 共n个
originStr.replace(A,B,n)

#左侧以字符0进行填充
originStr.zfill()

#分割，成n端
originStr.split(",",n)
# 给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。
#
# 例如a="cagy", b=3,
#
# 则输出 ：fdjb
a = "nica"
b = 26

# 创建一个映射字典
dict = {}
for k in range(1,27):
    for char in "abcdefghijklmnopqrstuvwxyz"[k-1]:
        dict[k] = char
        break

L = []
for char in a:
    for i in dict:
        if dict[i] == char:
            L.append(dict[(i+b)%26])
            break
print("".join(L))

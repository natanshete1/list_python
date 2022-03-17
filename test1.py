
# ls1 = [1,4,7]
# ls2 = [2,5,8]
# ls3 = [3,6,9]
# ls4 = [ls1,ls2,ls3]
# for i in range(len(ls4)):
#     for j in range(len(ls4[i])):
#         print(ls4[i][j],end='\t')
#     print()
#
# ls = []
# for i in range(101):
#     ls.append(i)
# print(ls)

# ls = []
# for i in range(10):
#     name = (input("enter nume :"))
#     ls.append(name)
# print(ls)
#
# ls = []
# for i in range(10):
#     name = input("enter name")
#     ls.append(name)
# for i in ls:
#     print(i)

# ls = ["natan","maor","david","moshe"]
# newls=[]
# for i in ls:
#     if "a" in i :
#         newls.append(i)
# print(newls)

# t1 = (1,2,3)
# t2 = ("natan","moshe","holle")
# print(t1,t2)
# print(t1[2:4])
# print(t1[2],t2[2])
# ls = [t1,t2]
# ls.append("3")
# ls.insert(0,"david")
# print(ls)

# for i in range(5):
#     i = ("i love python")
#     print(i)
#

# ls = []
# for i in range(10):
#     number = int(input("enter a number:\n"))
#     ls.append(number)
# print(ls)
# number = ls
# x = sorted(number)
# print(x)
#
ls = []
for i in range(11):
    num = input("enter a number:")
    ls.append(int(num))
print(sum(ls))
a_10 = 0
b_10 = 0
for j in ls:
    print(j/11)
if j >10:
    a_10 +=1
else:
    b_10 +=1
    if j %2 ==0:
        print(max(j)+"is the max number")

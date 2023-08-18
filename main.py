# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
X=[1,2,1,2,5]
c=0
il=[]
jl=[]
for i in range(5):
    il.append(i)
    for j in range(1,5-i):
        jl.append(j)
        if X[i]==X[-j]:
            c=c+1


print(c)
print(il)
print(jl)

def count(string):
    dic={}
    loco={}
    index = 0

    for k in string:
        if k in dic:
            dic[k] += 1
            loco[k].append(index)
        else:
            dic[k]=1
            loco[k]=[index]
        index += 1


    lst = list(dic.keys())
    lst = sorted(lst)

    for i in lst:
        print(i,": ", dic[i])

def factor(whatever):
    nums=[]
    whatever = int(whatever)
    for i in range(1, whatever+1):
        if whatever % i ==0:
            nums.append(i)
    print(nums)

count(input("What is your string?"))
factor(input("What is your number?"))

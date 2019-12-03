import random
numbers=[]
corrects=[]
notnumbers=[]
n=int(input(""))
for i in range(0,n):
    digits,correct=input("").split(" ")
    digits=[int(x) for x in str(digits)]
    corrects.append(int(correct))
    numbers.append(digits)
    if(int(correct)==0):
        notnumbers.append(digits)
#arr= np.array(numbers,dtype='int64')
print(numbers)
d=[]
for i in range(0,16):
    d.append([0,1,2,3,4,5,6,7,8,9])
nd=[[notnumbers[j][i] for j in range(len(notnumbers))] for i in range(len(notnumbers[0]))]

newnumbers=[]
for i in range(0,16):
    #print(i+1)
    fresh=[x for x in d[i] if x not in nd[i]]
    #print(fresh)
    newnumbers.append(fresh)
d=newnumbers
#print(d)
def check(gn):
    #print("---",gn)
    #time.sleep(3)
    gn=[int(x) for x in str(gn)] 
    for i in range(0,n):
        correct=0
        for j in range(0,16):
            #print(gn[j],numbers[i][j])
            if(gn[j]==numbers[i][j]):
                correct=correct+1;
        #print("------",correct,corrects[i])
        if(correct!=corrects[i]):
            return 0
    return 1
def randomnum():
    number=""
    for i in range(0,16):
        number=number+str(random.choice(d[i]))
        #print(i,number)
    return number
gnumber=randomnum()
print("begin")
while(check(gnumber)!=1):
    gnumber=randomnum()
print(gnumber)

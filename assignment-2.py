#第一題作業
def calculate(min,max):
    n = min
    sum = 0
    while n<=max:
        sum = sum + n
        n+=1
    print(sum)
calculate(1,3)
calculate(4,8)

#第二題作業
def avg(data):
    sum=0
    for i in range(0,3,1):
        sum=sum+data["employees"][i]["salary"]
    y=sum/data["count"]
    print(y)
avg({"count":3,
    "employees":[
        {"name":"John","salary":30000
        },
        {"name":"Bob","salary":60000
        },{"name":"Jenny","salary":50000
        }
    ]             
})
# print(data["employees"][0]["salary"])
#第三題作業
def maxProduct(nums):
    maxNumber=0
    for i in range(0,4,1):
        for j in range(i+1,4,1):
            if nums[i]*nums[j]>maxNumber:
                maxNumber=nums[i]*nums[j]
    print(maxNumber)
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

#第四題作業
def twoSum(nums, target):
    for i in range(0,len(nums),1):
        for j in range(0,len(nums),1):
            if nums[i]+nums[j]==target:
                return[i,j]

result=twoSum([2, 11, 7, 15], 9)
print(result)
#Sandy option1 S3C3
#this is the solution of codingbat of recursion 2
def groupSum(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False
    return groupSum(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)
print(groupSum(0,[2,4,8],10))

def groupSum6(start,nums,target):
    if start==len(nums):
        return (target==0)
    if nums[start]==6:
        return groupSum6(start+1,nums,target-6)
    return groupSum6(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)
print (groupSum6(0, [5, 6, 2], 8))


def groupNoAdj(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False
    return groupNoAdj(start+2,nums,target-nums[start]) or groupNoAdj(start+2,nums,target)
print (groupNoAdj(0, [2, 5, 10, 4], 12))

def groupSum5(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False
    if nums[start]%5==0:
        if nums[start+1]!=1:
            return groupSum5(start+1,nums,target-nums[start])
        return groupSum5(start+2,nums,target-nums[start])
    return groupSum5(start+1,nums,target-nums[start]) or groupSum5(start+1,nums,target)
print(groupSum5(0, [20, 1, 10, 4], 31 ))

def groupSumClump(start,nums,target):
    if target==0:
        return True
    if start==len(nums):
        return False
    n=0
    for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            n=n+nums[i]
            return groupSumClump(start+1,nums,target-n*nums[start])
    return groupSum(start+1,nums,target-nums[start]) or groupSum(start+1,nums,target)
print(groupSumClump(0,[1,2,2,2,2,4],3))

def sum(start,nums,sum1,sum2):
    if start>=len(nums):
        return (sum1==sum2)
    return sum(start+1,nums,sum1+nums[start],sum2) or sum(start+1,nums,sum1,sum2+nums[start])
def splitArray(nums):
    return sum(0,nums,0,0)
print(splitArray([1,2, 3,10,10,1,1]))

def sum(start,nums,sum1,sum2):
    if start>=len(nums):
        return (sum1%10==0) and (sum2%2==1)
    return sum(start+1,nums,sum1+nums[start],sum2) or sum(start+1,nums,sum1,sum2+nums[start])
def splitOdd10(nums):
    return sum(0,nums,0,0)
print(splitOdd10([5, 5, 6 ]))

def sum(start,nums,sum1,sum2):
    if start>=len(nums):
        return (sum1==sum2)
    if nums[start]%5==0:
        return sum(start+1,nums,sum1+nums[start],sum2)
    if nums[start]%3==0 and nums[start]%5!=0  :
        return sum(start+1,nums,sum1,sum2+nums[start])
    return sum(start+1,nums,sum1+nums[start],sum2) or sum(start+1,nums,sum1,sum2+nums[start])

def split53(nums):
    return sum(0,nums,0,0)
print(split53([30,15,5,40]))

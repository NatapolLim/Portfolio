def threeSum( nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans=set()
    for i in range(len(nums)):
        target = 0-nums[i]
        l = i+1
        r=len(nums)-1
        while l<r:
            if nums[l] +nums[r] == target:
                ans.add((nums[i],nums[l],nums[r]))
                l+=1
                r-=1
            elif nums[l]+nums[r] > target:
                r-=1
            else:
                l+=1
    return ans
threeSum([-1,0,1,2,-1,-4])
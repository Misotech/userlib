import re

def clean_phone(inp):
    nums = "".join(re.compile(r'[\d]+').findall(inp))
    if len(nums) == 11 and nums[0] == '8':
        nums = '7' + nums[1:]
    return nums

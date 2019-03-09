import re

def clean_phone(inp):
    nums = "".join(re.compile(r'[\d]+').findall(inp))
    if len(nums) == 11 and nums[0] == '8':
        nums = '7' + nums[1:]
    if len(nums) == 10 and nums[0] == '9':
        nums = '7' + nums
    return nums


def clean_telegram(inp):
    username = "".join(re.compile(r'[a-zA-Z\d_]+').findall(inp))
    if username.isdigit():
        username = clean_phone(username)
    return username


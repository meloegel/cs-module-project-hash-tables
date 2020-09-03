"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def combinations(nums):
    nums = list(nums)
    add = {}
    subtract = {}
    answers = {}
    keyA = None
    keyB = None
    
    for x in nums:
        ans = f(x)
        answers[x] = ans
    for i in range(len(nums)):
        for y in range(len(nums)):
            addVal = f(nums[i]) + f(nums[y])
            addKey = (nums[i], nums[y])
            add[addKey] = addVal
            subtractVal = f(nums[i]) - f(nums[y])
            subtractKey = (nums[i], nums[y])
            subtract[subtractKey] = subtractVal
    for (keyA, ValA) in add.items():
        for (keyB, ValB) in subtract.items():
            if add[keyA] is subtract[keyB]:
                print(f'f({keyA[0]}) + f({keyA[1]}) = f({keyB[0]}) - f({keyB[1]}) | {answers[keyA[0]]} + {answers[keyA[1]]} | {add[keyA]} = {subtract[keyB]}')

combinations(q)
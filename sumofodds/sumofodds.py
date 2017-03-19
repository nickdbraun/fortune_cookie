def sum_of_initial_odds(nums):
    # your code here
    a= 0
    for value in nums:
        if value % 2 != 0:
            a += value
        else:
            return a
    return a

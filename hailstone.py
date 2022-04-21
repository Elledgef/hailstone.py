# Author: Faith Elledge
# Grithub username: Elledgef
# Date: 4/20

def hailstone(num):
    """Divide even integers by 2 and odd ones multiply by 3 then add 1"""
# count starts at zero
count = 0
while num!= 1:
    if num% 2 == 0:
        num//= 2
    else:
        num = 3*num+ 1
        count += 1
    break

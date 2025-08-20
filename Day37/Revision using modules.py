# Revising a random problem using Python:

from random import choice

a = [
    485,
    977,
    1295,
    1,
    217,
    283,
    344,
    1089,
    27,
    88,
    1672,
    349,
    387,
    9,
    412,
    1281,
    1365,
    1523,
    2520,
    1431,
    231,
    1137,
    50,
    26,
    1480,
    1108,
    242,
    80,
    53,
    905,
    121,
    122,
    1929,
    125,
    54,
    3,
    1876,
    167,
    49,
    904,
    169,
    14,
    912,
    80,
    169,
    75,
    88,
    35,
    704,
    33,
    34,
    852,
    69,
    875,
    74,
]
print(choice(a))

# To check if I wrote all problems that I solved I did:
print(len(a))
# where, a is a list of all the problem numbers done till now.

# But the output was 55, meaning there are problems that I solved more than once
# and added them more than once and then I removed the repetitions by searching
# them, not manually but by making a frequency hashmap and hence
# I was able to implement Python again for my work.

freq = {}
for num in a:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1

for num in freq.keys():
    if freq[num] > 1:
        print("This problem is solved multiple times:", num)

# I added the repititions again to show the working of this
# frequency hashmap tho.


# Output from the choice function: 1929
# Revising problem 1929 (Concatenation of Array):
# Trying a different approach from the previous ones:
def getConcatenation(nums):
    n = len(nums)
    ans = [0] * (n * 2)
    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans


def solve():
    nums = [1, 2, 1]
    print(getConcatenation(nums))


if __name__ == "__main__":
    solve()

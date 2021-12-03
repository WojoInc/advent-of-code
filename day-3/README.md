# Day 3 Challenge notes

Notes for Day 3 challenges so I can remember how I solved it

## Part 1

**Spoilers here**

**Do not read if you haven't solved part 1 yet!**


Know that for this part, you need not keep track of the 1s and 0s.
You can simply sum up each column. Then to get most frequent bit,
check if the sum for each column is greater or less than half the total
number of input lines. 

This works because we're talking base2 instead of base10.

Less = MFB is 0

Greater = MFB is 1

Gamma is then the decimal equivalent of the binary string of MFBs

Epsilon is then found by flipping each of the MFBs used for Gamma, and again converting to decimal.

The flip is easy to do via xor, saves needing if statements

## Part 2

Part 2 requires tracking inputs to some degree, but is moreso about doing a binary search on the array.

Based on each digit, in order, split array into high and low (1s and 0s), and based on which subsequent array is bigger, use it as the input for the next round.

This part is much easier to do recursively.
# Day 7

**As always, spoilers**

# Part 1
Goal is to find the point which has the shortest distance to all other points(subs).

Instead of comparing each combination, instead, create an array, 0 -> highest input value.

Then, read in all inputs. For each input:
Calculate its distance to each index in the array above, add this number to the sum at this index. Check if value at index is lower than current lowest value. If so, update lowest value, and keep track of the current index.
Repeat for remaining inputs.

At the end, index indicates the position to move to, and value indicates the amount of fuel needed.

# Part 2

Same as above, however, the equation changes. No longer the distance between two points, but instead, the summation of the range `[0, abs(a-b)]`

This takes a bit longer to run. Still seems to be under the 15 second mark that AoC indicates for these problems. Might still be a more efficient way, and python is also very slow for this kind of problem.

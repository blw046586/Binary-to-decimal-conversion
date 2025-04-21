# Binary-to-decimal-conversion
A binary number contains digits of 0 and 1 called bits. Each bit's weight is an increasing power of 2, starting from the leftmost bit.

Ex: 110 is

1*22 + 1*21 + 0*20

which equals…

1*4 + 1*2 + 0*1

which then equals…

4 + 2 + 0 = 6

Given an input of an 8-bit binary number as 1's and 0's separated by spaces, compute and output the decimal equivalent.

Ex: If the input for 00011111 is:

0
0
0
1
1
1
1
1
the output is

31
Hints:

Store the bits in reverse, so that the rightmost bit is in element 0.

Write a for loop to read the input bits into a list. Then write a second for loop to compute the decimal equivalent.

To compute the decimal equivalent, loop through the elements, multiplying each by a weight, and adding to a sum.

Use a variable to hold the weight. Start the weight at 1, and then multiply the weight by 2 at the end of each iteration.

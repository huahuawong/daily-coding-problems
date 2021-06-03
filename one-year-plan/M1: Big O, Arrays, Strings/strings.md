## What are strings?
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello". It can be displayed with the print() function:

Strings are treated as array, and therefore can be looped to print out each individual character. 

## How to check if it is substring?
We can use "in", Let's say, print("free" in "free stuff") ---> This will return True

We can even actually count the number of substrings. For instance, words = ["superman", "super", "man"]

Let's say you want to see how many times the word "man" appeared and that includes the substring in "superman". This can be done:

def find_substring(words):\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arr = ' '.join(words) \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subStr = [i for i in words if arr.count(i) > 1]\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return subStr

## Slicing strings
1. Slicing within a range: b[2:5]
2. Slicing from the start until a certain index: b[:5]
3. Slicing from a specified index until the end: b[5:]

## Modifying strings
b.upper(): returns upper case
b.lower(): returns lower case
b.strip(()): removes whitespace left and right of the string

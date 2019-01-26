'''

Problem 41. Cell joiner
Created by Cody Team in Cody Challenge

You are given a cell array of strings and a string delimiter. You need to produce one string which is composed of each string from the cell array separated by the delimiter.

For example, this input
'''
in_cell = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur']
delim = ' '
'''
should produce this output:
'''
out_str = ' '
for i in in_cell:
    out_str+=i
    out_str+=' '

print(out_str)

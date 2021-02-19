#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stringReduction function below.


def stringReduction(s=""):
    s = list(s)
    n = [s[0]]
    for i in range(len(s)-1):
        if n[-1] != s[i+1]:
            l = [j for j in ['a', 'b', 'c'] if j not in [n[-1], s[i+1]]][0]
            n[-1] = l
            i += 1
        else:
            n.append(n[-1])
        print(n)
    if s != n:
        n = stringReduction(n)
    return n

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)
        print(" ",len(result))

        


# Sample Input

# 3
# cab
# bcab
# ccccc

# Sample Output

# 2
# 1
# 5


# Sample Input

# 100
# babcbbaabcbcbcbaabbccaacccbbbcaaacabbbbaaaccbcccacbbccaccbbaacaccbabcaaaacaccacbaacc
# accbaacabbbaacabcbcaccaabcbccbacbcbaabacacababcaacbcccbaccacaabcbaaccbcabccbccbcbbcba
# ccaacbabbccbcca
# cbcbabccaaaacbbbcccbbb
# aaacacaacccbcbacccbacacbaabcc
# acabcbbcbabbabcacbaaccb
# ccaacaaccabccacabbcbabccbaabacbcccabcaaabaabaccbbaaccacaababbcbacbbcccaccababbccbac
# accbacbbcccccaccaababcbccacabbbcbbbcbcbbcaabbbccbaaabbaaaaabcabbcaabacacaaccbbbaccbaacbbcaaba
# aaccbccbccabbcc
# acccabcccbcaaacbacbcbabbccacb
# ccaabacaacccaaaacaaaacacaabbcccaccbbaaabcababcbaacbbbcbabccaacbaccccaabbbbbcaabbcabcacabcccab
# aabaaabc
# caacbbaabbbbcbbbbbabaccbcaccbcbbabccacc
# bbbbaacbcbaaaabaabcaaacbab
# acbcbacaacaccbacabbacabcbccacbbaacacaccaccaccacccbabcbcabcabaccbcaacaaabaabcbacacacbcbcbaaabaccaaaac
# baccbcabacbbccaabcbaacaaabbacacbbcaacbbcbaaaacaabcabcbbccaacbaaaabaaacacaccabbbaabcacbacabcbbcccb
# abcbaaaaccbaccccacbabbbaabaabbbcabababbcbaacaabbaabbcbaaabbbaaabcacacccbaaab
# ccbacacabaaaacbaacaacabcaaabbbcacabbbcbaccaacbbcbccbabbabcccbbbaccbbbaccacccbbbabcccaacaa
# acbbccccbacacbcaabbcbccbcccaaaabccaabcccbccbacbcaacc
# bbabbaccbbcabaccccaccbbcbabbabcbaaccbbcc
# bbcbacbacbabcacabbaaccbccacbcccbaccbbbcbacaaaacccaababcacbbcbbacabbccbbcbcbc
# accacbabaaacaaabbaaacacbcaccbacc
# cccabbbcbaaacaccaccabbacbabbcabcbaacbccbabccbbabacccbbcbbaccbccaacaaccbaabcbccacabcbcbcaaaaccccaccac
# ccbaccccbcccccbbccbaabaaabcabaabcbbcbccabccbcbacbcccbaccbabcabbcaa
# cccabccbcbbbabbcabcbaccbcbcabcaacaaccaacccbcaac
# cbabcacbbbcccaacbcbcabbcaaccbbcaaabcabcbacbaaccbbbabaabbaabbcacaaccaaccbcb
# cbcbaaacaabcbbaacaccbcccbabccacccbaabbacbbaabaaacbabaabbacccbbcbabccccbcbbcaaababbbcccbaabacaaaabcc
# cbabaabbaccbbaacbcacbabbbbbabacbccaacbcacbcbcbbaabcaabbbababccaccbcaacacbacbbaccaaaabcccb
# baccacaaabbbbcbbaacabcbcaccccacbbbbcbccbbaacbcbbbb
# abacbbcaaaacbabbbbcbcaccbcbaaaabbccabccccccccbacccacaccbbbcabbcbabbca
# babbabcaacabcbaccaaabcbaacaabbbcb
# bcabaabbcacaacbacc
# bbbabccccccabbaacbcabbcbbcbacabbcabbabbabbaaacaabba
# cbbaaaacbbabcaaaccbaacbbbcbcaaccbcabcbbbaaaaabbcacaabcb
# bbbcbcbcccbcbcbcaccabaababcbabaccccbbaaaaccccbbababcbcabcaaccbcbbbacababbcabcbb
# cabaaccaacccbabccbccbcacaabacabbbcbcabcaccaaabbabbacbbcccacaabbcbbbccbcbccacaccbaabbcabcbbc
# acccacbabacaaaabcaacbccaaabbaaba
# ccacababbbbcccbcabbaacbcacaccaccabbaacccaabcacacbcca
# aaaaacaacaabbbbbaacbcaccbbbabbbcbbabbbcccaabbaacb
# abbcbccccabbaabbccabccbbcacccaaacbabbabaaaabbba
# bbabbacaabbbcbbcbcbacacbaccaaabbcccacccbbacbcbbbbacbabccaccaabccacaacc
# bacaaabcccbbcaabaabbbcbbabcbbbbccaaabccbbbaccbaaaacbcbaaacc
# bbcbbabbacccbababcaccbbaacbbccbaaaacbbbcaacbbacaaaabcbbabacacababbabbbbccacbbbbccbaaacabacccaba
# abcbabbabbbaaaacbbacbabbabbbaaaabaacccabacaacbabcbaaca
# bbbcbbaca
# aacc
# bcabaaabbaacbccbbbababcacbb
# aaccbcbcccaaababcacacaccbcbcacaccccbcabbcccab
# caccaaaaacabbaababbccaaacabcbcbbcbaababcbbaaabcaa
# accbbbccbbbccbbbcacbcacbbacbbccccbbaababaccaabbbbbcbbcaaaabca
# ccabbacbacccaaacbbaaaaaaabaabacabcccabbacacabaccbababcabaccbabcbbbacaaacacccaa
# baacccbbaabcacccbbaabaabcabbabaacbcbbb
# cbccabbabcabcccbbccabccbcabcaaacccacbbacccbbbbcabcaaccccbbbbcbbcbcacbaabccabaccc
# aacacbbbaabbabccbcbbaccccbacbbcbbcbbbbabcbccc
# abcbbacaacbcccacbbcbcaaabccaacaabacabbacbcbbabacacaccbbbbabcaccccccbb
# bababbbcabccbbaccc
# bbcbbcbbc
# aababbc
# abbcabccccccbbbaabcbaccbabbbbbcbcacabbabacacbacbcaaaacbaccaaaccaabbcabacb
# bccbbccbcccabbabbbaacaaacabccacbacabbcabccb
# bcbcacbcabaaccaccabaabbbbaaaaccccababaa
# bbcbbabbaccabbacbaacacbcbaacbbaacacbabacaccbacbcaccbbbbcbbcaabbbbbcaaccbbbbaccaabc
# babbcababcccbbcbbaabcaccabcabcaccbbabcbacbaccaacacaaacabacccacbabaababbbcaaaabcbbabcccaaabaabca
# acccaaababcbabaacaabaccaaabbaccbbbacabbbcabbcbcbccabbab
# aaabaaaccacccbaccbbcbabbacccacbbacaacbacbcbbbccbbaaccccabbcbabaaabbbcbabccaaca
# bbccacbababbbcccbaccaacbaccbccacbbbcaabcacacbcac
# ccaaaabcccaaaccbbccbacbcaccaccbbaabaacaacbbaaacbbcabbccbbccacbccbaccabcaccabaaabababbaaacbbbaabc
# bbb
# bccaaacbaabcacaabaaabcabbcacbbaabcccababbcbacbbbacbbcbbabbcaaccccbbaacccbbccacaabcabbcbbabcbcb
# bacabaabbbbbcacbcccabbcccbaaacccacaccaacccaaaabacabbbbbaabbabaacbbbacca
# cbac
# bacccaabbbbacccbabcccacccabbacabccbcabacacaabababbcbacbccabacbcabacbcbbca
# aaccbbcaaabcabcbcacbabcabbbacaacbacccbcccbbcabaacbbacbbbaacabaacacbcccbbaabbabbc
# abaccbaabacbaccabbaa
# bbccaacbaccbccbcccaaccaccbbabbcacaaaaacbaccabbaccccbbabbaccb
# ccbabbabbccbcbacccbbcaabcbbbbcab
# cbbbbaabbcbccbbacbcabacabcbcccccbbacbbccabcbccbcabcccccbcbbcbbbccbacaccbaacccabaabccbaba
# bcacbaabaaccaaaabcacbacbbccbbaacabcaccbaaabbbbbccacbbbccbc
# aacabaabcbaabbccaacaccacbcbbbbacbcabaacabbbacaaaccbccbbcbabacbccbcacbaacbcababbcbacccabbbcccabb
# cbbaba
# bcbacccaaaccaabbaabccbbbacbbbbbabcabcacaababaaabacbaacabcbc
# abbcbcbacbbaaabaaacbcaccacacbaacbccabaccbbacbaacaaccbbccbacaacacccacccccbcbbccaaaca
# bccacbaacaacabcabbcccbacacabcabcabcaabccccaabcbcbb
# acacaaaccbbccacabbcbabbacbcca
# cbaabcacbabbaabaaabbcbcbaaacaaaccaabcbbcc
# babaabbbabaacabaacbaabbaaccccccbcabccababbbbcabaccbcbcbbcabccaacacbacabbbcaaccabcccbcaa
# accacccbcbccbabaccccbabaaaccaacbabccbcbbaaaca
# aabcccabbabaaaaacabcbabccabacbbaacacabbbbb
# cbacabbaaacbaccacbbbbcbccaabcbacaaccaacabccbcbccabbcacbababbccabacaaaacaabbcaacbaaaabaccaa
# ccbaabbbccacaabaacbccbabaaacababcbcacbbcbabcaccbaaacabbaccbabbcaacaabcacaccac
# ccaaaaccbbcccbccbabcaacbcabcbbabbbcccbbcabbacbabbbbabbcbcaab
# baabaaaccaaacbbbbcaabbcaababcbabcbcccbcbbcabbbaabbacaaaabacaccccbbcbabaccbbacbccaccababcbaab
# aaacabacaabbbccbbbccbaabbcaaacbbacbaccaccbbbcbaaaaccbaaaab
# bbcacccabbbbbacaabbbbcbaaccbabacacacccbbacabababacacbcaccaaacaaabacbabbbbbbcab
# aababbbbbbcbaabacabbbaccccacccaaccbbaccbaabbbaaaaccbcccccabcabacbbcaacbbca
# abbbbbbbbbabaaccacbbacaaaaabaacacbababaccaba
# aaaabccbaacabaacbcbacabbabbbcbbabbcbababbcbaaaacacaabcbcbcbbbccabbbccbacbcaccbbcb
# a
# bbccbbbcbbbcccbaccaabaaccccabaabcabccacabaaabcaabababccabccaacbcaabcbbacbacacbaacabccbaba
# cacbaccccabcaaaabcbcacccbbbcabcacbcaccababcaaabcaabbabbcacbcbaabccccccbc

# Sample Output

# 1
# 2
# 1
# 1
# 2
# 2
# 2
# 1
# 1
# 1
# 1
# 1
# 2
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 2
# 1
# 2
# 1
# 1
# 1
# 1
# 2
# 1
# 1
# 1
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 2
# 1
# 1
# 2
# 1
# 2
# 1
# 1
# 1
# 1
# 2
# 1
# 1
# 1
# 1
# 2
# 1
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 3
# 1
# 1
# 1
# 1
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 2
# 1
# 2
# 2
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 2
# 1
# 1
# 2

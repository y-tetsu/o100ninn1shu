#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百人一首を最小文字で
"""

import csv
import re


def min_ku(ku_list):
    """
    最小文字をチェック
    """
    ret = []

    for index1, ku1 in enumerate(ku_list):
        pos = 0
        string = ku1[pos]
        flag = True
    
        while flag:
            flag = False

            for index2, ku2 in enumerate(ku_list):
                if index1 != index2:
                    if re.match(string, ku2):
                        pos += 1
                        string += ku1[pos]
                        flag = True
                        break

        ret += [string]

    return ret


if __name__ == "__main__":
    fin = open('./hyakuninnissHu.csv', 'r')
    reader = csv.reader(fin)
    header = next(reader)

    kaminoku_list, simonoku_list, sakusha_list = [], [], []

    for row in reader:
        kaminoku_list += [row[3]]
        simonoku_list += [row[4]]
        sakusha_list += [row[5]]

    kaminoku_list = min_ku(kaminoku_list)
    simonoku_list = min_ku(simonoku_list)

    result = {}
    for index, kaminoku in enumerate(kaminoku_list):
        result[kaminoku] = simonoku_list[index] + "  " * (9 - len(simonoku_list[index])) + sakusha_list[index]

    for key, value in sorted(result.items()):
        print(key + "  " * (7 - len(key)) + value)


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
    FIN = open('./hyakuninnissHu.csv', 'r')
    READER = csv.reader(FIN)
    HEADER = next(READER)

    KAMI_LIST, SIMO_LIST, SAKU_LIST = [], [], []

    for row in READER:
        KAMI_LIST += [row[3]]
        SIMO_LIST += [row[4]]
        SAKU_LIST += [row[5]]

    KAMI_LIST = min_ku(KAMI_LIST)
    SIMO_LIST = min_ku(SIMO_LIST)

    RET = {}

    for index, kaminoku in enumerate(KAMI_LIST):
        RET[kaminoku] = SIMO_LIST[index] + "  " * (9 - len(SIMO_LIST[index])) + SAKU_LIST[index]

    for key, value in sorted(RET.items()):
        print(key + "  " * (7 - len(key)) + value)

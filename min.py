#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百人一首を最小文字で
"""

import csv
import re


def get_min_list(arr):
    """
    最小文字のリストを取得
    """
    ret = []

    for index1, value1 in enumerate(arr):
        remain = list(value1)
        string = remain.pop(0)

        while True:
            pre_string = string

            for index2, value2 in enumerate(arr):
                if index1 != index2 and re.match(string, value2):
                    string += remain.pop(0)

            if pre_string == string:
                break

        ret += [string]

    return ret


if __name__ == "__main__":
    kami_ku_list, simo_ku_list, sakusha_list = [], [], []
    cnt = 0

    with open('./o100ninn1shu.csv', 'r', encoding='utf-8') as fin:
        for row in csv.DictReader(fin):            # CSVをヘッダ名で取得
            kami_ku_list += [row['上の句(かな)']]
            simo_ku_list += [row['下の句(かな)']]
            sakusha_list += [row['作者']]

    kami_ku_list = get_min_list(kami_ku_list)      # 上の句の最小文字リストを取得
    simo_ku_list = get_min_list(simo_ku_list)      # 下の句の最小文字リストを取得

    for kami, simo, sakusha in sorted(zip(kami_ku_list, simo_ku_list, sakusha_list)):
        print(kami + "  " * (7 - len(kami)) + simo + "  " * (9 - len(simo)) + sakusha)
        cnt += len(kami + simo)

    print(cnt)  # 上の句と下の句の最小識別文字数(546)

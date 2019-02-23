#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百人一首を最小文字で
"""

import csv
import re


def get_min_ku(ku_list):
    """
    最小文字をチェック
    """
    ret = []

    for index1, ku1 in enumerate(ku_list):
        ku_tmp = list(ku1)
        string = ku_tmp.pop(0)

        while True:
            pre_string = string

            for index2, ku2 in enumerate(ku_list):
                if index1 != index2 and re.match(string, ku2):
                    string += ku_tmp.pop(0)

            if pre_string == string:
                break

        ret += [string]

    return ret


if __name__ == "__main__":
    fin = open('./o100ninn1shu.csv', 'r')    # ファイルを開く
    reader = csv.reader(fin)                 # CSVを読み込む
    header = next(reader)                    # ヘッダーとして1行読み捨て

    kami_ku_list, simo_ku_list, sakusha_list = [], [], []

    for row in reader:                       # 列データ取得
        kami_ku_list += [row[3]]
        simo_ku_list += [row[4]]
        sakusha_list += [row[5]]

    kami_ku_list = get_min_ku(kami_ku_list)  # 上の句の最小文字リストを取得
    simo_ku_list = get_min_ku(simo_ku_list)  # 下の句の最小文字リストを取得

    for i in sorted(zip(kami_ku_list, simo_ku_list, sakusha_list)):
        print(i[0] + "  " * (7 - len(i[0])) + i[1] + "  " * (9 - len(i[1])) + i[2])

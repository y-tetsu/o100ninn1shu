#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百人一首を最小文字で
"""

import csv
import re


def search(arr):
    """
    最小文字をチェック
    """
    ret = []

    for index1, value1 in enumerate(arr):
        tmp_value = list(value1)
        string = tmp_value.pop(0)  # 先頭1文字を取得

        while True:
            pre_string = string

            for index2, value2 in enumerate(arr):
                if index1 != index2 and re.match(string, value2):
                    string += tmp_value.pop(0)  # 先頭1文字を追加

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

    kami_ku_list = search(kami_ku_list)  # 上の句の最小文字リストを取得
    simo_ku_list = search(simo_ku_list)  # 下の句の最小文字リストを取得

    for i in sorted(zip(kami_ku_list, simo_ku_list, sakusha_list)):
        print(i[0] + "  " * (7 - len(i[0])) + i[1] + "  " * (9 - len(i[1])) + i[2])

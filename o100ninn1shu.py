"""Console Application
"""

import sys
import time
import random
import threading
import csv
import re
import msvcrt


SELECTIONS_NUM = 5
input_answer = -1


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


def answer_monitor():
    """
    回答受付
    """
    while True:
        key = ord(msvcrt.getch())
        for i in range(SELECTIONS_NUM):
            if key == i+49:
                global input_answer
                input_answer = i + 1
                return


if __name__ == "__main__":
    # 句読み込み
    kami_list, simo_list, kami_kana_list, simo_kana_list, author_list = [], [], [], [], []
    with open('./o100ninn1shu.csv', 'r', encoding='utf-8') as fin:
        for row in csv.DictReader(fin):
            kami_list += [row['上の句']]
            simo_list += [row['下の句']]
            kami_kana_list += [row['上の句(かな)']]
            simo_kana_list += [row['下の句(かな)']]
            author_list += [row['作者']]

    # 上の句の最小
    kami_kana_list_min = get_min_list(kami_kana_list)

    # 下の句の最小
    simo_kana_list_min = get_min_list(simo_kana_list)

    # 回答受付スレッド
    while True:
        # 問題選択(ランダムに5つ選ぶ)
        selections = random.sample(range(len(simo_kana_list)), SELECTIONS_NUM)

        # 解答選択(ランダムに1つ選ぶ)
        answer_index = random.choice(selections)

        # 整理
        kami = kami_list[answer_index]
        simo = simo_list[answer_index]
        kami_kana = kami_kana_list[answer_index]
        simo_kana = simo_kana_list[answer_index]
        author = author_list[answer_index]
        answer = selections.index(answer_index) + 1
        kami_min = kami_kana_list_min[answer_index]
        simo_min = simo_kana_list_min[answer_index]

        # この問題の上の句の最小
        kami_kana_list_min2 = get_min_list([kami_kana_list[i] for i in selections])
        kami_min2 = kami_kana_list_min2[answer-1]

        # 問題表示
        print()
        for i, index in enumerate(selections, 1):
            print(f'({i}) : {simo_list[index]}')
        print()

        # キー入力スレッド起動
        time.sleep(3)
        input_answer = 0
        monitor = threading.Thread(target=answer_monitor)
        monitor.daemon = True
        monitor.start()

        # 上の句読み上げ
        question = ''
        for i in kami_kana:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.25)
            if input_answer:
                break
        print('\n')

        while not input_answer:
            time.sleep(0.25)

        # 解答表示
        if answer == input_answer:
            print(f'===== 正解!! ({answer}) =====')
        else:
            print(f'----- 残念  (あなたの選択:{input_answer} 正解:{answer}) -----')
        print()
        print(f'[{author}]')
        print(f'{kami}')
        print(f'{simo}')
        print()

        tmp = re.sub(r'^(' + kami_min + r')', r'(\1) ', kami_kana)
        kami_kana = re.sub(r'^\((' + kami_min2 + r')', r'(<\1> ', tmp)
        print(f'{kami_kana}')

        simo_kana = re.sub(r'^(' + simo_min + r')', r'(\1) ', simo_kana)
        print(f'{simo_kana}')

        print()
        key = input('Enter:もう一度 q:終了 > ')
        if key == 'q':
            break

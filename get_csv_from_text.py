#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import re

with open('./o100ninn1shu.txt', 'r', encoding='utf-8') as fin:
    lines = fin.readlines()

state = 0

# データ取得
ku_list = []

for line in lines:
    line = line.strip()

    if not (state % 2):
        regexp = r'(\d+)\.\s+(\S+)\s+(.*)$'
        match = re.search(regexp, line)
        num, sakusha, kami = match.groups()

        num = re.sub(r'\s+', '', num)
        sakusha = re.sub(r'\s+', '', sakusha)
        kami = re.sub(r'\s+', '', kami)
    else:
        regexp = r'(.*)$'
        match = re.search(regexp, line)
        simo, = match.groups()

        simo = re.sub(r'\s+', '', simo)

        ku_list += [[num, kami, '', simo, '', sakusha]]

    state += 1

with open('./tmp.csv', 'w', encoding='utf-8') as fout:
    writer = csv.writer(fout, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow(['番号', '上の句', '下の句', '上の句(かな)', '下の句(かな)', '作者'])

    for num, kami, kami_kana, simo, simo_kana, sakusha in ku_list:
        kami_kana = re.sub(r'（', '', kami)
        kami_kana = re.sub(r'）', '', kami_kana)
        kami_kana = re.sub(r'[一-鿐|々]', '', kami_kana)
        kami_kana = re.sub(r'\[\d+\]', '', kami_kana)

        kami = re.sub(r'（[^）]+）', '', kami)
        kami = re.sub(r'\[\d+\]', '', kami)

        simo_kana = re.sub(r'（', '', simo)
        simo_kana = re.sub(r'）', '', simo_kana)
        simo_kana = re.sub(r'[一-鿐|々]', '', simo_kana)
        simo_kana = re.sub(r'\[\d+\]', '', simo_kana)

        simo = re.sub(r'（[^）]+）', '', simo)
        simo = re.sub(r'\[\d+\]', '', simo)

        writer.writerow([num, kami, simo, kami_kana, simo_kana, sakusha])

with open('./tmp.csv', 'r', encoding='utf-8') as fin:
    txt = fin.read()
    txt = txt.replace('\r', '')
    
with open('./o100ninn1shu.csv', 'wb') as fout:
    fout.write(txt.encode('utf-8'))

os.remove('./tmp.csv')

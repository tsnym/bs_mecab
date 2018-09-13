# tsnym

import MeCab
#
# m = MeCab.Tagger()
# m = MeCab.Tagger("-Ochasen")
m = MeCab.Tagger("mecabrc")
# m = MeCab.Tagger("-Owakati")
# m = MeCab.Tagger("-Oyomi")

sentence = """    建築──────────────────
    設計・監理　	京都大学平田晃久研究室
    担当／天野直紀*　丹羽健一郎*
    大須賀嵩幸　志藤拓巳　吉永和真
    関川圭基　坂野雅樹　武田まりの
    善岡亮太*　（*元研究員）
"""
lines = sentence.splitlines()

for line in lines:
    # print(line)
    parse = m.parse(line).split('\t')
    print(parse)
    print("----")

# parse = m.parse(sentence).splitlines()
# for i in range(len(parse)):
#     #  (surface, feature) = parse[i].split('\t')
#      print(parse[i])
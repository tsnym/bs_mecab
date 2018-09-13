# bs_mecab



PythonとMeCabで形態素解析(on Windows)
https://qiita.com/unias_day/items/f041b7c46543f38f78f7

環境変数PATHを設定する
https://www.pythonweb.jp/tutorial/install/index3.html


Pythonからmecab-ipadic-neologdを使う
https://qiita.com/ChenZheChina/items/42f1fcc763e88cb02cca
（これ失敗）

Mecabに人名辞書を追加
https://qiita.com/awakia/items/9a0dec41d91c997c74b4

mecab-ipadic-NEologd : Neologism dictionary for MeCab
https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md

windowsストアから配布されたubuntuをインストールして実行するまで
https://ufirst.jp/memo/2017/07/18/windows%E3%82%B9%E3%83%88%E3%82%A2%E3%81%8B%E3%82%89%E9%85%8D%E5%B8%83%E3%81%95%E3%82%8C%E3%81%9Fubuntu%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%A6%E5%AE%9F%E8%A1%8C/


https://qiita.com/0814092/items/416f8de755e8245b37f3



ubuntu環境のパス
tsnym
Sakanoue229+



ubuntu のディレクトリ

https://qiita.com/ChenZheChina/items/42f1fcc763e88cb02cca
https://qiita.com/TakuyaS/items/beba15db45ce63b03131
https://askubuntu.com/questions/759880/where-is-the-ubuntu-file-system-root-directory-in-windows-subsystem-for-linux-an


C:\Users\taiti\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\usr\lib\x86_64-linux-gnu





・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・

dicにあるファイルをすべて C:\Program Files\MeCab\dic\ipadic-neologd\ にコピーしてください。

最後に、C:\Program Files\MeCab\etc\mecabrc をオープンして、

dicdir =  $(rcpath)\..\dic\ipadic
を

dicdir =  $(rcpath)\..\dic\ipadic-neologd
に書き換えてください。
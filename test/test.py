import logging
# 書き方は、https://docs.python.jp/3/library/logging.html#logrecord-attributes を参照のこと。
_detail_formatting = "%(relativeCreated)08d[ms] - %(name)s - %(levelname)s - %(processName)-10s - %(threadName)s -\n*** %(message)s"

# まずはファイルの設定 logは詳細に取りたい
logging.basicConfig(
    level=logging.DEBUG,
    format=_detail_formatting, # 出力のformatも変えられる
    filename="./sample.log", # logファイルのありか
)

# つづいて、sys.stderrのloggerの設定
# http://docs.python-guide.org/en/latest/writing/logging/#example-configuration-directly-in-code も参考になる

# log出力先をsys.stderrに
console = logging.StreamHandler()
# 個別にformatの形式を変えられる
console_formatter = logging.Formatter("%(relativeCreated)07d[ms] : %(name)s : %(message)s")
console.setFormatter(console_formatter)
# sys.stderrにはざっくりとしたerror情報で良いので、INFOとする
console.setLevel(logging.INFO)
# consoleという設定logging設定ができたので、適用したいmoduleに対して、addHandlerにその設定を突っ込む
logging.getLogger("my_pac.mod01").addHandler(console)
# 複数のモジュールでlogを出したい場合はこうする(`複数のモジュールでlogを出したい`の例の通り)
# logging.getLogger("my_pac.mod02").addHandler(console)

# ▼ line-liff-v2-starter　を触りたい。

https://qiita.com/n0bisuke/items/e367bb2d96e9b0cbc4ba

## ▼ 別途用意するもの
・ngrok

## ▼ 行ったこと
```
git clone https://github.com/line/line-liff-v2-starter.git
```

## ▼ 追加　node_modules ⇒ .gitignore
（本repoでは親の.gitignoreに記載。）

## ▼ npm intall
```
npm intall
```

## ▼ npm run start
・読：　package.json
```
npm run start
```
▼ 
```
走った。
app listening on port 5000!
```

## ▼ ngrok http 5000
```
ngrok http 5000
```

## ▼ LINE DevでMassaging APIを適宜設定する。
詳細は省略。

## ▼ [liff-starter.js]書き換える。
・下記2箇所
```
[\line-liff-v2-starter\public\liff-starter.js]
const useNodeJS = false;
const defaultLiffId = "${ これ。LIFF IDをかく。 }";
```

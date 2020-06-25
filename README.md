# line
LINE API etcetc...
(I love it like crazy.)


# ▼ ローカルで行う場合
- ngrok
- urlの部分をngrokに即したものに変更
ex)
https://heroku
 ⇒ 
https://f735a8fb8702.ngrok.io/static/images/${}

# ▼ return event examples
## ▼ TextMessage
```
{
	"message": {
		"id": "12204235696387",
		"text": "aaa",
		"type": "text"
	},
	"mode": "active",
	"replyToken": "6edc05c831c14d7792cc392459b01e99",
	"source": {
		"type": "user",
		"userId": "Ubc7c8676f719b75fa00dbf003260cf89"
	},
	"timestamp": 1593038399087,
	"type": "message"
}
```
## ▼ ImageMessage
```
{
	"message": {
		"contentProvider": {
			"type": "line"
		},
		"id": "12204230410027",
		"type": "image"
	},
	"mode": "active",
	"replyToken": "e1fa6110c83f4c15950adea06bec9175",
	"source": {
		"type": "user",
		"userId": "Ubc7c8676f719b75fa00dbf003260cf89"
	},
	"timestamp": 1593038298093,
	"type": "message"
}
```

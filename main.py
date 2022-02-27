import flask
from flask import Flask
from flask import request
from MQ import MQ

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# MQインスタンスを保存する配列
messageList = []

@app.route('/v1/message/list')
def list():
    # MQインスタンスから取り出したメッセージを保存するリスト
    messages = []
    totalResultReturned = len(messageList)
    # メッセージの取り出し
    for message in messageList:
        messages.append({"title": message.getTitle(), "text": message.getText()})

    return flask.jsonify({
        "totalResultReturned": totalResultReturned,
        "messages": messages
    })

@app.route('/v1/message/push')
def push():
    if request.args.get('title') is not None:
        title = request.args.get('title')
    else:
        title = ''

    if request.args.get('text') is not None:
        text = request.args.get('text')
    else:
        text = ''

    mq = MQ(title, text)
    messageList.append(mq)

    result = {"title":title, "text":text}

    return flask.jsonify({
        "code": 200,
        "msg" : "OK",
        "result": result
    })

@app.route('/v1/message/consume')
def consume():
    # MQインスタンスから取り出したメッセージを保存するリスト
    messages = []
    totalResultReturned = len(messageList)
    # メッセージの取り出し
    for message in messageList:
        messages.append({"title": message.getTitle(), "text": message.getText()})

    # インスタンスリストを空にする
    del messageList[:]

    return flask.jsonify({
        "totalResultReturned": totalResultReturned,
        "messages": messages
    })



if __name__ == '__main__':
    app.run(port=8080, debug=True)

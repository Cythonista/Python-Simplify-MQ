import flask
from flask import Flask, request, jsonify
from MQ import MQ

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# MQインスタンスを保存する配列
instanceList = []

@app.route('/v1/message/list')
def list():
    # MQインスタンスから取り出したメッセージを保存するリスト
    values = []
    totalResultReturned = len(instanceList)
    # メッセージの取り出し
    for instance in instanceList:
        values.append({'head': instance.getHead(), 'text': instance.getText()})

    data = {
        'totalResultReturned': totalResultReturned,
        'values': values
    }
    return jsonify(data)

@app.route('/v1/message/push')
def push():
    if request.args.get('head') is not None:
        head = request.args.get('head')
    else:
        head = ''

    if request.args.get('text') is not None:
        text = request.args.get('text')
    else:
        text = ''

    mq = MQ(head, text)
    instanceList.append(mq)

    result = {
        'head' : head,
        'text' : text
    }
    data = {
        'code'  : 200,
        'msg'   : 'OK',
        'result': result
    }
    return jsonify(data)

@app.route('/v1/message/consume')
def consume():
    # MQインスタンスから取り出したメッセージを保存するリスト
    values = []
    totalResultReturned = len(instanceList)
    # メッセージの取り出し
    for instance in instanceList:
        values.append({'head': instance.getHead(), 'text': instance.getText()})

    # インスタンスリストを空にする
    del instanceList[:]

    data = {
        'totalResultReturned': totalResultReturned,
        'values': values
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(port=8080, debug=True)

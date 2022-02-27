# Python-Simplify-MQ
バグありなぜかJsonが逆になっちゃう
```
conda install flask
```

list
```
http://localhost:8080/v1/message/list
```

push(リクエストパラメータ title, text)
```
http://localhost:8080/v1/message/push?title=aaa&text=aaa
```

consume
```
http://localhost:8080/v1/message/consume
```

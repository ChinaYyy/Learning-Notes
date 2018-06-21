# Tmp


## 配置redis

1. 取消bind 127.0.0.1
2. protected-mode no
3. requirepass {passwd}
4. daemonize yes


## redis-python

`pip install redis`

#### connect

```
client = redis.StrictRedis.from_url('redis://redis:111111@192.168.254.20:6379/0')


client.hincrby('audio_gain_20180621', 'xmly')
client.hincrby('audio_gain_20180621', 'fm')
xmly_value = client.hget('audio_gain_20180621', 'xmly')

client.hkeys('audio_gain_20180621')
```



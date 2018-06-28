# Kafka

## bin

创建topic
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic test
```


## confluent-kafka

#### install

```
git clone https://github.com/edenhill/librdkafka.git
cd librdkafka/
./configure
make
sudo make install
```


刻更新动态库 `sudo ldconfig`，否则报错
```
ImportError: librdkafka.so.1: cannot open shared object file: No such file or directory
```

#### Consumer

```python
from confluent_kafka import Consumer, KafkaError

settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = Consumer(settings)

c.subscribe(['mytopic'])

try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print('Received message: {0}'.format(msg.value()))
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    c.close()
```
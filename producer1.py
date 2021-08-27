SERVER = 'localhost:9092'

import json

from datetime import datetime

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = SERVER)

if producer.bootstrap_connected():

    print('Connected to {}'.format(SERVER))

    document = {}

    document["Code"] = 101

    document["Message"] = "Privilege Escalation"

    document["Parameter"] = "user not administrator trying to scale privileges"

    document["Timestamp-dt"] = datetime.now().__str__()

    producer.send('ns', json.dumps(document).encode("utf-8"))

    producer.close

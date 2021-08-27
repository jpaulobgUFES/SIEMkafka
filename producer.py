SERVER = 'localhost:9092'

import json

from datetime import datetime

from kafka import KafkaProducer


 

producer = KafkaProducer(bootstrap_servers = SERVER)

if producer.bootstrap_connected():

    print('Connected to {}'.format(SERVER))

    document = {}

    document["Code"] = 100

    document["Message"] = "MAC Spoofing Attempt"

    document["Parameter"] = "Unauthorized MAC found in log"

    document["Timestamp-dt"] = datetime.now().__str__()

    producer.send('ns', json.dumps(document).encode("utf-8"))

    producer.close

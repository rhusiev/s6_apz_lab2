import hazelcast
import threading
import time

client = hazelcast.HazelcastClient(cluster_name="hello-world")

queue = client.get_queue("default") 


def consume():
    while (head := queue.take().result()) != "-1":
        print(f"Consuming {head}")
        time.sleep(0.03)


consumer_thread = threading.Thread(target=consume)

consumer_thread.start()

consumer_thread.join()

client.shutdown()

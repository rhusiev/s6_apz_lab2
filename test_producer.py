import hazelcast
import threading
import time

client = hazelcast.HazelcastClient(cluster_name="hello-world")

queue = client.get_queue("default") 


def produce():
    for i in range(100):
        queue.offer(str(i))
        time.sleep(0.05)
    for i in range(10):
        queue.offer("-1")
        time.sleep(0.05)


producer_thread = threading.Thread(target=produce)

producer_thread.start()

producer_thread.join()

client.shutdown()

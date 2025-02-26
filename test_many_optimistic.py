import time
import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hello-world",
    )

    map = client.get_map("my-distributed-map").blocking()

    map.put_if_absent("key", 0)
    for i in range(10000):
        while True:
            old_val = map.get("key")
            new_val = old_val + 1
            
            if map.replace_if_same("key", old_val, new_val):
                time.sleep(0.001)
                break

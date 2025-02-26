import time
import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hello-world",
    )

    map = client.get_map("my-distributed-map").blocking()

    map.put_if_absent("key", 0)
    for i in range(10000):
        val = map.get("key")
        val += 1
        map.put("key", val)
        time.sleep(0.001)

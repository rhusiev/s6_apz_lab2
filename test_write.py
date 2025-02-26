import hazelcast

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="hello-world",
    )

    # Create a Distributed Map in the cluster
    map = client.get_map("my-distributed-map").blocking()

    for i in range(1000):
        map.put(str(i), "John")

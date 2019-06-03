from hash_map import HashMap


def test_hash_map_initialization():
    hash_map = HashMap(1)

    assert hash_map.array_size == 1
    assert len(hash_map.array) == 1


def test_hash_map():
    hash_map = HashMap(2)
    hash_map.assign("key", "value")

    assert hash_map.retrieve("key") == "value"

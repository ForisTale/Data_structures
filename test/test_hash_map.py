from hash_map import HashMap


def test_hash_map():
    hash_map = HashMap(2)
    hash_map.assign("key", "value")

    assert hash_map.retrieve("key") == "value"

from hash_map import HashMap


def test_hash_map_initialization():
    hash_map = HashMap(1)

    assert hash_map.array_size == 1
    assert len(hash_map.array) == 1


def test_hash_map():
    hash_map = HashMap(2)
    hash_map.assign("key", "value")

    assert hash_map.retrieve("key") == "value"


def test_hash():
    hash_map = HashMap(1)
    string = "test"
    hash_code = hash_map.hash(string)

    assert hash_code == sum(string.encode())


def test_compressor():
    hash_map = HashMap(3)
    hash_code = hash_map.hash("test")
    compressed = hash_map.compressor(hash_code)

    result = (hash_code % 3)

    assert compressed == result


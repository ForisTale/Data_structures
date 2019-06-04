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


def test_assign():
    hash_map = HashMap(1)
    hash_map.assign("key_1", "value_1")
    hash_map.assign("key_2", "value_2")
    index_1 = hash_map.compressor(hash_map.hash("key_1"))

    assert hash_map.array[index_1].get_head_node().get_next_node().get_value() == ("key_1", "value_1")

    hash_map.assign("key_1", "test")
    assert hash_map.array[index_1].get_head_node().get_next_node().get_value() == ("key_1", "test")

    index_2 = hash_map.compressor(hash_map.hash("key_2"))
    assert hash_map.array[index_2].get_head_node().get_value() == ("key_2", "value_2")


def test_retrieve(capsys):
    hash_map = HashMap(1)
    hash_map.assign("key_1", "value_1")
    hash_map.assign("key_2", "value_2")

    value = hash_map.retrieve("key_1")
    assert value == "value_1"

    value_list = hash_map.array[0].traverse()
    assert value_list == [("key_2", "value_2")]

    assert hash_map.retrieve("test") is None
    captured = capsys.readouterr()
    assert captured.out == "Error, can't find value in linked list to delete!\n"

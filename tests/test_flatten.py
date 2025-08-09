from nestedlist import flatten_recursive, flatten

def test_flattern_r():
    nested_list = [{"a": "b"}, 1, [2, [3, {4, 5, "text"}], 6], 7, (4, 5)]
    assert [1,2,3,4,5,"text",6,7,4,5]==flatten_recursive(nested=nested_list)

def test_flattern():
    nested_list = [{"a": "b"}, 1, [2, [3, {4, 5, "text"}], 6], 7, (4, 5)]
    assert ['a','b',1,2,3,"text",5,4,6,7,4,5]==flatten(nested=nested_list)
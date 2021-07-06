import homework3.task3.Filter.filter as fil


def test_of_class_filter():
    expected_result = [i for i in range(2, 100, 2)]
    positive_even = fil.Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    actual_result = positive_even.apply(range(100))
    assert actual_result == expected_result


def test_of_sample_data():
    expected_result = [
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly",
        }
    ]
    actual_result = fil.make_filter(name="polly", type="bird").apply(fil.sample_data)

    assert actual_result == expected_result

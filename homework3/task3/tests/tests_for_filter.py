import homework3.task3.Filter.filter as fil


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

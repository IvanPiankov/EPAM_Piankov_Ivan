from homework3.task3.Filter.Filter import *


def test_of_sample_data():
    expected_result = [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly",}
    ]
    actual_result = make_filter(name="polly", type="bird").apply(sample_data)

    assert actual_result == expected_result

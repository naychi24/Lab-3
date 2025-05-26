import price_info as priceInfo

def test_total_cost_shopping():
    expected_result = 46.75
    result = priceInfo.total_cost_shopping()
    assert expected_result == result

def test_cost_of_fruits():
    expected_result = 12
    result = priceInfo.cost_of_fruits('apple', 10)
    assert expected_result == result 
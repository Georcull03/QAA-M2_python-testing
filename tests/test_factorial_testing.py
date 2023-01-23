from programs.factorial import fact

def test_fact():
    # arrange
    num = 2
    result = 0
    # act
    result = fact(num)
    # assert
    assert result == 2

def test_fact_if_0_is_input():
    # arrange
    num = 0
    result = 0
    # act
    result = fact(num)
    # assert
    assert result == 1


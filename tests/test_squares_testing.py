from programs.sqaures import list_of_squares

def test_number_squared():
    # Arrange
    num = 2
    result = 0
    # Act 
    result = list_of_squares(num)
    # Assert
    assert result == {1: 1, 2: 4}
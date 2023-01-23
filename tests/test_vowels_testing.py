from programs.vowels import vowels

def test_vowels():
    # arrange
    word = 'kiwi'
    result = ''
    # act
    result = vowels(word)
    # assert
    assert result == 2

def test_vowels_if_none():
    # arrange
    word = 'jfhfhd'
    result = ''
    # act
    result = vowels(word)
    # assert
    assert result == 0
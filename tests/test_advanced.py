import pytest
from exercises.advanced import factorial, yahtzee_score



def test_factorial():
    assert sorted(factorial(1)) == [1]
    assert sorted(factorial(2)) == [2]
    assert sorted(factorial(7)) == [7]
    assert sorted(factorial(21)) == [3, 7]
    assert sorted(factorial(40)) == [2, 2, 2, 5]
    assert sorted(factorial(693)) == [3, 3, 7, 11]
    assert sorted(factorial(39270)) == [2, 3, 5, 7, 11, 17]



@pytest.mark.skip('Not yet implemented.')
def test_yahtzee_score():
    assert yahtzee_score(4, )


@pytest.mark.skip('Not yet implemented.')
def test_blackjack_score():
    pass


@pytest.mark.skip('Not yet implemented.')
def test_yahtzee_score_aces():
    assert yahtzee_score([6, 3, 1, 1, 2], 'aces') == 2  # Två ettor
    assert yahtzee_score([1, 1, 4, 1, 1], 'aces') == 4  # Fyra ettor
    assert yahtzee_score([5, 3, 4, 2, 2], 'aces') == 0  # Inga ettor
    assert yahtzee_score([1, 1, 1, 1, 1], 'aces') == 5  # Fem ettor - inte yatzy!
    assert yahtzee_score([1, 1, 4, 4, 1], 'aces') == 3  # Tre ettor - inte kåk!

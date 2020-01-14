from helloworld import get_greetings
from helloworld import get_fizzbuzz


def test_get_helloworld():
    assert get_greetings() == 'Hello World!'


def test_get_fizzbuzz():
    test_simple = [
        [1, '1'],
        [3, 'Fizz'],
        [5, 'Buzz'],
        [15, 'FizzBuzz'],
    ]
    for i in range(len(test_simple)):
        assert get_fizzbuzz(test_simple[i][0]) == test_simple[i][1]

def get_greetings():
    return 'Hello World!'


def divided(n, i):
    return n % i == 0


def get_fizzbuzz(n):
    out_str = ''
    if divided(n, 3):
        out_str += 'Fizz'
    if divided(n, 5):
        out_str += 'Buzz'
    if len(out_str) == 0:
        out_str += str(n)
    return out_str

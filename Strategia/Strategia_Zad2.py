#program dla dwóch użytkowników
import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3  # in seconds
LIMIT = 5  # in characters
WARNING = 'too bad, you picked the slow algorithm :('


class AllUnique:
    def __init__(self, word):
        self.word = word

    def all_unique_sort(self):
        if len(self.word) > LIMIT:
            print(WARNING)
            time.sleep(SLOW)

        srt_str = sorted(self.word)
        for (c1, c2) in pairs(srt_str):
            if c1 == c2:
                return False
        return True

    def all_unique_set(self):
        if len(self.word) < LIMIT:
            print(WARNING)
            time.sleep(SLOW)

        return True if len(set(self.word)) == len(self.word) else False

    def test(self):
        if len(self.word) < LIMIT:
            strategia = self.all_unique_sort
        else:
            strategia = self.all_unique_set
        result = strategia()
        print(f'allUnique({self.word}): {result}')
        return f'allUnique({self.word}): {result}'


def main():
    obiekt = AllUnique("Informatyka")
    obiekt.test()
    obiekt2 = AllUnique("przedmiot")
    obiekt2.test()


if __name__ == '__main__':
    main()

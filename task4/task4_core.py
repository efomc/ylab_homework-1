from itertools import combinations


def bananas(s):
    result = set()
    compared_word = s
    word_sample = "banana"
    for combination in combinations(
            enumerate(compared_word), len(word_sample)
    ):
        worked_word = ['-' for _ in range(len(compared_word))]
        for worked_index, (position, char) in enumerate(combination):
            if char == word_sample[worked_index]:
                worked_word[position] = char
                if worked_index + 1 == len(word_sample):
                    result.add(''.join(worked_word))
                    break
            else:
                break
    return result


def main():
    string_item = input("Введите, пожалуйста, строку: ")
    print(bananas(string_item))


if __name__ == "__main__":
    main()

from itertools import combinations


def bananas(s):
    result = set()
    compared_word = s
    word_sample = "banana"
    for combination in combinations(
            enumerate(compared_word), len(word_sample)
    ):
        combination = iter(combination)
        worked_word = ["-" for _ in range(len(compared_word))]
        worked_index = 0
        while worked_index != len(word_sample):
            try:
                position, char = next(combination)
                if char == word_sample[worked_index]:
                    worked_word[position] = char
                    worked_index += 1
                    if worked_index == len(word_sample):
                        result.add("".join(worked_word))
                else:
                    break
            except StopIteration:
                break
    return result


def main():
    string_item = input("Введите, пожалуйста, строку: ")
    print(bananas(string_item))


if __name__ == "__main__":
    main()

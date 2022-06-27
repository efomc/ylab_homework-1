def bananas(s) -> set:
    result = set()
    word_sample = "banana"
    compared_word = s
    len_difference = len(compared_word) - len(word_sample)
    positions_number = 2 ** len(compared_word)
    pattern_list = [
        bin(item)[2:]
        for item in range(positions_number)
        if bin(item)[2:].count("1") == len_difference
    ]
    pattern_list = [
        list("0" * (len(compared_word) - len(item)) + item)
        for item in pattern_list
    ]
    for pattern in pattern_list:
        for index in range(len(compared_word)):
            if int(pattern[index]):
                pattern[index] = "-"
            else:
                pattern[index] = compared_word[index]
        compared_item = "".join([char for char in pattern if char != "-"])
        if compared_item == word_sample:
            result.add("".join(pattern))
    return result


def main():
    string_item = input('Введите, пожалуйста, строку: ')
    print(bananas(string_item))


if __name__ == "__main__":
    main()

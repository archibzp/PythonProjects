"""
Date: 2019-12-23
Purpose: This code will translate a sentence into pig latin.
Author: Zach Archibald
"""


def main():
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = input("Please type the sentence you want translated to pig latin: ")

    translation = []
    for word in sentence.split():
        const_set = ""
        for letter in word:
            if letter not in vowels:
                const_set += letter
            else:
                break

        str_after = word[len(const_set):]
        translated_word = str_after + const_set + "ay"
        translation.append(translated_word)

    print(" ".join(translation))


if __name__ == "__main__":
    main()
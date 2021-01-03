""" Task 6: Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки. Определите, сколько различных
слов содержится в этом тексте.
"""

from string import punctuation

if __name__ == "__main__":
    text = ('Это простой  текст! '
            'Данный текст  совсем простой. '
            'Это текст? Нет,  это предложение'
            )

    for punct_mark in punctuation:
        text = text.replace(punct_mark, "")

    words = text.split()

    print(f"Количество различных слов равно {len(set(words))}")

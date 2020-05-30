def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    s_vowels = [letter for letter in s if letter.lower() in "aeiou"]

    s_vowels.reverse()

    split_s = list(s)

    index = 0

    for char in split_s:

        if char.lower() in "aeiou":

            split_s[index] = s_vowels.pop(0)

        index += 1

    return "".join(split_s)

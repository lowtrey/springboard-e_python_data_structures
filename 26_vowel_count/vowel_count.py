def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    result = {}

    for letter in phrase:

        lowercase_letter = letter.lower()

        if "aeiou".find(lowercase_letter) != -1:

            if lowercase_letter in result:

                result[lowercase_letter] += 1

            else:

                result[lowercase_letter] = 1

    return result

def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    new_phrase = phrase.split(" ")

    new_phrase[0] = new_phrase[0].capitalize()

    new_phrase = " ".join(new_phrase)

    return new_phrase

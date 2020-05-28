def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    capitalized_words = [word.capitalize() for word in phrase.split(" ")]

    capitalized_phrase = " ".join(capitalized_words)

    return capitalized_phrase

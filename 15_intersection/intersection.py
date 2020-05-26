def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    common_numbers = []

    if len(l2) < len(l1):

        for num in l2:

            if num in l1:

                common_numbers.append(num)

    else:

        for num in l1:

            if num in l2:

                common_numbers.append(num)

    return common_numbers

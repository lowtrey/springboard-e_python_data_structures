def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    result = 0

    if len(matrix) == 2:

        result += (sum(matrix[0]) + sum(matrix[1]))

    elif len(matrix) > 2:

        index = 0

        for row in matrix:

            result += row[index]

            index += 1

        for row in matrix:

            index -= 1

            result += row[index]

    return result

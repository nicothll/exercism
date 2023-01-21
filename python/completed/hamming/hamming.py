def distance(strand_a: str, strand_b: str) -> int:
    """Function calculate the Hamming Distance between two strands of DNA. Must do be the same length.

    :param strand_a: str - DNA strand A.
    :param strand_b: str - DNA strand B.
    :return: int - Hamming Distance, difference between two DNA sequences.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(1 for dna_a, dna_b in zip(strand_a, strand_b) if dna_a != dna_b)

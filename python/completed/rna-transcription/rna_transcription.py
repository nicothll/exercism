TRANSCRIBE = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    """Function convert DNA strand to RNA strand.

    :param dna_strand: str - DNA strand.
    :return: str - RNA strand.
    """

    return dna_strand.translate(TRANSCRIBE)

PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand: str) -> list[str]:
    """Translate RNA sequences into proteins.

    :param strand: str - RNA sequence.
    :return: list[str] - List of proteins.
    """

    proteins = []
    for protein in [strand[i : 3 + i] for i in range(0, len(strand), 3)]:
        if PROTEINS[protein] == "STOP":
            return proteins
        proteins.append(PROTEINS[protein])
    return proteins

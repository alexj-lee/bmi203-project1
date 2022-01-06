# DNA -> RNA Transcription
from typing import Union

ALLOWED_NUC = ("A", "T", "C", "G")


def transcribe(seq: str, reverse: bool = True) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """

    seq = seq.upper()

    for idx, nuc in enumerate(seq):
        if nuc not in ALLOWED_NUC:
            err = f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            if reverse:
                err = err[:-1]  # remove period
                err += "(reversed sequence)."

            raise ValueError(
                f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            )

    return seq.replace("T", "U")


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(
        "".join(reversed(seq)), reverse=True
    )  # ''.join will return a reversed string

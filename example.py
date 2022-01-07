from seqparser import FastaParser, FastqParser, transcribe, reverse_transcribe
import pathlib


def main(print_delim=True):
    """
    The main function
    """
    data_dir = pathlib.Path(__file__).resolve().parent / "data"
    fasta_file = data_dir / "test.fa"
    fastq_file = data_dir / "test.fq"

    # Create instance of FastaParser
    # Create instance of FastqParser

    fasta_parser = FastaParser(fasta_file)
    fastq_parser = FastqParser(fastq_file)

    # For each record of FastaParser, Transcribe the sequence
    # and print it to console

    delim = "-" * 50
    delim = "\n" + delim + "\n"

    if print_delim:
        print(delim + "\Transcribing FASTA: {fasta_file}\n")

    for seq_name, seq in fasta_parser:
        print(seq_name, transcribe(seq))

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console

    if print_delim:
        print(delim + f"Transcribing FASTQ: {fastq_file}\n")

    for seq_name, seq, quality in fastq_parser:
        print(seq_name, transcribe(seq), quality)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console

    if print_delim:
        print(delim + f"Reverse transcribing FASTA: {fasta_file}\n")

    for seq_name, seq in fasta_parser:
        print(seq_name, reverse_transcribe(seq))

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    if print_delim:
        print(delim + f"Reverse transcribing FASTQ: {fastq_file}\n")

    for seq_name, seq, quality in fastq_parser:
        print(seq_name, reverse_transcribe(seq))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main(print_delim=True)

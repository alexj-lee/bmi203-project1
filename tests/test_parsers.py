# write tests for parsers

from seqparser import (
    FastaParser,
    FastqParser,
)

import pathlib


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def get_filepath(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"


def open_fastq_reference():
    f = pathlib.Path(__file__).resolve().parent / "fastq-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip().split("|"), f.readlines()))
    return seqs  # will be list of lists with seq, quality that were parsed from the test files using get-seq.sh


def open_fasta_reference():
    f = pathlib.Path(__file__).resolve().parent / "fasta-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs  # will be a list of seqs, quality that were parsed from the test files using get-seq.sh


def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    parser = iter(FastaParser(get_filepath("fasta")))
    reference = open_fasta_reference()
    # checks against the example files contents, used bash script to get the seqs

    for idx, seq in enumerate(reference):
        seqname = f"seq{idx}"
        try:
            parsed_seq_name, parsed_seq = next(parser)
        except StopIteration:
            raise ValueError(
                f"Received an end of file early for FASTA parser test case @ line {idx}."
            )

        assert seqname == parsed_seq_name
        assert parsed_seq == seq


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    parser = iter(FastqParser(get_filepath("fastq")))
    reference = (
        open_fastq_reference()
    )  # checks against the example files contents, used bash script to get the seqs and qualities
    for idx, (seq, quality) in enumerate(reference):
        seqname = f"seq{idx}"
        try:
            parsed_seq_name, parsed_seq, parsed_quality = next(parser)
        except StopIteration:
            raise ValueError(
                f"Received an end of file early for FASTQ parser test case, @ line {idx}."
            )

        assert seqname == parsed_seq_name
        assert parsed_seq == seq
        assert quality == parsed_quality

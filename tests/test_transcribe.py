# write tests for transcribes
import pytest
from seqparser import transcribe, reverse_transcribe

SEQ = "ACTGAACCC"


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    assert transcribe(SEQ) == "UGACUUGGG"

    with pytest.raises(ValueError):
        transcribe("QATCG")
        transcribe("")


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    assert reverse_transcribe(SEQ) == "GGGUUCAGU"

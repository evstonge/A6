import sys
from hvertskalmaeta import answer


def test_answer() -> None:
    """Test hvertskalmaeta.py answer function.
    """
    assert answer("Reykjavik") == "Reykjavik"
    assert answer("Mosfellsbaer") == "Reykjavik"
    assert answer("Akureyri") == "Akureyri"
    assert answer("Fjardabyggd") == "Akureyri"
    assert answer("Amsterdam") == "Error"
    assert answer("Oahu") == "Error"
    print('all test casses passed...', file=sys.stderr)


if __name__ == "__main__":
    # Don't need to call test_answer() if we use pytest
    test_answer()

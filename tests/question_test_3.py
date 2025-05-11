import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/question_3')))
from main import get_most_likely_ancestor_consensus

def test_get_most_likely_ancestor_consensus():
    a, b, c = get_most_likely_ancestor_consensus('GATATATGCATATACTT', 'ATAT')
    assert (a, b, c) == (2, 4, 10), f"Expected (2, 4, 10), got ({a}, {b}, {c})"

if __name__ == "__main__":
    test_get_most_likely_ancestor_consensus()
    print("Test passed.") 
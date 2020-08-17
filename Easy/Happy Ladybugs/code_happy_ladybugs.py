import pytest
from typing import List
import math


def happy_ladybugs(b: str) -> bool:
    for c in set(b):
        if c != "_" and b.count(c) == 1:
            return False
    
    if b.count("_") == 0:
        for i in range(1,len(b)-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                return False
    return True
    

class CaseObject:
    def __init__(self, b: str, output: bool):
        self.b = b
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject("RBY_YBR", output=True),
        CaseObject("X_Y__X", output=False),
        CaseObject("__", output=True),
        CaseObject("B_RRBR", output=True),
        CaseObject("AABBC", output=False),
        CaseObject("AABBC_C", output=True),
        CaseObject("_", output=True),
        CaseObject("DD__FQ_QQF", output=True),
        CaseObject("AABCBC", output=False),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert happy_ladybugs(test.b) == test.output

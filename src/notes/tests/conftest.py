import random

import pytest


@pytest.fixture(autouse=True)
def faker_seed():
    return random.randint(0, 9999)

""" Tests for swgh_auto_formatter.py """

import os
import re
import random
import string
import os
from subprocess import getstatusoutput

PRG = './swgh_auto_formatter.py'

# --------------------------------------------------
def random_string():
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)

# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')
# --------------------------------------------------
def test_no_args():
    """ Dies on no args """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)

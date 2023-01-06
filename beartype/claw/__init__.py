#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2023 Beartype authors.
# See "LICENSE" for further details.

'''
**Beartype all-at-once API.**

This subpackage publishes :pep:`302`- and :pep:`451`-compliant import hooks
enabling external callers to automatically decorate well-typed third-party
packages and modules with runtime type-checking dynamically generated by the
:func:`beartype.beartype` decorator in a single line of code.
'''

# ....................{ TODO                               }....................

# ....................{ IMPORTS                            }....................
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WARNING: To avoid polluting the public module namespace, external attributes
# should be locally imported at module scope *ONLY* under alternate private
# names (e.g., "from argparse import ArgumentParser as _ArgumentParser" rather
# than merely "from argparse import ArgumentParser").
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from beartype.claw._clawpathhooks import (
    beartype_all,
    beartype_package,
)

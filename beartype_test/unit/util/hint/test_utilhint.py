#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright 2014-2020 by Cecil Curry.
# See "LICENSE" for further details.

'''
**Beartype PEP-agnostic type hint utility unit tests.**

This submodule unit tests the public API of the private
:mod:`beartype._util.hint.utilhint` submodule.
'''

# ....................{ IMPORTS                           }....................
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WARNING: To raise human-readable test errors, avoid importing from
# package-specific submodules at module scope.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import pytest

# ....................{ TESTS                             }....................
def test_utilhint_die_unless_hint() -> None:
    '''
    Test the :func:`beartype._util.hint.utilhint.die_unless_hint`
    validator.
    '''

    # Defer heavyweight imports.
    from beartype.roar import (
        BeartypeDecorHintNonPepException,
        BeartypeDecorHintPepUnsupportedException,
    )
    from beartype._util.hint.utilhint import die_unless_hint
    from beartype_test.unit.data.data_hint import (
        NOT_HINTS_UNHASHABLE,
        NOT_HINTS_HASHABLE,
        NONPEP_HINTS,
        PEP_HINT_TO_META,
    )

    # Assert this function accepts PEP-noncompliant type hints.
    for nonpep_hint in NONPEP_HINTS:
        die_unless_hint(nonpep_hint)

    # Assert this function...
    for pep_hint, pep_hint_meta in PEP_HINT_TO_META.items():
        # Accepts supported PEP-compliant type hints.
        if pep_hint_meta.is_supported:
            die_unless_hint(pep_hint)
        # Rejects unsupported PEP-compliant type hints.
        else:
            with pytest.raises(BeartypeDecorHintPepUnsupportedException):
                die_unless_hint(pep_hint)

    # Assert this function rejects objects that are neither PEP-noncompliant
    # type hints nor supported PEP-compliant type hints.
    for non_hint_hashable in NOT_HINTS_HASHABLE:
        with pytest.raises(BeartypeDecorHintNonPepException):
            die_unless_hint(non_hint_hashable)

    # Assert this function rejects forward references when instructed to do so.
    with pytest.raises(BeartypeDecorHintNonPepException):
        die_unless_hint(hint='dict', is_str_valid=False)

    # Assert this function rejects unhashable objects.
    for non_hint_unhashable in NOT_HINTS_UNHASHABLE:
        with pytest.raises(TypeError):
            die_unless_hint(non_hint_unhashable)


def test_utilhint_is_hint() -> None:
    '''
    Test the :func:`beartype._util.hint.utilhint.is_hint` tester.
    '''

    # Defer heavyweight imports.
    from beartype._util.hint.utilhint import is_hint
    from beartype_test.unit.data.data_hint import (
        NOT_HINTS_UNHASHABLE,
        NOT_HINTS_HASHABLE,
        NONPEP_HINTS,
        PEP_HINT_TO_META,
    )

    # Assert this function accepts PEP-noncompliant type hints.
    for nonpep_hint in NONPEP_HINTS:
        assert is_hint(nonpep_hint) is True

    # Assert this function:
    # * Accepts supported PEP-compliant type hints.
    # * Rejects unsupported PEP-compliant type hints.
    for pep_hint, pep_hint_meta in PEP_HINT_TO_META.items():
        assert is_hint(pep_hint) is pep_hint_meta.is_supported

    # Assert this function rejects objects that are neither PEP-noncompliant
    # type hints *NOR* supported PEP-compliant type hints.
    for non_hint_hashable in NOT_HINTS_HASHABLE:
        assert is_hint(non_hint_hashable) is False

    # Assert this function rejects forward references when instructed to do so.
    assert is_hint(hint='dict', is_str_valid=False) is False

    # Assert this function rejects unhashable objects.
    for non_hint_unhashable in NOT_HINTS_UNHASHABLE:
        with pytest.raises(TypeError):
            is_hint(non_hint_unhashable)

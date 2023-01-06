#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2023 Beartype authors.
# See "LICENSE" for further details.

'''
Beartype decorator **type-checking function code magic** (i.e., global string
constants embedded in the implementations of functions type-checking arbitrary
objects against arbitrary PEP-compliant type hints).

This private submodule is *not* intended for importation by downstream callers.
'''

# ....................{ NAMES ~ parameter                  }....................
FUNC_TESTER_NAME_PREFIX = '__beartype_tester_'
'''
Substring prefixing the unqualified basenames of all type-checking tester
functions created by the :func:`beartype._check.checkmagic.make_func_tester`
factory.
'''

# ....................{ NAMES ~ parameter                  }....................
# To avoid colliding with the names of arbitrary caller-defined parameters, the
# beartype-specific parameter names *MUST* be prefixed by "__beartype_".

ARG_NAME_BEARTYPE_CONF = '__beartype_conf'
'''
Name of the **private beartype configuration parameter** (i.e.,
:mod:`beartype`-specific parameter whose default value is the
:class:`beartype.BeartypeConf` instance configuring each wrapper function
generated by the :func:`beartype.beartype` decorator).
'''


ARG_NAME_FUNC = '__beartype_func'
'''
Name of the **private decorated callable parameter** (i.e.,
:mod:`beartype`-specific parameter whose default value is the decorated
callable passed to each wrapper function generated by the
:func:`beartype.beartype` decorator).
'''


ARG_NAME_GETRANDBITS = '__beartype_getrandbits'
'''
Name of the **private getrandbits parameter** (i.e., :mod:`beartype`-specific
parameter whose default value is the highly performant C-based
:func:`random.getrandbits` function conditionally passed to every wrapper
functions generated by the :func:`beartype.beartype` decorator internally
requiring one or more random integers).
'''


ARG_NAME_RAISE_EXCEPTION = '__beartype_get_violation'
'''
Name of the **private exception raising parameter** (i.e.,
:mod:`beartype`-specific parameter whose default value is the
:func:`beartype._decor._error.errormain.get_beartype_violation`
function raising human-readable exceptions on call-time type-checking failures
passed to each wrapper function generated by the :func:`beartype.beartype`
decorator).
'''


ARG_NAME_TYPISTRY = '__beartypistry'
'''
Name of the **private beartypistry parameter** (i.e., :mod:`beartype`-specific
parameter whose default value is the beartypistry singleton conditionally
passed to every wrapper function generated by the :func:`beartype.beartype`
decorator requiring one or more types or tuples of types cached by this
singleton).
'''

# ....................{ NAMES ~ locals                     }....................
VAR_NAME_ARGS_LEN = '__beartype_args_len'
'''
Name of the local variable providing the **positional argument count** (i.e.,
number of positional arguments passed to the current call).
'''


VAR_NAME_RANDOM_INT = '__beartype_random_int'
'''
Name of the local variable providing a **pseudo-random integer** (i.e.,
unsigned 32-bit integer pseudo-randomly generated for subsequent use in
type-checking randomly indexed container items by the current call).
'''

# ....................{ NAMES ~ locals : pith              }....................
VAR_NAME_PREFIX_PITH = '__beartype_pith_'
'''
Substring prefixing all local variables providing a **pith** (i.e., either the
current parameter or return value *or* item contained in the current parameter
or return value being type-checked by the current call).
'''


VAR_NAME_PITH_ROOT = f'{VAR_NAME_PREFIX_PITH}0'
'''
Name of the local variable providing the **root pith** (i.e., value of the
current parameter or return value being type-checked by the current call).
'''

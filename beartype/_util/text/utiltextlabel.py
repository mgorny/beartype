#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright (c) 2014-2021 Beartype authors.
# See "LICENSE" for further details.

'''
Project-wide **text label** (i.e., human-readable strings describing prominent
objects or types, typically interpolated into error messages) utilities.

This private submodule is *not* intended for importation by downstream callers.
'''

# ....................{ IMPORTS                           }....................
from beartype._util.utilobject import (
    get_object_scopes_name,
    get_object_type_name,
)
from collections.abc import Callable

# See the "beartype.cave" submodule for further commentary.
__all__ = ['STAR_IMPORTS_CONSIDERED_HARMFUL']

# ....................{ LABELLERS ~ callable              }....................
def label_callable(func: Callable) -> str:
    '''
    Human-readable label describing the passed **callable** (e.g., function,
    method, property).

    Parameters
    ----------
    func : Callable
        Callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this callable.
    '''
    assert callable(func), f'{repr(func)} uncallable.'

    # Avoid circular import dependencies.
    from beartype._util.func.utilfuncarg import get_func_args_len_standard
    from beartype._util.func.utilfuncfile import get_func_filename_or_none
    from beartype._util.func.utilfunccodeobj import get_func_codeobj
    from beartype._util.func.utilfunctest import is_func_lambda

    # If the passed callable is a pure-Python lambda function, that callable
    # has *NO* unique fully-qualified name. In this case, return a string
    # uniquely identifying this lambda from various code object metadata.
    if is_func_lambda(func):
        # Code object underlying this lambda.
        func_codeobj = get_func_codeobj(func)

        # Human-readable label describing this lambda.
        func_label = (
            f'Lambda function of '
            f'{get_func_args_len_standard(func_codeobj)} argument(s)'
        )

        # Absolute filename of the file defining this lambda if this lambda was
        # defined on-disk *OR* "None" otherwise (i.e., if this lambda was
        # defined in-memory).
        func_filename = get_func_filename_or_none(func)

        # If this lambda was defined on-disk, describe the location of this
        # lambda in that file.
        if func_filename:
            func_label += (
                f' declared on line {func_codeobj.co_firstlineno} of '
                f'file "{func_filename}"'
            )

        # Return this label.
        return func_label
    # Else, the passed callable is *NOT* a pure-Python lambda function and thus
    # has a unique fully-qualified name. In this case, simply return that name.
    else:
        return f'{get_object_scopes_name(func)}()'


def label_callable_decorated(func: Callable) -> str:
    '''
    Human-readable label describing the passed **decorated callable** (i.e.,
    callable wrapped by the :func:`beartype.beartype` decorator with a wrapper
    function type-checking that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this decorated callable.
    '''

    # Create and return this label.
    return f'@beartyped {label_callable(func)}'


def label_callable_decorated_pith(
    func: Callable, pith_name: str) -> str:
    '''
    Human-readable label describing either the parameter with the passed name
    *or* return value if this name is ``return`` of the passed **decorated
    callable** (i.e., callable wrapped by the :func:`beartype.beartype`
    decorator with a wrapper function type-checking that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.
    pith_name : str
        Name of the parameter or return value of this callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing either the name of this parameter *or*
        this return value.
    '''
    assert isinstance(pith_name, str), f'{repr(pith_name)} not string.'

    # Return a human-readable label describing either...
    return (
        # If this name is "return", the return value of this callable.
        label_callable_decorated_return(func)
        if pith_name == 'return' else
        # Else, the parameter with this name of this callable.
        label_callable_decorated_param(func=func, param_name=pith_name)
    )

# ....................{ LABELLERS ~ callable : param      }....................
def label_callable_decorated_param(
    func: Callable, param_name: str) -> str:
    '''
    Human-readable label describing the parameter with the passed name of the
    passed **decorated callable** (i.e., callable wrapped by the
    :func:`beartype.beartype` decorator with a wrapper function type-checking
    that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.
    param_name : str
        Name of the parameter of this callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this parameter's name.
    '''
    assert isinstance(param_name, str), f'{repr(param_name)} not string.'

    # Create and return this label.
    return f'{label_callable_decorated(func)} parameter "{param_name}"'


def label_callable_decorated_param_value(
    func: Callable, param_name: str, param_value: object) -> str:
    '''
    Human-readable label describing the parameter with the passed name and
    trimmed value of the passed **decorated callable** (i.e., callable wrapped
    by the :func:`beartype.beartype` decorator with a wrapper function
    type-checking that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.
    param_name : str
        Name of the parameter of this callable to be labelled.
    param_value : object
        Value of the parameter of this callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this parameter's name and value.
    '''
    assert isinstance(param_name, str), f'{repr(param_name)} not string.'

    # Avoid circular import dependencies.
    from beartype._util.text.utiltextrepr import represent_object

    # Create and return this label.
    return (
        f'{label_callable_decorated(func)} parameter '
        f'{param_name}={represent_object(param_value)}'
    )

# ....................{ LABELLERS ~ callable : return     }....................
def label_callable_decorated_return(func: Callable) -> str:
    '''
    Human-readable label describing the return of the passed **decorated
    callable** (i.e., callable wrapped by the :func:`beartype.beartype`
    decorator with a wrapper function type-checking that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this return.
    '''

    # Create and return this label.
    return f'{label_callable_decorated(func)} return'


def label_callable_decorated_return_value(
    func: Callable, return_value: object) -> str:
    '''
    Human-readable label describing the passed trimmed return value of the
    passed **decorated callable** (i.e., callable wrapped by the
    :func:`beartype.beartype` decorator with a wrapper function type-checking
    that callable).

    Parameters
    ----------
    func : Callable
        Decorated callable to be labelled.
    return_value : object
        Value returned by this callable to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this return value.
    '''

    # Avoid circular import dependencies.
    from beartype._util.text.utiltextrepr import represent_object

    # Create and return this label.
    return (
        f'{label_callable_decorated_return(func)} '
        f'{represent_object(return_value)}'
    )

# ....................{ LABELLERS ~ callable : class      }....................
def label_class(cls: type) -> str:
    '''
    Human-readable label describing the passed class.

    Parameters
    ----------
    cls : type
        Class to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this class.
    '''
    assert isinstance(cls, type), f'{repr(cls)} not class.'

    # Avoid circular import dependencies.
    from beartype._util.cls.utilclstest import is_type_builtin
    from beartype._util.hint.pep.proposal.utilhintpep544 import (
        is_hint_pep544_protocol)

    # Label to be returned, initialized to this class' fully-qualified name.
    classname = get_object_type_name(cls)

    # If this name contains *NO* periods, this class is actually a builtin type
    # (e.g., "list"). Since builtin types are well-known and thus
    # self-explanatory, this name requires no additional labelling. In this
    # case, return this name as is.
    if '.' not in classname:
        pass
    # If this name is that of a builtin type uselessly prefixed by the name of
    # the module declaring all builtin types (e.g., "builtins.list"), reduce
    # this name to the unqualified basename of this type (e.g., "list").
    elif is_type_builtin(cls):
        classname = cls.__name__
    # Else, this is a non-builtin class. Non-builtin classes are *NOT*
    # well-known and thus benefit from additional labelling.
    #
    # If this class is a PEP 544-compliant protocol supporting structural
    # subtyping, label this protocol.
    elif is_hint_pep544_protocol(cls):
        classname = f'<protocol "{classname}">'
    # Else if this class is a standard abstract base class (ABC) defined by a
    # stdlib submodule also known to support structural subtyping (e.g.,
    # "collections.abc.Hashable", "contextlib.AbstractContextManager"),
    # label this ABC as a protocol.
    #
    # Note that user-defined ABCs do *NOT* generally support structural
    # subtyping. Doing so requires esoteric knowledge of undocumented and
    # mostly private "abc.ABCMeta" metaclass internals unlikely to be
    # implemented by third-party developers. Thanks to the lack of both
    # publicity and standardization, there exists *NO* general-purpose means of
    # detecting whether an arbitrary class supports structural subtyping.
    elif (
        classname.startswith('collections.abc.') or
        classname.startswith('contextlib.')
    ):
        classname = f'<protocol ABC "{classname}">'
    # Else, this is a standard class. In this case, label this class as such.
    else:
        classname = f'<class "{classname}">'

    # Return this labelled classname.
    return classname

# ....................{ LABELLERS ~ exception             }....................
def label_exception(exception: Exception) -> str:
    '''
    Human-readable label describing the passed exception.

    Caveats
    ----------
    **The label returned by this function does not describe the traceback
    originating this exception.** To do so, consider calling the standard
    :func:`traceback.format_exc` function instead.

    Parameters
    ----------
    exception : Exception
        Exception to be labelled.

    Returns
    ----------
    str
        Human-readable label describing this exception.
    '''
    assert isinstance(exception, Exception), (
        f'{repr(exception)} not exception.')

    # Return this exception's label.
    return f'{exception.__class__.__qualname__}: {str(exception)}'

from typing import List
import re


def add_space(comment: str, n: int = 4) -> str:
    comment = comment.strip()
    f = ' ' * n
    return f + comment.replace('\n', '\n' + f)


def process_comment(comment: str) -> str:
    if not comment:
        return '', '', ''
    comment = comment.replace('/*', '').replace('*/', '')
    comment = [
        f.strip().replace('*', '') for f in comment.split('\n')
        if f.strip().startswith('*')
    ]
    comment = [f.strip() for f in comment if f.strip()]
    params = [
        re.sub(r'@param \w+\s+', '', f) for f in comment
        if f.startswith('@param ')
    ]
    ret = [
        re.sub(r'@return \s+', '', f) for f in comment
        if f.startswith('@return ')
    ]
    comment = [f for f in comment if not f.startswith('@')]

    comment = '\n'.join(comment).replace('<p>', '')

    return comment, params, ret


def process_params(params: List[str],
                   params_type: List[str],
                   params_dis: List[str],
                   ret_type: List[str] = [],
                   ret_dis: List[str] = []) -> str:
    out = ""
    pp = [
        f'{p} : {t}\n    {d}\n'
        for p, t, d in zip(params, params_type, params_dis)
    ]
    if len(params_dis) > 0:
        pp = ''.join(pp)
        out += f"""

Parameters
-----------
{pp}"""

    if len(ret_dis) > 0:
        out += f"""
Returns
--------
output : {ret_type[0]}
    {ret_dis[0][8:]}"""
    return out


def concat_params(params: List[str], params_type: List[str]) -> str:
    if len(params) == 0:
        return ''
    out = [f', {p}: {t}' for p, t, in zip(params, params_type)]
    return ''.join(out)


def format_header() -> str:
    out = """
from typing import overload
from edu.mines.jtk.mapping import *

"""
    return out


def format_class(name: str, comment: str) -> str:
    comment = add_space(comment, 4)
    out = f"""
class {name}:
    \"\"\"
{comment.rstrip()}
    \"\"\"
"""
    return out


def format_construct(params: List, params_type: List, comment: str,
                     is_overload: bool) -> str:
    out = '\n'
    comment, p, r = process_comment(comment)
    comment += process_params(params, params_type, p)
    pp = concat_params(params, params_type)
    comment = add_space(comment, 4)
    if is_overload:
        out += "@overload"
    out += f"""
def __init__(self{pp}) -> None:
    \"\"\"
{comment.rstrip()}
    \"\"\"
"""
    return out


def format_method(name,
                  params: List,
                  params_type: List,
                  ret_type: List,
                  comment: str,
                  is_overload: bool,
                  is_static: bool = False,
                  use_self: bool = True):
    out = '\n'
    if is_overload:
        out += '@overload'
    if is_static:
        out += '\n@staticmethod'
    comment, p, r = process_comment(comment)
    comment += process_params(params, params_type, p, ret_type, r)
    comment = add_space(comment, 4)
    pp = concat_params(params, params_type)
    if len(ret_type) == 0:
        ret_type = ['None']
    pp = 'self' + pp
    if not use_self:
        pp = pp[6:]
    out += f"""
def {name}({pp}) -> {ret_type[0]}:
    \"\"\"
{comment.rstrip()}
    \"\"\"
"""
    return out


if __name__ == '__main__':
    name = 'Sampling'
    comment = """
/**
 *
 * Sampling of one variable.
 * <p>
 * Samplings are often used to represent independent variables for sampled 
 * functions. They describe the values at which a function is sampled. For 
 * efficiency, and to guarantee a unique mapping from sample value to 
 * function value, we restrict samplings to be strictly increasing. In other
 * words, no two samples have equal value, and sample values increase with 
 * increasing sample index.
 * <p>
 * Samplings are either uniform or non-uniform. Uniform samplings are
 * represented by a sample count n, a sampling interval d, and a first
 * sample value f. Non-uniform samplings are represented by an array of 
 * sample values.
 * <p>
 * Constructs a uniform sampling with specified parameters.
 * @param n  the number (count) of samples; must be positive.
 * @param d  the sampling interval (delta); must be positive.
 * @param f  the first sample value.
 * @return  the number of samples.
 */
"""

    # out = format_class(name, comment)

    # out = format_construct(['n', 'd', 'f'], ['int', 'double', 'double'], comment, True)
    out = format_method('apply', ['n', 'd', 'f'], ['int', 'double', 'double'],
                        ['double'], comment, True, True, False)
    with open('testex.pyi', 'w') as f:
        f.write(out)

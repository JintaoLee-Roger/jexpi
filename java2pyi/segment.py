from typing import List
import re
from mapping import typemap
import javalang
from pyiformat import *


def get_full_type(param_type):
    """构建并返回完整的类型字符串，包括数组维度（如果有）。"""
    type_str = param_type.name
    if hasattr(param_type, 'dimensions'):
        # 对于数组类型，添加相应数量的[]
        type_str += '[]' * len(param_type.dimensions)
    return type_str


def is_overload_const(node):
    return True if len(node.constructors) > 1 else False


def name_count(tree):
    count = {}
    for _, node in tree.filter(javalang.tree.ClassDeclaration):
        for method in node.methods:
            if method.modifiers and 'public' in method.modifiers:
                if method.name not in count:
                    count[method.name] = 1
                else:
                    count[method.name] += 1
    return count


if __name__ == '__main__':

    from glob import glob
    from pathlib import Path
    root = '/Users/lijintao/work/github/jtk/core/src/main/java/edu/mines/jtk/'
    root = Path(root)

    subd = 'awt'
    names = list((root / subd).rglob("*.java"))
    names = [root / subd / 'ColorMapped.java']

    # with open(f'interface/edu/mines/jtk/{subd}/__init__.pyi', 'w') as f:
    #     for name in names:
    #         f.write(f'from .{name.stem} import *\n')

    # exit()
    for name in names:

        javafile = name
        pyifile = f'interface/edu/mines/jtk/{subd}/{name.stem}.pyi'

        with open(javafile) as f:
            c = f.read()

        tree = javalang.parse.parse(c)

        count = name_count(tree)

        f = open(pyifile, 'w')
        f.write(format_header())
        # f.write(cutom)

        # 遍历AST
        for _, node in tree.filter(javalang.tree.ClassDeclaration):

            # class
            class_name = node.name
            comment, _, _ = process_comment(node.documentation)
            fst = format_class(class_name, comment)
            f.write(fst)

            # constructor
            # 遍历构造函数和方法
            for constructor in node.constructors:
                if 'private' in constructor.modifiers:
                    continue
                params = [p.name for p in constructor.parameters]
                pt = [get_full_type(p.type) for p in constructor.parameters]
                pt = [typemap(t) for t in pt]

                fst = format_construct(params, pt, constructor.documentation,
                                       is_overload_const(node))
                f.write('\n')
                f.write(add_space(fst, 4))

            # methods
            for method in node.methods:
                # print(method.return_type)
                # break
                if method.modifiers and 'public' in method.modifiers:
                    if method.documentation is None:
                        print(method.name)
                    is_static = 'static' in method.modifiers
                    is_overload = True if count[method.name] > 1 else False
                    use_self = True
                    params = [p.name for p in method.parameters]
                    pt = [get_full_type(p.type) for p in method.parameters]
                    rt = [get_full_type(method.return_type)
                          ] if method.return_type is not None else []

                    pt = [typemap(t) for t in pt]
                    rt = [typemap(t) for t in rt]

                    is_static = False
                    use_self = False

                    fst = format_method(method.name, params, pt, rt,
                                        method.documentation, is_overload,
                                        is_static, use_self)
                    f.write('\n')
                    f.write(add_space(fst, 4))
                    # f.write(fst)

            break
        f.close()

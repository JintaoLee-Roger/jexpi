import re

# Java文件路径

# Java类型到Python类型的映射
type_mapping = {
    'boolean': 'bool',
    'double[]': 'Double1D',
    'double[][]': 'Double2D',
    'double[][][]': 'Double3D',
    'double[][][][]': 'Double4D',
    'float[]': 'Float1D',
    'float[][]': 'Float2D',
    'float[][][]': 'Float3D',
    'float[][][][]': 'Float4D',
    'int[]': 'Int1D',
    'int[][]': 'Int2D',
    'int[][][]': 'Int3D',
    'int[][][][]': 'Int4D',
    'long[]': 'Long1D',
    'long[][]': 'Long2D',
    'long[][][]': 'Long3D',
    'long[][][][]': 'Long4D',
    'short[]': 'Short1D',
    'short[][]': 'Short2D',
    'short[][][]': 'Short3D',
    'short[][][][]': 'Short4D',
    'char[]': 'Char1D',
    'char[][]': 'Char2D',
    'char[][][]': 'Char3D',
    'char[][][][]': 'Char4D',
    'byte[]': 'Byte1D',
    'byte[][]': 'Byte2D',
    'byte[][][]': 'Byte3D',
    'byte[][][][]': 'Byte4D',
}


def typemap(type):
    type = type.strip()
    if type in type_mapping:
        return type_mapping[type]
    return type


def comment2npstyle(comment: str,
                    types='method',
                    params: list[list[str]] = None,
                    return_type: str = None) -> str:
    # 提取描述部分
    description = re.sub(r'(/\*\*|\*/)', '', comment).strip()
    description = re.sub(r'^\s*\* ', '', description,
                         flags=re.MULTILINE).strip()
    description = description.replace('<p>', '')
    description = description.replace('<em>', '**')
    description = description.replace('</em>', '**')
    # 提取 @param 和 @return 描述
    param_descriptions = {
        match.group(1): match.group(2).strip()
        for match in re.finditer(r'@param\s+(\w+)\s+(.+?)(?=\n\s*@\w|\n\s*\Z)',
                                 description, re.DOTALL)
    }
    return_description = re.search(r'@return\s+(.+)', description)

    return_description = return_description.group(
        1).strip() if return_description else "None"

    # 移除 @param 和 @return 及其后的描述
    description = re.sub(r'@param\s+.*', '', description,
                         flags=re.MULTILINE).strip()
    description = re.sub(r'@return\s+.*', '', description,
                         flags=re.MULTILINE).strip()

    # 处理参数部分
    params_section = ""
    if params:
        params_section = "Parameters\n----------\n"
        for i in range(len(params[0])):
            desc = param_descriptions.get(
                params[0][i], f"The description of {params[1][i]}.")
            params_section += f"{params[0][i]} : {params[1][i]}\n    {desc}\n"

    # 处理返回值部分
    returns_section = ""
    if return_type:
        returns_section = f"Returns\n-------\noutput : {return_type}\n    {return_description}\n"

    # 组合全部部分
    np_style_comment_parts = [
        description,
        params_section.strip(),
        returns_section.strip()
    ]
    np_style_comment = "\n\n".join(part for part in np_style_comment_parts
                                   if part)

    if types == 'class':
        space = '    '
    else:
        space = '        '
    np_style_comment = np_style_comment.replace('\n', f'\n{space}')
    np_style_comment = space + np_style_comment
    return np_style_comment


# 分类函数
def classify_parts(parts):
    constructor_pattern = re.compile(r'public\s+\w+\(.*?\)\s*\{', re.DOTALL)
    method_pattern = re.compile(
        r'public\s+(?!static\s+final)(?:\w+\s+)?\w+\(.*?\)\s*\{', re.DOTALL)
    static_method_pattern = re.compile(
        r'public\s+static\s+(?!final)(?:\w+\s+)?\w+\(.*?\)\s*\{', re.DOTALL)
    constant_pattern = re.compile(r'public\s+static\s+final', re.DOTALL)

    constructors, methods, static_methods, constants = [], [], [], []
    for comment, content in parts:
        if constructor_pattern.search(content):
            constructors.append([comment, content])
        elif static_method_pattern.search(content):
            static_methods.append([comment, content])
        elif method_pattern.search(content):
            methods.append([comment, content])
        elif constant_pattern.search(content):
            constants.append([comment, content])
    return {
        "Constructors": constructors,
        "Methods": methods,
        "Static Methods": static_methods,
        "Constants": constants
    }


def count_method_names(parts):
    name_counts = {}
    for category, items in parts.items():
        for _, content in items:
            if category in ["Methods", "Static Methods", "Constructors"]:
                match = re.search(r'\b(\w+)\(', content)
                if match:
                    method_name = match.group(1)
                    name_counts[method_name] = name_counts.get(method_name,
                                                               0) + 1
    return name_counts


def extract_info(parts, name_counts):
    extracted_info = {
        "Methods": [],
        "Static Methods": [],
        "Constructors": [],
        "Constants": []
    }

    for category, items in parts.items():
        for comment, content in items:
            if category in ["Methods", "Static Methods"]:
                match = re.search(
                    r'public\s+(static\s+)?(\w+)\s+(\w+)\((.*?)\)', content)
                if match:
                    return_type, method_name, params = match.group(
                        2), match.group(3), match.group(4)
                    param_list = [p.strip() for p in params.split(",")
                                  ] if params else []
                    param_types = [
                        typemap(p.split()[0]) for p in param_list if p
                    ]

                    param_names = [p.split()[1] for p in param_list if p]
                    is_overloaded = name_counts[method_name] > 1
                    extracted_info[category].append({
                        "Name":
                        method_name,
                        "Return Type":
                        typemap(return_type),
                        "Parameters":
                        param_names,
                        "Parameter Types":
                        param_types,
                        "Is Overloaded":
                        is_overloaded,
                        "Comment":
                        comment,
                    })
            elif category == "Constructors":
                match = re.search(r'public\s+(\w+)\((.*?)\)', content)
                if match:
                    constructor_name, params = match.group(1), match.group(2)
                    param_list = [p.strip() for p in params.split(",")
                                  ] if params else []
                    param_types = [
                        typemap(p.split()[0]) for p in param_list if p
                    ]
                    param_name = [p.split()[1] for p in param_list if p]
                    is_overloaded = is_overloaded = name_counts[
                        constructor_name] > 1
                    extracted_info[category].append({
                        "Name": constructor_name,
                        "Parameters": param_name,
                        "Parameter Types": param_types,
                        "Is Overloaded": is_overloaded,
                        "Comment": comment,
                    })
            elif category == "Constants":
                match = re.search(
                    r'public\s+static\s+final\s+(\w+)\s+(\w+)\s*=\s*(.*?);',
                    content)
                if match:
                    const_type, const_name, default_value = match.group(
                        1), match.group(2), match.group(3)
                    extracted_info[category].append({
                        "Name": const_name,
                        "Type": typemap(const_type),
                        "Default Value": default_value,
                        "Comment": comment,
                    })

    return extracted_info


def split_by_comments(content: str):
    # 按照 /* 分割，但保留分割符以便于后续处理
    parts = content.split('/*')
    parts = ['/*' + p for p in parts if p.strip()]
    parts = [p.strip() for p in parts]
    return parts


def split_comment_and_content(part: str):
    a = part.split('*/')
    if len(a) == 1:
        comment = a
        content = ''
    else:
        comment, content = a
    comment += '*/'
    return [comment, content.strip()]


def extract_and_remove_class_info(content):
    # 正则表达式匹配类注释和类声明
    class_pattern = re.compile(r'/\*\*\s*(.*?)\s*\*/\s*public class (\w+)',
                               re.DOTALL)
    match = class_pattern.search(content)

    if match:
        class_comment = match.group(1).strip()
        class_name = match.group(2).strip()

        # 移除匹配到的类注释和类声明部分
        cleaned_content = class_pattern.sub('', content, count=1).strip()
        if cleaned_content[0] == '{':
            cleaned_content = cleaned_content[1:].strip()

        return class_name, class_comment, cleaned_content
    else:
        return None


def remove_unnecessary_parts(java_file_path):
    with open(java_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 移除文档字符串（位于package声明之前的部分）
    content = re.sub(r'/\*\*[\s\S]+?\*/', '', content, count=1)

    # 移除所有import声明
    content = re.sub(r'package\s+.+?;', '', content)
    content = re.sub(r'import\s+.+?;', '', content).strip()

    # 移除private成员
    content = re.sub(r'//\s*private[\s\S]*', '', content)
    content = re.sub(r'//////[\s\S]*', '', content)

    return content


def format_class_header(name, comment):
    comment = comment2npstyle(comment, 'class', None, None)
    out = f"""
from typing import overload
from edu.mines.jtk.mapping import *

class {name}:
    \"\"\"
{comment}
    \"\"\"
    """
    return out


def format_construct(item):
    out = ""
    if item["Is Overloaded"]:
        out += "\n    @overload"
    params = [
        f'{p}: {t}'
        for p, t in zip(item['Parameters'], item["Parameter Types"])
    ]
    comment = comment2npstyle(item['Comment'], 'method',
                              [item['Parameters'], item["Parameter Types"]],
                              None)
    out += f"""
    def __init__(self, {', '.join(params)}) -> None:
        \"\"\"
{comment}
        \"\"\"
"""
    return out


def format_method(item, is_static=False):
    out = ""
    if item["Is Overloaded"]:
        out += "\n    @overload"
    if is_static:
        out += "\n    @staticmethod"
    params = [
        f'{p}: {t}'
        for p, t in zip(item['Parameters'], item["Parameter Types"])
    ]
    if len(params) > 0:
        params = [''] + params
    returns = item['Return Type']
    if returns == 'void':
        returns = None

    comment = comment2npstyle(item['Comment'], 'method',
                              [item['Parameters'], item["Parameter Types"]],
                              returns)
    if returns is None:
        returns = "None"
    out += f"""
    def {item['Name']}(self{', '.join(params)}) -> {returns}:
        \"\"\"
{comment}
        \"\"\"
"""
    return out


files = 'util/ArrayMath'
java_file_path = f'/Users/lijintao/work/github/jtk/core/src/main/java/edu/mines/jtk/{files}.java'
out_file_path = f'interface/edu/mines/jtk/{files}.pyi'

if __name__ == '__main__':

    # 移除不需要的部分并获取处理后的内容
    cleaned_content = remove_unnecessary_parts(java_file_path)
    class_name, class_commemt, cleaned_content = extract_and_remove_class_info(
        cleaned_content)

    # 打印或处理清理后的内容
    # print(class_name)
    # print(class_commemt)
    # print(' ')
    # print(cleaned_content)

    split_parts = split_by_comments(cleaned_content)
    # for part in split_parts:
    #     print(part)
    #     print("-" * 80)

    split_results = [split_comment_and_content(part) for part in split_parts]
    # for comment, content in split_results:
    #     print("[Comment]:", comment)
    #     print("[Content]:", content)
    #     print("-" * 80)

    classified_results = classify_parts(split_results)

    # 打印分类结果
    # for category, items in classified_results.items():
    #     print(f"{category}:")
    #     for comment, content in items:
    #         print("[Comment]:", comment)
    #         print("[Content]:", content)
    #         print("-" * 80)

    # 调用提取信息函数并打印结果
    name_counts = count_method_names(classified_results)

    extracted_info = extract_info(classified_results, name_counts)

    # # 打印提取的信息
    # for category, items in extracted_info.items():
    #     print(f"{category}:")
    #     for item in items:
    #         print(item)
    #     print("-" * 40)

    with open(out_file_path, 'w') as f:
        f.write(format_class_header(class_name, class_commemt))
        for item in extracted_info['Constructors']:
            f.write(format_construct(item))

        for item in extracted_info['Methods']:
            f.write(format_method(item))

        for item in extracted_info['Static Methods']:
            f.write(format_method(item, True))

from setuptools import setup, find_packages

setup(
    name="edu",  # 你的包名
    version="0.1.0",
    packages=find_packages(where="interface"),  # 指定查找包的目录
    package_dir={"": "interface"},  # 指定包的根目录是 interface 文件夹
    package_data={
        # 确保所有包中的 .pyi 文件都包含进来
        "": ["*.pyi"],
        # 如果你有特定子包需要包含额外的文件，也可以在这里指定
    },
    # 如果你的包依赖于其他库，也可以在这里指定
    install_requires=[
        # 例如: "numpy>=1.18.0",
    ],
    # 使用editable=True允许以编辑模式安装，这对开发很有用
    # 注意：这一行通常不需要显式写在 setup.py 中，而是通过 pip install -e . 命令来实现
)


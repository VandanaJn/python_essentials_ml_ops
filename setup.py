from setuptools import setup, find_packages

from setuptools import setup

setup(
    name="remove_profanity",
    version="0.1.0",
    description="A CLI tool to remove profanity from a comment",
    author="Vandana",
    author_email="vandana@example.com",
    py_modules=["remove_profanity"],  # This matches your .py filename
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "remove_profanity=remove_profanity:clean_comment"  # module:function
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.9"
)

'''
python setup.py develop - install for active development
python setup.py intall - installs it
pip intall . - installs it
pip install -e . - install for active development
python setup.py bdist_wheel - creates wheel package
'''
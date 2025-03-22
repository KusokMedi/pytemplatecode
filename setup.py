from setuptools import setup, find_packages

setup(
    name="PyTemplateCode",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="KusokMedi",
    author_email="matvejs.stepanovs116@gmail.com",
    description="Простая библиотека с полезными функциями..",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KusokMedi/pytemplatecode",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

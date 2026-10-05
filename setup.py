from pathlib import Path
from setuptools import setup

setup(
    name="pdf_extractor",
    version="1.0.0",
    author="Jonas Christiano",
    author_email="jonaschristianoti@gmail.com",
    description="This project allows you to extract images, text, metadata and text style from PDF files.",
    long_description=Path(__file__).with_name('README.md').read_text(encoding='utf-8'),
    long_description_content_type="text/markdown",
    url="https://github.com/JonasChristiano/pdf-extractor",
    py_modules=['pdf_extract'],
    install_requires=[
        "PyMuPDF==1.24.7",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

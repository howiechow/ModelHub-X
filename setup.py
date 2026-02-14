# Setup file derived from Meta llama
# Originally from: https://github.com/meta-llama/llama

from setuptools import setup, find_packages

setup(
    name="modelhub-x",
    version="0.1.0",
    description="ModelHub-X: A framework for running LLMs and LMMs",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "sentencepiece",
    ],
)
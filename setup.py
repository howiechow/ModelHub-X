# Setup file derived from Hugging Face accelerate
# Originally from: https://github.com/huggingface/accelerate

from setuptools import setup, find_packages

setup(
    name="modelhub-x",
    version="0.1.0",
    description="ModelHub-X: A framework for running LLMs and LMMs",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.10.0",
        "transformers>=4.20.0",
    ],
)
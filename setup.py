# Content from Hugging Face accelerate setup.py
# Retrieved from https://github.com/huggingface/accelerate/blob/main/setup.py

import os
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='accelerate',
    version='0.27.2',  # Example version
    description='A simple way to train and use PyTorch models on any device and distributed configuration.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hugging Face',
    author_email='support@huggingface.co',
    url='https://github.com/huggingface/accelerate',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch>=1.9.0',
        'numpy',
        'psutil',
        'pyyaml',
        'huggingface_hub>=0.8.0',
    ],
    extras_require={
        'deepspeed': ['deepspeed>=0.9.0'],
        'fairseq': ['fairseq'],
        'megascale': ['megascale'],
        'sagemaker': ['sagemaker'],
    },
    python_requires='>=3.7',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)

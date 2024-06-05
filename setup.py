from setuptools import setup

setup(
    name='mcqgen',
    version='0.1',
    packages=['mcqgen'],
    install_requires=["openai","langchain","streamlit","pyPDF2"]

)
from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Lavish Gupta",
    author_email="lavishgupta613@gmail.com",
    install_requires=["gemini","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)
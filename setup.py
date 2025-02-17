from setuptools import setup, find_packages

setup(
    name="tennis_booking",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "streamlit>=1.32.0",
        "langchain>=0.1.0",
        "langchain-core>=0.1.22",
        "langchain-community>=0.0.10",
        "langchain-openai>=0.0.2.post1",
        "openai>=1.6.1",
        "python-dotenv>=1.0.1",
        "pydantic>=2.0.0",
        "dateparser>=1.2.0",
        "typing-inspect>=0.9.0",
        "typing_extensions>=4.7.0",
        "pandas>=1.3.0",
        "plotly>=5.0.0",
        "yfinance>=0.2.0",
        "pandas-datareader>=0.10.0",
        "prophet>=1.1.0"
    ],
    description="A tennis court booking assistant with natural language processing",
    author="varrek",
    author_email="",
    url="https://github.com/varrek/nlp_tennis_courte_booking",
    include_package_data=True,
    zip_safe=False,
) 
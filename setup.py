from setuptools import setup, find_packages

setup(
    name="tennis_booking",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit==1.32.0",
        "langchain==0.1.12",
        "langchain-openai==0.0.8",
        "python-dotenv==1.0.1",
        "pydantic>=2.6.4,<3.0.0",
        "pydantic-core>=2.16.3",
        "dateparser==1.2.0",
        "typing-inspect>=0.9.0",
        "typing_extensions>=4.5.0"
    ],
    python_requires=">=3.8,<3.12",
    description="A tennis court booking assistant with natural language processing",
    author="varrek",
    author_email="",
    url="https://github.com/varrek/nlp_tennis_courte_booking",
) 
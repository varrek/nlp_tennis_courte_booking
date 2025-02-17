from setuptools import setup, find_packages

setup(
    name="tennis_booking",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit==1.32.0",
        "langchain==0.0.350",
        "langchain-core==0.1.22",
        "langchain-community==0.0.10",
        "langchain-openai==0.0.2.post1",
        "openai==1.6.1",
        "python-dotenv==1.0.1",
        "pydantic==1.10.13",
        "dateparser==1.2.0",
        "typing-inspect>=0.9.0",
        "typing_extensions>=4.5.0"
    ],
    python_requires=">=3.10,<3.12",
    description="A tennis court booking assistant with natural language processing",
    author="varrek",
    author_email="",
    url="https://github.com/varrek/nlp_tennis_courte_booking",
) 
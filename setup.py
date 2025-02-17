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
        "pydantic==2.6.4",
        "dateparser==1.2.0"
    ],
    python_requires=">=3.8",
) 
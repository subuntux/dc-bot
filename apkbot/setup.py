from setuptools import setup, find_packages

setup(
    name="apkbot",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "discord.py",  # Stelle sicher, dass du alle benötigten Abhängigkeiten auflistest.
    ],
    # Weitere Metadaten wie Autor, Beschreibung, etc.
)

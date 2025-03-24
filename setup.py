from setuptools import setup

# Load README.md content
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="catfiles",
    version="0.1.0",
    py_modules=["catfiles"],
    entry_points={
        "console_scripts": [
            "catfiles = catfiles:main",
        ],
    },
    install_requires=[
        "pyperclip"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",  # important if using Markdown
)
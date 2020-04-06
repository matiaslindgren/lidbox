import setuptools

with open("README.md") as f:
    readmefile_contents = f.read()

setuptools.setup(
    name="lidbox",
    version="0.4.0",
    description="Command line toolbox for end-to-end speech classification experiments.",
    long_description=readmefile_contents,
    long_description_content_type="text/markdown",
    author="Matias Lindgren",
    author_email="matias.lindgren@gmail.com",
    license="MIT",
    python_requires=">= 3.7.*",
    install_requires=[
        "PyYAML ~= 5.1",
        "jsonschema",
        "kaldiio ~= 2.13",
        "librosa ~= 0.7",
        "matplotlib ~= 3.1",
        "webrtcvad ~= 2.0.10",
    ],
    packages=[
        "lidbox",
        "lidbox.dataset",
        "lidbox.features",
        "lidbox.models",
        "lidbox.schemas",
    ],
    entry_points={
        "console_scripts": [
            "lidbox = lidbox.__main__:main",
        ],
    },
)

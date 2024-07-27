import setuptools

with open("READ.md", 'r', encoding='utf-8') as f:
    long_descrip = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney_Disease_Classification-MLflow-DVC"
AUTHOR_USER_NAME = 'dipesh4568'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'dipesh.ghiyal8@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="END TO END DEEP LEARNING PROJECT",
    long_description=long_descrip,
    long_description_content='text/markdown',
    url=f'https'
)
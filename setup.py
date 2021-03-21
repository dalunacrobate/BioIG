from setuptools import setup, find_packages


setup(
    name='bioig',
    version="1.0",
    packages=find_packages(),
    author="Dalunacrobate",
    install_requires=["requests","bs4"],
    description="BioAnalyzer is a module that allows you to extract personnals informations from an instagram profile bio such as : Religion, Hobbies, Ethnicity, Emails, Paypal.me/, Snapchat, Twitter, Best Friends, Age, Location, Love Relationship, Love Relationship date, Facebooks, Astrologic Sign, Sexuality.",
    include_package_data=True,
    url='https://github.com/dalunacrobate/BioIG',
    entry_points = {'console_scripts': ['BioIG = BioIG.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
from setuptools import setup, find_packages

setup(
    name                = 'ypcc',
    version             = '0.6.3',
    long_description    = 'Hello. This is ypcc.',
    description         = 'ccpy',
    license             = 'MIT',
    author              = 'jeakwon',
    author_email        = 'onlytojay@gmail.com',
    url                 = 'https://github.com/jeakwon/ypcc',
    download_url        = 'https://github.com/jeakwon/ypcc/archive/0.0.tar.gz',
    install_requires    = [
        "numpy < 1.15"
    ],
    packages            = find_packages(exclude = []),
    keywords            = ['ypcc'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

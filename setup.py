import setuptools

setuptools.setup(
    name='badge',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)

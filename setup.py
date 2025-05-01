from setuptools import setup, find_packages

setup(
    name='python3-boleto',
    version='1.0.0',
    author='Alexandre Ferreira (fork de Trust-Code)',
    author_email='alexandreferreira.cont@outlook.com',
    url='https://github.com/Alexandre-Dev1010/python-boleto',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pyboleto': ['media/*.jpg', 'media/*.png', 'templates/*.html'],
        'tests': ['xml/*.xml'],
    },
    license='BSD',
    description='Biblioteca Python para geração de boletos bancários para diversos bancos brasileiros.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: Financial',
        'Framework :: Django',
    ],
    install_requires=[
        'reportlab'
    ],
    python_requires='>=3.6',
)

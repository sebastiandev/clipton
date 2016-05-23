from setuptools import setup


# Dynamically calculate the version based on clipton.VERSION.
setup(
    name='clipton',
    version=__import__('clipton').__version__,
    url='https://github.com/sebastiandev/clipton',
    author='Sebastian Packmann',
    author_email='devsebas@gmail.com',
    description=('A cross-platform clipboard for Python'),
    license='MIT',
    packages=['clipton'],
    test_suite='',
    keywords="clipboard test testing automation",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

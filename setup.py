from setuptools import setup

setup(
    name='pygks',
    version=__import__('pygks').__version__,
    url='https://github.com/b1015062Furukawa/pygks.git',
    author='Akiya Furukawa',
    author_email='akiya.noface@gmail.com',
    maintainer='Akiya Furukawa',
    maintainer_email='akiya.noface@gmail.com',
    description=('A module for calling GetKeyState easily'),
    license='MIT',
    packages=['pygks'],
    keywords="keyboard win32",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)

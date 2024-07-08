import os

from setuptools import setup


def read_md(f):
    with open(f, encoding='utf8') as fin:
        return fin.read()


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_reqs(fn):
    return [_.strip() for _ in open(os.path.join(CURRENT_DIR, fn), encoding='utf8').readlines() if _.strip() and not _.strip().startswith('#')]


setup(
    name="edgetest",
    version='0.1.1',
    scripts=['edgetest'],
    author="Chris Spencer",
    author_email="cspencer@edgeondemand.com",
    description="Test running tool.",
    long_description=read_md('README.md'),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/Edge-On-Demand/edgetest",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
    zip_safe=False,
)

from setuptools import setup, find_packages

import subprocess


def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse',
                                    'HEAD']).decode("utf-8").strip(' \n')


git_sha1 = get_git_revision_hash()

with open('kk_test/__init__.py', 'a') as f:
    f.write(f"__git_sha1__ = '{git_sha1}'\n")

setup(
    name='kk_test',
    author='Fangjun Kuang',
    author_email='csukuangfj@gmail.com',
    description='Test Python setup.py',
    packages=find_packages(),
    url='https://github.com/csukuangfj/kk_test.git',
    version='1.0.0',
)

with open('kk_test/__init__.py', 'r') as f:
    lines = f.readlines()

with open('kk_test/__init__.py', 'w') as f:
    for line in lines:
        if '__git_sha1__' not in line:
            f.write(line)

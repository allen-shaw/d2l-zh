from setuptools import setup, find_packages
import d2l

requirements = [
    'jupyter',
    'numpy',
    'matplotlib',
    'requests',
    'pandas'
    # 'jupyter==1.0.0',
    # 'numpy==1.24.4',
    # 'matplotlib==3.5.1',
    # 'requests==2.25.1',
    # 'pandas==1.4.4'
]

setup(
    name='d2l',
    version=d2l.__version__,
    python_requires='>=3.5',
    author='D2L Developers',
    author_email='d2l.devs@gmail.com',
    url='https://d2l.ai',
    description='Dive into Deep Learning',
    license='MIT-0',
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements,
)

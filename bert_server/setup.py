from setuptools import find_packages, setup
setup(
    name='bert_sample',
    version='0.0.0.1',
    description='bert基本操作',
    long_description=open('README.md', 'r').read(),
    author='Terry Chan',  # 作者
    author_email='napoler2008@gmail.com',
    url='https://www.terrychan.org',
    # packages=find_packages(),
    packages=['bert_sample'],  # 这里是所有代码所在的文件夹名称
    install_requires=[
        'numpy',
        'flask',
        'tqdm',
        'Terry_toolkit',
        'pytorch_pretrained_bert',
        'torch'


    ]



    )

# python setup.py sdist
# #python setup.py install
# python setup.py sdist upload

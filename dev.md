
## 提交包
python3 setup.py sdist
# #python3 setup.py install
python3 setup.py sdist upload


## 构建文档
```
mkdir docs
cd docs
sphinx-quickstart
cd ../

sphinx-apidoc -f -o docs/source/ src --ext-autodoc -e


sphinx-apidoc -f -o docs/source/ src --ext-autodoc -e --ext-githubpages --ext-viewcode --ext-todo
```

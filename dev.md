## 运行docker

https://github.com/napoler/Docker-pytorch-pretrained-BERT


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

sphinx-apidoc -f -o docs/source/ src/pytorch_pretrained_bert/ --ext-autodoc -e

# 更多的信息生成
sphinx-apidoc -f -o docs/source/ src/pytorch_pretrained_bert/ --ext-autodoc -e --ext-githubpages --ext-viewcode --ext-todo

## jupyter

jupyter notebook --generate-config

jupyter notebook password


jupyter notebook --ip=0.0.0.0 --port=5000 --allow-root --browser="UTF-8" --config=/workspace/conf/jupyter/jupyter_notebook_config.py

jupyter notebook -h


jupyter notebook --allow-root --config=/workspace/conf/jupyter/jupyter_notebook_config.py




export LC_ALL=$(locale -a | grep UTF-8)

```

## 修复权限

 chmod 777 -R ./* 

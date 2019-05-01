 
git clone https://gitee.com/terrychan/apex.git && cd apex && python setup.py install --cuda_ext --cpp_ext

## 运行docker

https://github.com/napoler/Docker-pytorch-pretrained-BERT

## 创建虚拟环境
创建
python3 -m venv 项目目录
激活
source 项目目录/bin/activate
退出
deactivate

## 提交包
python3 setup.py sdist
# #python3 setup.py install
python3 setup.py sdist upload

## 监视显卡使用情况
watch -n 10 nvidia-smi

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

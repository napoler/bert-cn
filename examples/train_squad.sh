# SQUAD_DIR=/raid/qsj/pytorch-pretrained-BERT/data/SQuAD

# python run_squad.py \
#   --bert_model bert-base-uncased \
#   --do_train \
#   --do_predict \
#   --train_file $SQUAD_DIR/train-v1.1.json \
#   --predict_file $SQUAD_DIR/dev-v1.1.json \
#   --train_batch_size 12 \
#   --learning_rate 3e-5 \
#   --num_train_epochs 2.0 \
#   --max_seq_length 384 \
#   --doc_stride 128 \
#   --output_dir /raid/qsj/pytorch-pretrained-BERT/checkpoints/squad



rm -rf ../data/squad1
mkdir ../data/squad1
rm -rf ../data/squad_cn/squad_dev.json_*
#!export SQUAD_DIR=./BERT-for-Chinese-Question-Answering-master/data/squad_cn

# bert-base-chinese

python3 run_squad_cn_62.py  --bert_model ../data/model_cn/ --do_train   --do_predict  --train_file ../data/squad_cn/squad_dev.json --predict_file ../data/squad_cn/squad_train.json  --train_batch_size 12  --learning_rate 3e-5   --num_train_epochs 2   --max_seq_length 384   --doc_stride 128   --output_dir ../data/squad1
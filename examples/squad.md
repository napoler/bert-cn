SQuAD
This example code fine-tunes BERT on the SQuAD dataset. It runs in 24 min (with BERT-base) or 68 min (with BERT-large) on a single tesla V100 16GB.

The data for SQuAD can be downloaded with the following links and should be saved in a $SQUAD_DIR directory.

train-v1.1.json
dev-v1.1.json
evaluate-v1.1.py
export SQUAD_DIR=/workspace/data/corpus/SQuAD/


```
python run_squad.py \
  --bert_model bert-base-uncased \
  --do_train \
  --do_predict \
  --do_lower_case \
  --train_file $SQUAD_DIR/train-v1.1.json \
  --predict_file $SQUAD_DIR/dev-v1.1.json \
  --train_batch_size 12 \
  --learning_rate 3e-5 \
  --num_train_epochs 2.0 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --output_dir /workspace/data/corpus/SQuAD/debug_squad/
  
  ```
Training with the previous hyper-parameters gave us the following results:

{"f1": 88.52381567990474, "exact_match": 81.22043519394512}
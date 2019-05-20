from pytorch_pretrained_bert import WEIGHTS_NAME, CONFIG_NAME

output_dir = "/home/terry/pan/github/bert/model/bert-base-chinese/"

# Step 1: Save a model, configuration and vocabulary that you have fine-tuned
import os

import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM,BertForNextSentencePrediction

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

#model = BertModel.from_pretrained('bert-base-chinese')

model = BertForNextSentencePrediction.from_pretrained('bert-base-chinese')

# If we have a distributed model, save only the encapsulated model
# (it was wrapped in PyTorch DistributedDataParallel or DataParallel)
model_to_save = model.module if hasattr(model, 'module') else model

# If we save using the predefined names, we can load using `from_pretrained`
output_model_file = os.path.join(output_dir, WEIGHTS_NAME)
output_config_file = os.path.join(output_dir, CONFIG_NAME)

torch.save(model_to_save.state_dict(), output_model_file)
model_to_save.config.to_json_file(output_config_file)
tokenizer.save_vocabulary(output_dir)

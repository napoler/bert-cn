import subprocess
import Terry_toolkit as tkit


model_path ="/home/terry/pan/github/bert/test/"
#corpus_path ="/home/terry/pan/github/bert/book/"
corpus_path ="/home/terry/pan/github/bert/test/book/"
training_path="/home/terry/pan/github/bert/training"
epochs='30'
max_seq_len ="128"

tfile=tkit.File()
corpu_list= tfile.file_List(corpus_path,'txt')

for item in corpu_list:
  print("开始处理: "+item)



  cmd = "python3 pregenerate_training_data.py --train_corpus "+item+"  --bert_model "+model_path+"last/ --do_lower_case --output_dir /home/terry/pan/github/bert/training/ --epochs_to_generate "+epochs+" --max_seq_len "+max_seq_len

  print(subprocess.call(cmd, shell=True))

  #移除已经训练的数据
 # cmd = "python3 pregenerate_training_data.py --train_corpus "+item+"  --bert_model "+model_path+"last/ --do_lower_case --output_dir /home/terry/pan/github/bert/training/ --epochs_to_generate "+epochs+" --max_seq_len "+max_seq_len+"

  #print(subprocess.call(cmd, shell=True))

  cmd_run="python3 finetune_on_pregenerated.py --pregenerated_data "+training_path+" --bert_model "+model_path+"last/ --do_lower_case --output_dir "+model_path+"temp/ --epochs "+epochs+" --no_cuda"


  print(subprocess.call(cmd_run, shell=True))




  cmd_mv="mv "+model_path+"temp/* "+model_path+"last/"


  print(subprocess.call(cmd_mv, shell=True))

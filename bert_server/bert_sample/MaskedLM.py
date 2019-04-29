import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM
from Terry_toolkit import Text
#进度条显示
from tqdm import tqdm
import numpy as np
from random import *
class MaskedLM:
    def __init__(self):
        print('start MaskedLM')
        # self.tokeniser = BertTokenizer.from_pretrained(model)
        # self.model = BertForMaskedLM.from_pretrained(model)
    def model_init(self,model='bert-base-chinese'):
        """
        这里进行手动初始化模型
        
        """
        self.tokeniser = BertTokenizer.from_pretrained(model)
        self.model = BertForMaskedLM.from_pretrained(model)
    def sentence_pre(self,text1,text2 ):
        """
        进行句子预处理
        返回为

        >>> sentence_pre(text1,text2 ):
        
        """

        text1='[CLS] '+text1+' [SEP] '
        text2=text2+' [SEP] '
        text = text1+' '+text2
        # text = "[CLS] Do you like me ?  [SEP]  No  [SEP]"


        tokenized_text1 = self.tokeniser.tokenize(text1)
        tokenized_text2 = self.tokeniser.tokenize(text2)
        tokenized_text = self.tokeniser.tokenize(text)

        for i in range(len(tokenized_text1)+3,len(tokenized_text1)+5):
            tokenized_text[i] = '[MASK]'
        print('tokenized_text\n',tokenized_text)
        # Convert token to vocabulary indices
        #给单词标号
        indexed_tokens = self.tokeniser.convert_tokens_to_ids(tokenized_text)
        print('indexed_tokens\n',indexed_tokens)
        print('indexed_tokens \n',len(indexed_tokens))
        segments_ids =[0]*len(tokenized_text1)+[1]*len(tokenized_text2)

        print('segments_ids长度 \n',len(segments_ids))

        return indexed_tokens,segments_ids
    # def count_of(self,num,segments_ids):
    #     """
    #     返回数组中某一元素的个数

    #     >>> count_of(num,segments_ids)
        
    #     """
    #     # print('segments_ids',segments_ids)
    #     # list_a = [num for x in segments_ids]
    #     # print(list_a)
    #     a_count = segments_ids.count(num)
    #     return a_count
    #     # print(a_count)
        

    def prediction(self,indexed_tokens,segments_ids):
        
        # Convert inputs to PyTorch tensors
        tokens_tensor = torch.tensor([indexed_tokens])
        # print('编码后的语句信息')
        # print('tokens_tensor\n',tokens_tensor)
        segments_tensors = torch.tensor([segments_ids])
        # print('分句标记信息')
        # print('segments_tensors \n',segments_tensors)
        
        with torch.no_grad():
            predictions = self.model(tokens_tensor, segments_tensors)
            print('predictions\n',predictions)
        tokeniser=self.tokeniser
        list1=segments_ids.count(0)
        print('list1',list1)
        list2=segments_ids.count(1)
        remove_predicted_ids=[0,list1-1,list2-1]

        text_new=''
        text_new1=''
        for i in range(0,len(segments_ids)-1):
            print(i)
            #删除掉首个和断句字符的影响
            if i in remove_predicted_ids:
                continue
            
            

            #   print('segments_ids',segments_ids)
            
            predicted_index = torch.argmax(predictions[0, i]).item()
            print('predicted_index',predicted_index)
            predicted_tokens = tokeniser.convert_ids_to_tokens([predicted_index])

            print('predicted_tokens',predicted_tokens)
            # print('predicted_token',predicted_token)

            if i<list1:
                
                text_new=text_new+''+str(predicted_tokens[0])
            else:
                text_new1=text_new1+''+str(predicted_tokens[0])

        return text_new,text_new1

   
    # def text_to_array(self,text):
    #     """
    #     文字分句,文本转换成数组

    #     >>> text_to_array(text)

    #     """
    #     t=Text()
    #     data= t.sentence_segmentation(text)
    #     return data

# mlm=MaskedLM()
# #初始化模型
# mlm.model_init()
# text1="今天天气好吗 "
# text2="估计n牛错。"
# indexed_tokens,segments_ids= mlm.sentence_pre(text1,text2)
# # print(t)
# text_new,text_new1=mlm.prediction(indexed_tokens,segments_ids)
# print('text1',text1)
# print('t new',text_new)
# print('text2',text2)
# print('tnew1',text_new1)



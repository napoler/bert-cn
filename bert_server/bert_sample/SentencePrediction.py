import torch
from pytorch_pretrained_bert import BertTokenizer, BertForNextSentencePrediction
from Terry_toolkit import Text
#进度条显示
from tqdm import tqdm
import numpy as np
from random import *
import multiprocessing as mp
import gc
class SentencePrediction:
    def __init__(self,model='bert-base-chinese'):
        print('start NextSentence')
#         self.tokeniser = BertTokenizer.from_pretrained(model)
#         self.model = BertForNextSentencePrediction.from_pretrained(model)
    def model_init(self,model='bert-base-chinese'):
        """
        初始化模型内容
        
        >>> model_init(model='bert-base-chinese')
        
        """
        self.tokeniser = BertTokenizer.from_pretrained(model)
        self.model = BertForNextSentencePrediction.from_pretrained(model)
        self.model.eval()
        if torch.cuda.is_available():

            self.dirve ='cuda'
        else:
            self.dirve ='cpu'
        print('use ',self.dirve)
        
        self.model.to(self.dirve)
    def free_ram(self):
        """
        这里进行手动初始化模型
        
        """
        del self.tokeniser
        del self.model
        gc.collect()
        torch.cuda.empty_cache()
        print('已经释放模型内存')
    def one_sentence(self,data,previous_line):
        """
        文字数组中最符合的下一行

        返回内容为数组



        >>> one_sentence(text_array,previous_line)

        >>> one_sentence(text_array,previous_line)

        """
        # items = np.array([['line_number','prediction','text']])
#         items = np.dtype([('line_number', int ),('prediction',  'S10'),('prediction',  'S10')])
        items=[]
        # print(len(data))
        data_len=len(data)
        for line_number in tqdm(range(0, data_len-1)):
            print('line_number',line_number)

            #选取需要检测的内容
            line_to_check = data[line_number]
            #检查是否是相关
            next_line_prediction=self.predictions_check(previous_line,line_to_check)
            line={
                'line_number':line_number,
                'line_to_check':line_to_check,
                'next_line_prediction':next_line_prediction


            }
#             print('line_to_check',line_to_check)
#             print('相关性指数',next_line_prediction)
            # item = np.array([[line_number,line_to_check,next_line_prediction]])
            # try:
            #     items=np.r_[items,item]
            # except:
            #     items= item
            items.append(line)
            
        print('items',items)
        return items

        #基于最后一个数据排序
        # items=items[np.lexsort(items.T)]

        #倒序输出
        # return np.flipud(items)

#         pass
    def predictions_check(self,previous_line,line_to_check):

            """
            检查两个语句是否是相似

            >>> predictions_check(previous_line,line_to_check)

            """


            len_line_1 = len(self.tokeniser.tokenize(previous_line))
            len_line_2 = len(self.tokeniser.tokenize(line_to_check))

            text = previous_line + ' ' + line_to_check

                #         print('text',text)
            tokenized_text = self.tokeniser.tokenize(text)
            #         print('tokenized_text',tokenized_text)

            indexed_tokens = self.tokeniser.convert_tokens_to_ids(tokenized_text)

            segments_ids = ([0] * len_line_1) + ([1] * len_line_2)
            tokens_tensor = torch.tensor([indexed_tokens]).to(self.dirve)
            segments_tensors = torch.tensor([segments_ids]).to(self.dirve)
            #         print('tokens_tensor',tokens_tensor)
            #         print('segments_tensors',segments_tensors)
            #这里使用模型进行预测
            predictions = self.model(tokens_tensor, segments_tensors)

            next_line_prediction = predictions[0,0].item()

            return next_line_prediction
    def text_to_array(self,text):
        """
        文字分句,文本转换成数组

        >>> text_to_array(text)

        """
        t=Text()
        data= t.sentence_segmentation(text)
        return data
    def sentence(self,text,previous_line):
        """
        获取文本中每句的可能性

        >>> sentence(text,previous_line)

        >>> sentence(text,previous_line)

        """
        paragraph_array=self.text_to_array(text)
        next_line=self.one_sentence(paragraph_array,previous_line)
        return next_line


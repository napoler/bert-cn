import gc
from sys import getrefcount
import resource
from functools import partial

import multiprocessing as mp
from flask import Flask, render_template, request, json, Response, jsonify
from bert_sample import SentencePrediction,MaskedLM
from flask_ngrok import run_with_ngrok
# import numba
# from numba import jit, njit, prange, config, generated_jit


app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


 
def mem():
    print('Memory usage         : % 2.2f MB' % round(
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0,1)
    )

 
def get_post_data():
    """
    从请求中获取参数
    :return:
    """
    data = {}
    if request.content_type.startswith('application/json'):
        data = request.get_data()
        data = json.loads(data)
    else:
        for key, value in request.form.items():
            if key.endswith('[]'):
                data[key[:-2]] = request.form.getlist(key)
            else:
                data[key] = value
    return data

@app.route("/")
def hello():
    return "Bert 中文测试!"

@app.route("/tools/sentence/prediction")
 
def tools_sentence_prediction():
    return render_template("tools_sentence_prediction.html",**locals())
    
@app.route("/json/sentence/prediction" ,methods=['GET', 'POST'])
def json_sentence_prediction():
    data= get_post_data()
    print('data',data)
    # paragraph = request.args.get('text')
    # previous_line=request.args.get('sentence')
    paragraph = data['text']
    previous_line = data['sentence']
    print('paragraph',paragraph)
    print('previous_line',previous_line)
    
    if paragraph and previous_line:
        nextS=SentencePrediction()
        nextS.model_init()
        next_line=nextS.sentence(paragraph,previous_line)

        #释放内存
        nextS.free_ram()
        del nextS
        gc.collect()
        # print(len(next_line))
        # print('next_line',next_line[:10])
        # data=next_line[:10].tolist()
        data={'data':next_line}

        data['msg']='返回预测结果'
    else:
        data={'msg':'数据不完整'}


    return jsonify(data)
    # return "Hello World!"


@app.route("/tools/sentence/gaicuo")
def tools_sentence_gaicuo():
    return render_template("tools_sentence_gaicuo.html",**locals())

#改错
@app.route("/json/sentence/gaicuo" ,methods=['GET', 'POST'])
def json_sentence_gaicuo():
    data= get_post_data()
    print('data',data)
    # paragraph = request.args.get('text')
    # previous_line=request.args.get('sentence')
    text1 = data['text1']
    text2 = data['text2']
    # print('paragraph',paragraph)
    # print('previous_line',previous_line)
    
    if text1 and text2:

        text_new,text_new1=mlm(text1,text2)
        # p = mp.Pool(1)
        # prod_x=partial(mlm, text2=text2) # prod_x has only one argument x (y is fixed to 10) 
        # text_new,text_new1 = p.map(prod_x,text1)
        # print rslt
#         print(getrefcount(mlm))
        # print(len(next_line))
        # print('next_line',next_line[:10])
        # data=next_line[:10].tolist()

        data={'data':{
            'text_new':text_new,
            'text_new1':text_new1

        }
        
        }

        data['msg']='返回预测结果'
    else:
        data={'msg':'数据不完整'}

    gc.collect()
    return jsonify(data)
    # return "Hello World!"
 
def mlm(text1,text2):
    print(text1,text2)
    mem()
    # nextS=SentencePrediction()
    # next_line=nextS.sentence(paragraph,previous_line)
    mlm=MaskedLM()
    #初始化模型
    mlm.model_init()
    # text1="今天天气好吗 "
    # text2="估计n牛错。"
    indexed_tokens,segments_ids= mlm.sentence_pre(text1,text2)
    
    # print(t)
    text_new,text_new1=mlm.prediction(indexed_tokens,segments_ids)
    #释放内存
#         mlm.free_ram()
    print('getrefcount(mlm)',getrefcount(mlm))
    #释放显存
    # mlm.clear()
    # # mlm.free_ram()
    mem()
    del mlm
    gc.collect()
    mem()
    
    return text_new,text_new1

if __name__ == "__main__":
    app.run()
#     app.run(
#          host='0.0.0.0',
#          port=8110,
#       #   debug=True
#          )

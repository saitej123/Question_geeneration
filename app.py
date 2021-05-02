import os
import numpy as np
import pandas as pd
import joblib
from joblib import load
import streamlit as st
import _pickle as pickle
from pprint import pformat
from PIL import Image
import markdown
import requests
import json


def main():

        """SAI ML App """
        image = Image.open('sai_app_header.png')
        st.image(image,use_column_width=True)
        
        st.subheader("Question Generation model")
        context = st.text_area("Enter the context", '')
        answer = st.text_area("Enter the Answer", '')

        # fastapi endpoint
        url = 'https://question-generation-ifib6cnr6a-el.a.run.app'
        endpoint = '/getquestion'
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        def get_json(context,answer):
            dict_1={"context": context, "answer": answer}            
            return  json.dumps(dict_1)
                
        def process(context, answer, server_url: str):                 
            r = requests.post(server_url, headers=headers,data=get_json(context,answer))
            return r

        result = process(context,answer, url +endpoint)        
        if st.button('Generate question'):
            result = process(context,answer, url +endpoint)
                        
            if (result.status_code == 200):
                jsonDecoded = result.json()
                question=jsonDecoded["question"]
                st.balloons()
                st.text_area("Generated Question",question)







if __name__ == '__main__':
	main()
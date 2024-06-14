import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from text_utils import read_file
from text_utils import read_file,get_table_data
import streamlit as st
#from langchain.callbacks import get_openai_callback
from openai_utils import generate_evaluate_chain

from logger import logging

#loading the json file
with open(r"C:\Users\Hp\Desktop\MCQ_GEN\Response.json")  as file:
    RESPONSE_JSON=json.load(file)

#Create the title for the app
st.title("MCQ Application with LangChain")
#Create  form using st.form
with st.form("user-inputs") as file_upload:
    uploaded_file=st.file_uploader("Upload PDF file or txt file")
    #input field
    mcq_count=st.number_input("No of MCQs",min_value=3,max_value=20)
    # Add Button
    button=st.form_submit_button("Generate Questions")
    # Check if button is checked and all field have input
    if button and uploaded_file is not None and mcq_count:
        with st.spinner("Loading....") as spinner:
            try:
                text=read_file(uploaded_file)
                response=generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "Response_json": json.dumps(RESPONSE_JSON)
                    }
                )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")

            else:
                if isinstance(response,dict):
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                        else:
                            st.error("Error in table data")
                    else:
                        st.write(response)
import streamlit as st
from utils.st_def import st_logo, st_data_acquisition_contents

st_logo("Welcome 👋 to Data Acquisition!", "Data Acquisition")
st_data_acquisition_contents()
#-----------------------------------------------
from pathlib import Path

def create_file_list(directory, filter_str='*'):
  files = Path(directory).glob(filter_str)
  files_to_analyze = list(map(str, files))
  return files_to_analyze

corpus_dir = './data/books'

if st.button("List all the files we have:", type="primary", key = 'c1'):
    corpus_file_list = create_file_list(corpus_dir)
    st.write(corpus_file_list)

if st.button("List Austen's :", type="primary", key = 'c11'):
    austen_list = create_file_list(corpus_dir, 'austen*')
    st.write(austen_list)

if st.button("List Austen's Emma's first sentence:", type="primary", key = 'c12'):
    emmapath = create_file_list(corpus_dir, 'austen-emma*')[0]
    st.write(emmapath)

    preview_len = 290
    sentence = ""
    with open(emmapath, 'r') as f:
        emma_sent = f.read(preview_len)[50:preview_len]
    st.markdown(emma_sent)
    
    if 'emma_sent' not in st.session_state:   st.session_state['emma_sent'] = ''
    st.session_state['emma_sent'] = emma_sent
    # st.write(f"You entered: {st.session_state['article_content']}")



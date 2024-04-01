import spacy, streamlit as st
import en_core_web_sm
spacyt = spacy.load("en_core_web_sm")

class Our_Tokenizer:
  def __init__(self):
    #import spacy tokenizer/language model
    self.nlp = en_core_web_sm.load()
    self.nlp.max_length = 4500000 # increase max number of characters that spacy can process (default = 1,000,000)
  def __call__(self, document):
    tokens = self.nlp(document)
    return tokens

if 'emma_sent' not in st.session_state:   st.session_state['emma_sent'] = ''
st.write(f"You entered: {st.session_state['article_content']}")

tokens = spacyt(sentence)
for t in tokens:
 print(t.text)
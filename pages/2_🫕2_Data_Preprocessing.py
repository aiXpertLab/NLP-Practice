# st.session_state['frequency_table'] = frequency_table
import streamlit as st
from utils.st_def import st_logo, st_text_cleaning_contents

st_logo(title = "Welcome 👋 to Text Cleaning!", page_title="Text Cleaning",)
st_text_cleaning_contents()

#------------------------------------------------------------------------
from spacy.lang.en.stop_words import STOP_WORDS
import spacy, en_core_web_sm
spacyt = spacy.load("en_core_web_sm")

class Our_Tokenizer:
  def __init__(self):
    #import spacy tokenizer/language model
    self.nlp = en_core_web_sm.load()
    self.nlp.max_length = 4500000 # increase max number of characters that spacy can process (default = 1,000,000)
  def __call__(self, document):
    tokens = self.nlp(document)
    # return tokens
    simplified_tokens = [str.lower(token.lemma_) for token in tokens]
    return simplified_tokens


def main():
    if 'emma_sent' not in st.session_state:
      st.info("Click: 1 Local Data List first.")
    else:
      tokens = spacyt(st.session_state['emma_sent'])
      st.header("Tokenizer and Lemma:")
      for t in tokens:
        st.write(t.text)
        st.write(str.lower(t.lemma_))
    st.header("Stop words:")
    st.write(STOP_WORDS)


if __name__ == "__main__":
    main()

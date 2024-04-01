from pathlib import Path



def create_file_list(directory, filter_str='*'):
  files = Path(directory).glob(filter_str)
  files_to_analyze = list(map(str, files))
  return files_to_analyze

corpus_dir = './data/books'
corpus_file_list = create_file_list(corpus_dir)
austen_list = create_file_list(corpus_dir, 'austen*')
# print(austen_list)

preview_len = 290
emmapath = create_file_list(corpus_dir, 'austen-emma*')[0]
print(emmapath)
sentence = ""
with open(emmapath, 'r') as f:
  sentence = f.read(preview_len)[50:preview_len]
print(sentence)


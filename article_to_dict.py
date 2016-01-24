import cPickle as pickle

import sys

from nltk.tokenize import sent_tokenize


#usage, first arg is text file, second arg is title, third arg is url, fourth is output file name

wiki_file = sys.argv[1]
title = sys.argv[2]
url = sys.argv[3]
outfile_name = sys.argv[4]

fix_encoding = lambda s: s.decode('utf8', 'ignore')

wiki_file = open(wiki_file, 'rb')
wiki_text = wiki_file.read()
wiki_text = fix_encoding(wiki_text)

wiki_sentences = sent_tokenize(wiki_text)

wiki_dict = {'sentences':wiki_sentences, 'title':title, 'url':url}

pickle.dump(wiki_dict, open(outfile_name, 'wb'))

print 'Done!'
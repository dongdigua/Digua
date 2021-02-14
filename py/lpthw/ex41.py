import ramdom
from urllib.request import urlopen
import sys

WORD_URL = "http://learnpython3thehardway.org/words.txt"
WORDS = []

PHRASES = {
    
}
if len(sys.argv) ==2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRACE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf.8"))

def convert(snippet, phrase

#这代码毫无意义呀！不写了！











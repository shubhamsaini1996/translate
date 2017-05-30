from rapidconnect import RapidConnect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f=open("input.txt","r")

s=''
for i in f:
    for word in i:
        s=s+word
f.close()
print s

rapid = RapidConnect("go_591d954ee4b0959fdd12398f", "98df537b-0c0f-4670-b4e8-51865da4491b")

result = rapid.call('GoogleTranslate', 'translate', {
                    'apiKey': 'AIzaSyCvA9lwJ2pSdjrsA2rHR93I33k9mgYdjU4',
                    'string': s,
                    'targetLanguage': 'hi',
                    'sourceLanguage': 'en'
                    })
out=open("output","w")
out.write(result)
out.close()

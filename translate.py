#https://cloud.google.com/translate/docs/basic/translating-text?hl=vi#translate_text_with_model-python

import json
import codecs
import os

from google.cloud import translate_v2 as translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gg.json'
translate_client = translate.Client()
supportLanguage = ['ar','da', 'el', 'fa', 'fa', 'fr', 'he', 'id', 'ja', 'km', 'ko', 'lo', 'nl', 'zh', 'vi', 'de']

with open('en.json') as json_file:
    data = json.load(json_file)
    for lang in supportLanguage:
        output = {}
        for key,value in data.iteritems():
            translate = translate_client.translate(value, lang)['translatedText']
            print(translate)
            output[key] = translate
        with codecs.open('translated/{}.json'.format(lang), 'w', encoding='utf-8') as fp:
            json.dump(output, fp, ensure_ascii=False)
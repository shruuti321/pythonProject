

from bardapi import Bard
import json
# with open('cred.json','r') as f:
#     file=json.load(f)
#     token=file['token']
token='YAgcDEpAgj9kmEZoJ5Wer9g16M956cmuinxWWTczfigeULOOtcBj09zUOUqpEkkj47PI0g.'
bard = Bard(token=token)
response=bard.get_answer("What is Machine Learning")['content']
print(response)
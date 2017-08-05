import re
#import requests
#from mooc_chatbot.settings import BIDIRECTIONAL_API_LINK, DEVELOPMENT_PROXY
#import json

class Intelligence():
	def __init__(self,uname='buddy'):
		self.user_name = uname
		self.current_intent = 'default'
		self.response_dict = {'greeting':'Hey there {}! I am stupid chatbot'.format(self.user_name), 'end':'Ok bye! Hope to see you soon', 'weather':'IDK. LOL. Google it', 
		'undefined ques':'I am sorry I don\'t know the answer to that. Try posting it on the FAQ page.', 'affirmative':'ok great', 'negative':'well that\'s unfortunate', 
		'intro':'Ask me a question, I\'ll try my best to answer it.', 'unsatisfied':'Sorry to disappoint you. Try posting it on FAQ page', 'confirm':'Was my answer good enough?',
		'derogatory':'Why are you saying such things, you are making me cry', 'asked ques':'REDIRECT' }

		self.query_dict = {r'(^(?:h(?:ello+|ey+|i+)|ahoy|yo|bonjour|namaste))':'greeting', r'(bye|good\s?night|tata|ttyl|see\sy(?:a|ou))':'end',
			r'(no(?:pe)?|not\sgood)(\s|$)':'negative', r'(y(?:es|eah|a)|good|sure|ok(?:ay)?)(\s|$)':'affirmative'}

	def addResponse(self,intent,answer):
		if not response_dict.has_key(intent):
			response_dict[intent] = answer

	def reply(self, intent):
		if intent in self.response_dict.keys():
			if intent == 'asked ques':
				"""
				result = requests.get(BIDIRECTIONAL_API_LINK, params={'paragraph': topic_content, 'question':query_text}, proxies=DEVELOPMENT_PROXY)    
				# apply intelligence here to generate 'response'			   
				answer = json.loads(result.text)['result']
				# answer = " use bi-att-flow here "
				#if error occurs self.current_intent = 'undefined ques' and answer = None
				self.current_intent = 'confirm'
				return [answer, self.response_dict[self.current_intent]]
				"""
			self.current_intent = intent
			return [self.response_dict[intent]]

	def matchIntent(self,query):
		undef = True
		i = 'default'
		for reg in self.query_dict.keys():
			mo = re.search(reg,query,re.I)
			if mo:
				i = self.query_dict[reg]
				undef = False
				break

		if undef:
			i = 'asked ques'
		#conversation flow model
		if i == 'negative' and self.current_intent == 'confirm':
			i='unsatisfied'
		if i == 'greeting' and self.current_intent == 'greeting':
			i='intro'

		return i

	def replyToQuery(self,query):
		i = self.matchIntent(query)
		return self.reply(i)




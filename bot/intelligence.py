import re

class Intelligence():
	def __init__(self,uname):
		self.user_name = uname
		self.current_intent = 'default'
		self.response_dict = {'greeting':'Hey there {}! I am stupid chatbot'.format(self.user_name), 'end':'Ok bye! Hope to see you soon', 'weather':'IDK. LOL. Google it', 
		'undefined ques':'I am sorry I don\'t know the answer to that. Try posting it on the FAQ page.', 'affirmative':'ok great', 'negative':'well that\'s unfortunate', 
		'intro':'Ask me a question, I\'ll try to answer as much as I can.', 'unsatisfied':'Sorry to disappoint you. Try posting it on FAQ page', 'confirm':'Was my answer good enough?'
		'derogatory':'Why are you saying such things, you are making me cry', 'asked ques':'RE-DIRECT', }

		self.query_dict = {r'(^(?:h(?:ello+|ey+|i+)|ahoy|yo|bonjour|namaste))':'greeting', r'(bye|good\s?night|tata|ttyl|see\sy(?:a|ou))':'end',
			r'(y(?:es|eah|a)|good|sure|ok(?:ay)?)(\s|$)':'affirmative', r'(no(?:pe)?|not\sgood)(\s|$)':'negative',  }

	def addResponse(self,intent,answer):
		if not response_dict.has_key(intent):
			response_dict[intent] = answer

	def reply(self, intent):
		if response_dict.has_key(intent):
			self.current_intent = intent
			return response_dict[intent]

	def matchIntent(self,query):
		undef = True
		i = 'default'
		for reg in query_dict.keys():
			mo = re.search(reg,query,re.I)
			if mo:
				i = query_dict[reg]
				undef = False
				break

		if undef:
			i = 'asked ques'

		if i == 'negative' and self.current_intent == 'confirm':
			i='unsatisfied'

		return i

	def replyToQuery(self,query):
		i = self.matchIntent(query)
		if i == 'asked ques':
			""" use bi-att-flow here """
			# if error encountered i = undefined ques
			i = 'confirm'
		return self.reply(i)




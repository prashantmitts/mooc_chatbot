
class Intelligence():
	def __init__(self,uname):
		self.user_name = uname
		self.response_dict = {'greeting':'Hey there {}! I am stupid chatbot'.format(self.user_name), 'end':'Ok bye! Hope to see you soon', 'weather':'IDK. LOL. Google it', 
		'undefined ques':'I am sorry I don\'t know the answer to that. Try posting it on the FAQ page.', 'affirmative':'ok great', 'negative':'well nevermind', 
		'intro':'Ask me a question, I\'ll try to answer as much as I can.', 'unsatisfied':'Sorry to disappoint you. Try posting it on FAQ page', 'confirm':'Was my answer good enough'
		'derogatory':'Why are you saying such things, you are making me cry'}
		#self.query_dict = {}

	def addResponse(self,intent,answer):
		if not response_dict.has_key(intent):
			response_dict[intent] = answer

	def reply(self, intent):
		if response_dict.has_key(intent):
			return response_dict[intent]
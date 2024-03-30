from transformers import pipeline, Conversation
converse = pipeline("conversational", model="microsoft/DialoGPT-medium")

conversation_1 = Conversation("Want to learn Python, how?")
conversation_2 = Conversation("any website?")
conversation_3 = Conversation("what can i learn from it?")
conversation_4 = Conversation("is it easy to learn?")
conversation_5 = Conversation("how long will it take?")
print(converse([conversation_1, conversation_2, conversation_3, conversation_4, conversation_5]))
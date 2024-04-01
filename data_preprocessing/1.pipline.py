from transformers import pipeline, Conversation

conversation_1 = Conversation("Want to learn Python, how?")
conversation_2 = Conversation("any website?")
conversation_3 = Conversation("what can i learn from it?")
conversation_4 = Conversation("is it easy to learn?")
conversation_5 = Conversation("how long will it take?")

generator = pipeline("conversational", model="microsoft/DialoGPT-medium")
converse = generator(conversation_1, pad_token_id=generator.tokenizer.eos_token_id)
print(converse)
# print(converse([conversation_1, conversation_2, conversation_3, conversation_4, conversation_5]))

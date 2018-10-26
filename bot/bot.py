from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import winspeech
import speech_recognition as sr

r=sr.Recognizer()

#initializing speech recognizer
winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

#creating chat bot
bot=ChatBot('test')

#reading from file
conv=open('M.txt').readlines()

#bot training
bot.set_trainer(ListTrainer)

#trained for conversation
bot.train(conv)

#recognizing audio


while True:
	
    


	request=input('You: ')
	
	response=bot.get_response(request)
	winspeech.say(response)

#response of the bot
	print('Bot: ',response)
	

if result == 'Bye':
      winspeech.stop_listening()
      sys.exit(0)

#conversaation ends


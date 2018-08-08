from flask import Flask,request
app = Flask(__name__)

# import speech_recognition as sr
# r = sr.Recognizer()

# import assemblyai
# aai = assemblyai.Client(token='39f8f26db4c546c99308fba032eda3dd')

# , methods=["POST","GET"]

@app.route('/')
def example():
	# harvard = sr.AudioFile('house.wav')
	# with harvard as source:
 #  		audio = r.record(source)
	# text = r.recognize_google(audio)



	# f = request.files['file']
	# transcript = aai.transcribe(filename=f.filename)
	# while transcript.status != 'completed':
	# 	transcript = transcript.get()
	# text = transcript.text

	return "text"
app.run()



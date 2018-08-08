import os
from flask import Flask, request
app = Flask(__name__)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))




 # import speech_recognition as sr
# r = sr.Recognizer()
import assemblyai
aai = assemblyai.Client(token='39f8f26db4c546c99308fba032eda3dd')
@app.route('/', methods=["POST"])
def index():
	# harvard = sr.AudioFile('house.wav')
	# with harvard as source:
 #  		audio = r.record(source)
	# text = r.recognize_google(audio)
	# file = request.files['file']
	target = os.path.join(UPLOAD_FOLDER,'')

	if not os.path.isdir(target):
		os.mkdir(target)

	for f in request.files.getlist("file"):
		destination = "/".join([target,f.filename])
		f.save(destination)
		
		transcript = aai.transcribe(filename=f.filename)
		while transcript.status != 'completed':
			transcript = transcript.get()
		text = transcript.text
	return text


  
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	resp = MessagingResponse()

	resp.message("Thanks for the response.  We will get back to you shortly with more information")

	return str(resp)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run(debug=True)
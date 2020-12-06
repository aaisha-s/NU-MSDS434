from flask import Flask,render_template,request,url_for
#from google.cloud import automl
import sys
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1

project_id = 'nu-msds434'
model_id = 'TST4666162421537177600'

options = ClientOptions(api_endpoint='automl.googleapis.com')
prediction_client = automl_v1.PredictionServiceClient(client_options=options)

model_full_id = 'projects/755666330619/locations/us-central1/models/TST4666162421537177600'

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/results",methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        comment = request.form['comment']
        #data = [comment]
        text_snippet = automl_v1.TextSnippet(content=comment, mime_type="text/plain")
        payload = automl_v1.ExamplePayload(text_snippet=text_snippet)
        my_prediction = prediction_client.predict(name=model_full_id, payload=payload)
        
        return render_template('results.html',prediction = my_prediction,comment = comment)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

    

from flask import Flask, url_for, request, render_template
from flask import jsonify
from google.cloud import automl
import sys
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1 
#from google.cloud.automl_v1.proto import service_pb2

project_id = 'nu-msds434'
model_id = 'TST4666162421537177600'
#content = {{ user_comment }}

prediction_client = automl.PredictionServiceClient()

model_full_id = automl.AutoMlClient.model_path(
    project_id, "us-central", model_id
)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST', 'GET'])
def prediction():
    return render_template('results.html', sentPred = 1, content = 'yup')
'''
    if request.method == 'POST':
        commentInput = request.form
        for key, item in commentInput.items():
            text_snippet = automl.TextSnippet(
            content=item, mime_type="text/plain"
            )
        payload = automl.ExamplePayload(text_snippet=text_snippet)
        response = prediction_client.predict(name=model_full_id, payload=payload)
        
        for annotation_payload in response.payload:
            sentPred = annotation_payload.display_name
            break

        return render_template('results.html', sentPred = sentPred, content = content)
'''
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

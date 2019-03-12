import pickle    # Todo: consider joblib for scikit models instead
import flask
import pandas as pd

# Todo: consider extending to different formats, eg. byte streams

def run(model_file):

    app = flask.Flask(__name__)

    # load model
    print('Loading model')
    model = pickle.load(open(model_file, "rb"))

    @app.route('/ml-app/v1.0/predict/', methods=['POST'])
    def predict():
        '''
        Tasks to execute upon each API call
        :return: 
        '''

        if flask.request.method == 'POST':

            # try:
            data = flask.request.get_json()
            data = pd.read_json(data, orient='records')
            print('Input data:', data)

            # except ValueError:
            #     return flask.jsonify("Post request failed")

            print('Making predictions')
            prediction = model.predict(data)

            # preparing a response object and storing the model's predictions
            prediction_series = list(pd.Series(prediction))

            # sending our response object back as json
            responses = flask.jsonify(predictions=prediction_series.to_json(orient="records"))
            responses.status_code = 200

            return responses

    # start the API
    app.run(debug=True, port=5000)



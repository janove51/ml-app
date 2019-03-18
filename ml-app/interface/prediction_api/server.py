import pickle    # Todo: consider joblib for scikit models instead
import flask
import pandas as pd

# Todo: consider extending to different formats, eg. byte streams

def run(model_file, endpoint, probability = False, debug=True, port=5000):
    '''
    Starts server, exposing specific enpoint on specific port and loads scikit learn 
    model from pickled object into memory
    :param model_file: String, path to pickled model
    :param endpoint: String, example: /ml-app/v1.0/predict/
    :param probability: Boolean, whether scikit returns probability or not
    :param debug: Boolean, whether flask should run in debug mode or not
    :param port: Integer, Which port to choose
    :return: json, predictions and status code
    '''

    app = flask.Flask(__name__)

    # load model
    print('Loading model')
    model_metadata = pickle.load(open(model_file, "rb"))
    model = model_metadata['model']

    print('Making predictions using model with', model_metadata['accuracy'])

    @app.route(endpoint, methods=['POST'])
    def predict(model=model, probability=probability):
        '''
        Tasks to execute upon each API call
        :return: 
        '''

        if flask.request.method == 'POST':

            # try:
            data = flask.request.get_json()
            print('New input data:', data)

            data = pd.read_json(data, orient='records')


            if probability is False:
                prediction = model.predict(data)
            elif probability is True:
                prediction = model.predict_proba(data)

            # preparing a response object and storing the model's predictions
            prediction_series = pd.Series(prediction)

            # sending our response object back as json
            predictions = prediction_series.to_json(orient="records")
            print('predictions', predictions)
            responses = flask.jsonify(predictions)

            return responses

    # start the API
    app.run(debug=debug, port=port)



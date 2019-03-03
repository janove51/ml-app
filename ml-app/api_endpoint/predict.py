import pickle    # Todo: consider joblib for scikit models instead
import flask


def run_flask(model_file):

    app = flask.Flask(__name__)

    # load model
    model = pickle.load(open(model_file, "rb"))

    @app.route('/ml-app/v1.0/predict/', methods=['POST'])
    def predict():
        '''
        Tasks to execute upon each API call
        :return: 
        '''

        if flask.request.method == 'POST':

            try:
                data = flask.request.get_json()
                print('feature_array:', data['feature_array'])

            except ValueError:
                return flask.jsonify("Post request failed")

            prediction = model.predict(data['feature_array']).tolist()

            # preparing a response object and storing the model's predictions
            response = {}
            response['predictions'] = prediction

            # sending our response object back as json
            return flask.jsonify(response)

    # start the API
    app.run(debug=True, port=5000)

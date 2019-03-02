import pickle
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

        feature_array = flask.request.get_json()['feature_array']
        print('feature_array:', feature_array)
        prediction = model.predict([feature_array]).tolist()

        # preparing a response object and storing the model's predictions
        response = {}
        response['predictions'] = prediction

        # sending our response object back as json
        return flask.jsonify(response)


"""
How to run
$ export FLASK_APP=mock_ingest_feeds export FLASK_ENV=development flask run
"""

from flask import Flask, request, Response, make_response

import json

app = Flask(__name__)


@app.route('/netflix/feed', methods=['GET', 'POST'])
def netflix_feed():

    if request.method == 'GET':
        with app.open_resource('static/netflix/netflix_data_sources.json') as netflix_data_sources_json:
            netflix_data_sources = json.load(netflix_data_sources_json)

            return Response(json.dumps(netflix_data_sources))

@app.route('/netflix/data', methods=['GET', 'POST'])
def netflix_data():

    if request.method == 'GET':
        with app.open_resource('static/netflix/netflix_metadata.json') as netflix_metadata_json:
            netflix_metadata = json.load(netflix_metadata_json)

            return Response(json.dumps(netflix_metadata))


@app.route('/tenaa/feed', methods=['GET', 'POST'])
def tenaa_feed():
    count = request.args['count']
    start_index = request.args['startIndex']

    if request.method == 'GET':
        with app.open_resource('static/ten_aa_metadata.json') as ten_aa_metadata_json:
            ten_aa_metadata = json.load(ten_aa_metadata_json)
            ten_aa_metadata['itemCount'] = len(ten_aa_metadata["itemList"])

            return Response(json.dumps(ten_aa_metadata))


@app.route('/prime/feed', methods=['GET', 'POST'])
def prime_feed():

    if request.method == 'GET':

        amazon_feed_sources = {
            "metadata": ["http://127.0.0.1:5000/prime/meta"],
            "offers": ["http://127.0.0.1:5000/prime/offers"]
        }

        return Response(json.dumps(amazon_feed_sources))


@app.route('/prime/meta', methods=['GET', 'POST'])
def prime_meta():

    if request.method == 'GET':

        with app.open_resource('static/amazon_prime/prime_metadata.json') as prime_metadata_json:
            prime_metadata = json.load(prime_metadata_json)

            prime_metadata_string = '\n'.join([json.dumps(prime_item) for prime_item in prime_metadata])
            return Response(prime_metadata_string)


@app.route('/prime/offers', methods=['GET', 'POST'])
def prime_offers():

    if request.method == 'GET':
        with app.open_resource('static/amazon_prime/prime_offers.json') as prime_offers_json:
            prime_offers = json.load(prime_offers_json)

            prime_offers_string = '\n'.join([json.dumps(prime_offer) for prime_offer in prime_offers])
            return Response(prime_offers_string)


@app.route('/britbox/catalog', methods=['GET', 'POST'])
def britbox_catalog():

    if request.method == 'GET':
        with app.open_resource('static/britbox/britbox_metadata.json') as britbox_metadata_json:
            britbox_metadata = json.load(britbox_metadata_json)

            return Response(json.dumps(britbox_metadata))


@app.route('/britbox/availability', methods=['GET', 'POST'])
def britbox_availability():

    if request.method == 'GET':
        with app.open_resource('static/britbox/britbox_availability.json') as britbox_availability_json:
            britbox_availability = json.load(britbox_availability_json)
            britbox_availability['availability']['service']['totalItemCount'] = len(britbox_availability['availability']['service']['item'])

            return Response(json.dumps(britbox_availability))


@app.route('/acorntv/metadata', methods=['GET', 'POST'])
def acorntv_metadata():

    if request.method == 'GET':
        with app.open_resource('static/acorn_tv_metadata.json') as acorn_tv_metadata_json:
            acorn_tv_metadata = json.load(acorn_tv_metadata_json)

            return Response(json.dumps(acorn_tv_metadata))


@app.route('/disney_plus/feed', methods=['GET', 'POST'])
def disney_plus_feed():

    if request.method == 'GET':
        with app.open_resource('static/disney_plus_feed.json') as disney_plus_feed_json:
            disney_plus_feed = json.load(disney_plus_feed_json)

            return Response(json.dumps(disney_plus_feed))


@app.route('/hayu/feed', methods=['GET', 'POST'])
def hayu_feed():

    if request.method == 'GET':

        if request.args.get('test_number') == '1':
            # both items of the same series are missing their series title

            with app.open_resource('static/hayu/hayu_metadata_test_1.xml') as hayu_metadata_xml:
                return make_response(hayu_metadata_xml.read())

        if request.args.get('test_number') == '2':
            # both items of the same series have their series title, but one
            # is missing it's episode title

            with app.open_resource('static/hayu/hayu_metadata_test_2.xml') as hayu_metadata_xml:
                return make_response(hayu_metadata_xml.read())

        else:

            with app.open_resource('static/hayu/hayu_metadata.xml') as hayu_metadata_xml:
                return make_response(hayu_metadata_xml.read())


@app.route('/iwonder/feed', methods=['GET', 'POST'])
def iwonder_feed():

    if request.method == 'GET':

        if request.args.get('test_case') == "1":
            # skip item types feature and film that have no name (title)

            with app.open_resource('static/iwonder/iwonder_metadata_test_case_1.json') as iwonder_metadata_test_case_1_json:
                iwonder_metadata_test_case_1 = json.load(iwonder_metadata_test_case_1_json)
                return Response(json.dumps(iwonder_metadata_test_case_1))

        elif request.args.get('test_case') == "2":
            # item tv
            # skip processing the series item, but process the season(s) and episode(s) items

            with app.open_resource('static/iwonder/iwonder_metadata_test_case_2.json') as iwonder_metadata_test_case_2_json:
                iwonder_metadata_test_case_2 = json.load(iwonder_metadata_test_case_2_json)
                return Response(json.dumps(iwonder_metadata_test_case_2))

        elif request.args.get('test_case') == "3":
            # item tv
            # skip processing season items with missing name and/or season number

            with app.open_resource('static/iwonder/iwonder_metadata_test_case_3.json') as iwonder_metadata_test_case_3_json:
                iwonder_metadata_test_case_3 = json.load(iwonder_metadata_test_case_3_json)
                return Response(json.dumps(iwonder_metadata_test_case_3))

        elif request.args.get('test_case') == "4":
            # item tv
            # skip processing episode items with missing name and/or episode number

            with app.open_resource('static/iwonder/iwonder_metadata_test_case_4.json') as iwonder_metadata_test_case_4_json:
                iwonder_metadata_test_case_4 = json.load(iwonder_metadata_test_case_4_json)
                return Response(json.dumps(iwonder_metadata_test_case_4))

        else:

            with app.open_resource('static/iwonder/iwonder_metadata.json') as iwonder_metadata_json:
                iwonder_metadata = json.load(iwonder_metadata_json)
                return Response(json.dumps(iwonder_metadata))

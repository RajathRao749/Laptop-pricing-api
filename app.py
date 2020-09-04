from flask import Flask, jsonify,abort,make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    """
    This function is used to authorize the user
    """

    if username == 'rajath':
        return 'accept@error'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Restricted access!!!!!!'}), 403)

models = [
    {
        'name':'HP 14q cs2002TU',
        'processor':'1.1GHz Intel Celeron N4020 processor',
        'ram': '4GB DDR4 RAM',
        'display': '14-inch screen',
        'graphics':'Intel UHD  Graphics',
        'os': 'Windows 10 Home operating system',
        'weight':'1.47kg', 
        'cost':26000
    },
    {
        'name': 'ASUS VivoBook Ultra K14',
        'processor': '10th Gen Intel Core i3-10110U Processor, 2.1 GHz ',
        'ram':'4GB DDR4',
        'display':'14.0-inch (16:9) LED-backlit FHD (1920x1080) 60Hz Anti-Glare Panel with 45% NTSC',
        'graphics':'Integrated Intel UHD Graphics',
        'os':' Pre-loaded Windows 10 Home with lifetime validity',
        'weight':'1.40 kg',
        'cost':44990, 
    },
    {
        'name':'ASUS ZenBook 13',
        'processor':'10th Gen Intel Core i5-1035G1 Processor, 1.0 GHz ',
        'ram':'10th Gen Intel Core i5-1035G1 Processor, 1.0 GHz ',
        'display':'13.3-inch Full HD (1920 x 1080), 16:9 aspect, 300nits brightness, anti-glare panel',
        'graphics':' Integrated Intel UHD Graphics',
        'os':' Pre-loaded Windows 10 Home with lifetime validity',
        'weight':'1.11 kg',
        'cost':85500
    },
    {
        'name':'Alienware m15 ',
        'processor':'2.20GHz Intel Intel Core i7 8750H 8th Gen processor',
        'ram':'16GB DDR4 RAM',
        'display':'15.6-inch screen',
        'graphics':'Nvidia GE Force RTX 2070 8GB Graphics',
        'os':'Windows 10 with MS Office H&S 2019 operating system',
        'weight':'2.16kg',
        'cost':267898

    },
    {
        'name':'Lenovo Ideapad S540',
        'processor':'10th Generation Intel Core i7 10510U; Base Speed: 1.8Ghz, Max Speed: 4.9Ghz, 4 Cores, 8 Threads, 8 MB Smart Cache',
        'ram':'8 GB RAM',
        'display':'15.6-inch screen with (1920X1080) full HD display , Anti Glare technology , IPS Screen',
        'graphics':' NVIDIA MX250 2GB Graphics',
        'os':' Pre-loaded Windows 10 Home with lifetime validity',
        'weight':'1.8kg',
        'cost':84689
    }

]

@app.route('/electronics/laptop/models', methods=['GET'])
@auth.login_required
def get_tasks():
    """
    this function return all the models which are available
    """
    return jsonify({'models': models})

@app.route('/electronics/laptop/models/<int:price>',methods=['GET'])
@auth.login_required
def get_price(price):
    """
    this function return all the models which are less than or equal to the price specified by the user
    """
    prices = [mp  for mp in models if mp['cost']<=price]
    if len(prices)==0:
        abort(404)
    else:
        return jsonify({'price':prices})

@app.errorhandler(404)
def handle_error(error):
    return make_response(jsonify({'error':'please enter a range between 30000 - 300000'}),404)

if __name__ == '__main__':
    app.run(debug=True)

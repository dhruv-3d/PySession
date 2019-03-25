from flask import Flask, request
from flask import jsonify, render_template

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

@app.route('/', methods=['GET'])
def start_app():
    my_details = {
        'name': 'Dhruv Desai',
        'skills': ['Python', 'Javascript'],
        'education': 'B.Tech, Computer Engineering',
        'cgpa': 7.0,
        'interest': ['Graphics Designing', 'Lavara karva'],
        'email': 'dhruv_desai7@yahoo.com',
        'phone': 'nathi',
        'address': 'Surat, Gujarat',
    }

    return render_template('index.html', details=my_details)

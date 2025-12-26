from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

# Реквизиты храма для пожертвований
TEMPLE_REQUISITES = {
    'inn': '4020005692',
    'account_number': '40703810327000000178',
    'correspondent_account': '30101810100000000780',
    'bik': '042908780',
    'kpp': '402702001',
    'full_name': 'Архиерейское Подворье - Храм в Честь Казанской Иконы Пресвятой Богородицы в П. Октябрьский Ферзиковского района'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', section='about', requisites=TEMPLE_REQUISITES)

@app.route('/clergy')
def clergy():
    return render_template('about.html', section='clergy', requisites=TEMPLE_REQUISITES)

@app.route('/schedule')
def schedule():
    return render_template('about.html', section='schedule', requisites=TEMPLE_REQUISITES)

@app.route('/contacts')
def contacts():
    return render_template('about.html', section='contacts', requisites=TEMPLE_REQUISITES)

@app.route('/photos')
def photos():
    return render_template('about.html', section='photos', requisites=TEMPLE_REQUISITES)

@app.route('/shrines')
def shrines():
    return render_template('about.html', section='shrines', requisites=TEMPLE_REQUISITES)

@app.route('/donate')
def donate():
    return render_template('about.html', section='donate', requisites=TEMPLE_REQUISITES)

# Health check для мониторинга
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'temple-site',
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5001)
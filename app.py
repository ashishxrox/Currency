from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('file1.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        currency_code = request.form.get('currency').upper()
        api_url = f'https://restcountries.com/v3.1/currency/{currency_code}'
        response = requests.get(api_url)
        data = response.json()

        countries = []
        for country in data:
            name = country.get('name', {}).get('common', 'N/A')
            code = country.get('cca2', '')
            capital = country.get('capital', ['N/A'])[0]
            flag_class = f'flag-icon flag-icon-{code.lower()}'
            countries.append({'name': name, 'code': code, 'capital': capital, 'flag_class': flag_class})

        return jsonify({'success': True, 'countries': countries})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

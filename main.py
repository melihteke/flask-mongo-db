from flask import Flask, render_template, request
from mongodb_operations import MongoDBOperation

app = Flask(__name__)

mongo = MongoDBOperation()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        record = {
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        mongo.add_record(record)
        return render_template('record_added.html')
    return render_template('add_record.html')

@app.route('/remove_record', methods=['GET', 'POST'])
def remove_record():
    if request.method == 'POST':
        record_id = request.form['record_id']
        mongo.remove_record(record_id)
        return render_template('record_removed.html')
    return render_template('remove_record.html')

@app.route('/update_record', methods=['GET', 'POST'])
def update_record():
    if request.method == 'POST':
        record_id = request.form['record_id']
        updates = {
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        mongo.update_record(record_id, updates)
        return render_template('record_updated.html')
    return render_template('update_record.html')

@app.route('/view_all_records')
def view_all_records():
    records = mongo.view_all_records()
    return render_template('view_all_records.html', records=records)

@app.route('/view_specific_record', methods=['GET', 'POST'])
def view_specific_record():
    if request.method == 'POST':
        filters = {
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        records = mongo.view_specific_record(filters)
        return render_template('view_specific_record.html', records=records)
    return render_template('view_specific_record.html')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=8081)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vr-view')
def vr_view():
    room = request.args.get('room', '')
    res = request.args.get('res', 'low')
    return render_template('vr-view.html', room=room, res=res)

if __name__ == '__main__':
    app.run(debug=True)
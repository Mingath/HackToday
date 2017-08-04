from flask import Flask, request, render_template
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)
@app.route('/')
@app.route('/<index>')
def root(index="index.html"):
    return app.send_static_file(index)

@app.route('/static/css/')
@app.route('/static/css')
@app.route('/css')
@app.route('/css/')
def css():
    return 'one step closer'

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)
    
@app.route('/static/css/portal/')
@app.route('/static/css/portal')
def thi():
    return 'you got the portal, now use it'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
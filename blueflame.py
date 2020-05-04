from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    html = '''
        <!doctype html>
        <html>
            <head>
                <title>blueflame</title>
            </head>

            <style>
            .content {
            max-width: 1280px;
            margin: auto;
            background-color: black;
            }
            </style>

            <body class="content">
                <video width="100%" height="auto" autoplay loop>
                    <source src="./static/blueflame05.mp4" type="video/mp4">
                </video>
            </body>
        </html>
    '''
    return html
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

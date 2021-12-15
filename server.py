from flask import Flask, render_template,url_for,request
from cryption import FileEncyrption
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/',methods = ['POST'])
def my_link():
    data_cryptiption = FileEncyrption(request.form['filename'])
    if request.form['button'] == "encrypt":
        data_cryptiption.encrypt_file()
        return 'Crypted'
    elif request.form['button'] == "decrypt":
        data_cryptiption.decrypt_file()
        return 'Decrypted'
    

if __name__ == '__main__':
  app.run(debug=True)
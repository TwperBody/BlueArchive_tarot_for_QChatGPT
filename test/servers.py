# servers.py

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
import threading

app = Flask(__name__)

# 设置图片存储路径
app.config['UPLOADED_PHOTOS_DEST'] = 'image'

# 确保上传目录存在
if not os.path.exists(app.config['UPLOADED_PHOTOS_DEST']):
    os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

# 初始化文件编号
file_counter = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global file_counter
    file = request.files['photo']
    if file:
        new_filename = str(file_counter) + '.png'
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], new_filename))
        file_counter += 1
        return redirect(url_for('uploaded_file', filename=new_filename))
    return 'File upload failed'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

def run_server():
    app.run(host='0.0.0.0', port=1145, debug=True, use_reloader=False)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

# 设置图片存储路径
app.config['UPLOADED_PHOTOS_DEST'] = 'plugins/QChatGPT_BlueArchive_tarot/image'

# 确保上传目录存在
if not os.path.exists(app.config['UPLOADED_PHOTOS_DEST']):
    os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['photo']
    if file:
        # 生成数字文件名，例如：1.png, 2.png, ...
        new_filename = str(len(os.listdir(app.config['UPLOADED_PHOTOS_DEST'])) + 1) + '.png'
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], new_filename))
        return redirect(url_for('uploaded_file', filename=new_filename))
    return 'File upload failed'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1145, debug=True)  # 运行在端口1145

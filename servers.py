from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

# 设置图片存储路径
app.config['UPLOADED_PHOTOS_DEST'] = 'plugins/QChatGPT_BlueArchive_tarot/image'

# 设置模板文件夹路径
app.template_folder = 'plugins/QChatGPT_BlueArchive_tarot/templates'

# 确保上传目录存在
if not os.path.exists(app.config['UPLOADED_PHOTOS_DEST']):
    os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

# 初始化文件编号
file_counter = 0

@app.route('/')
def index():
    # 确保 index.html 文件位于正确的模板文件夹内
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global file_counter
    file = request.files['photo']
    if file:
        new_filename = str(file_counter) + '.png'
        file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], new_filename)
        file.save(file_path)
        file_counter += 1
        print(f"File saved to {file_path}")  # 输出文件保存路径
        return redirect(url_for('uploaded_file', filename=new_filename))
    return 'File upload failed'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)
    except FileNotFoundError:
        return f"File {filename} not found at {app.config['UPLOADED_PHOTOS_DEST']}", 404

def run_server():
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == '__main__':
    run_server()

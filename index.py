from flask import Flask,request,make_response,jsonify,render_template,Response,redirect,abort
from werkzeug.utils import secure_filename
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
file_dir = './files'


# 图片获取地址
@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_url = os.path.join(file_dir, filename)
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            try:
                image_data = open(file_url, "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/jpeg'
                return response
            except Exception:
                abort(404)
    else:
        pass

# 保存头像地址
@app.route('/saveFile',methods=['POST'])
def saveFile():
    file = request.files['avatar']
    new_file_info = []
    try:
        fname=secure_filename(file.filename)
        ext = fname.rsplit('.',1)[1]
        unix_time = int(time.time())
        new_filename=str(unix_time)+'.'+ext
        file.save(os.path.join(file_dir,new_filename))
        new_file_info.append({
            'filename':new_filename,
            "code":0,
            "msg":"上传成功",
        })
    except Exception:
        new_file_info.append({
                "code":-1,
                "msg":"上传失败",
            })
    response = make_response(jsonify(new_file_info))
    return response

# 保存图片墙的图片
@app.route('/saveFiles',methods=['POST'])
def saveFiles():
    file = request.files['file']
    new_file_info = []
    try:
        fname=secure_filename(file.filename)
        ext = fname.rsplit('.',1)[1]
        unix_time = int(time.time())
        new_filename=str(unix_time)+'.'+ext
        file.save(os.path.join(file_dir,new_filename))
        new_file_info.append({
            'filename':new_filename,
            "code":0,
            "msg":"上传成功",
        })
    except Exception:
        new_file_info.append({
                "code":-1,
                "msg":"上传失败",
            })
    response = make_response(jsonify(new_file_info))
    return response

# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
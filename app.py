from flask import Flask,render_template,request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])

def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary,original_text,len_ori_text,len_summary = summarizer(rawtext)
        return render_template('summary.html',summary=summary,original_text=original_text,len_ori_text=len_ori_text,len_summary=len_summary)
    
    # Optionally handle GET requests with a default response
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)


# def analyze():
#     if request.method == 'POST':
#         rawtext = request.form['rawtext']
#         summary, original_text, len_ori_text, len_summary = summarizer(rawtext)
#         return render_template(
#             'summary.html',
#             summary=summary,
#             original_text=original_text,
#             len_ori_text=len_ori_text,
#             len_summary=len_summary
#         )

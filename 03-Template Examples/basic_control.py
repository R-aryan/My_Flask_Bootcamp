from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    my_list=["Huskie","Golden Retriever","German Sephard","Stray","St.Bernard"]
    return render_template('03-Template-Control-Flow.html',my_l=my_list)


if __name__=='__main__':
    app.run(debug=True)

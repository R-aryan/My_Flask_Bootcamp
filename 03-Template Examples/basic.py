from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    some_var="Ritesh"
    l=list(some_var)
    pup_dict={'pup_name':'sammy','pup_age':'12 months'}
    return render_template('01-Template-variables.html',my_var=some_var,my_letter=l,pd=pup_dict)


if __name__=='__main__':
    app.run(debug=True)


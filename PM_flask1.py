from flask import Flask, render_template # render_template accesses an html file

app=Flask(__name__) #instatiates the Flask app

@app.route('/') #this specifies the URL
def home():
    return render_template("home.html")

@app.route('/about/') #this specifies the URL
def about():
    return render_template("about.html") # the webapp automatically notices changes
    # in the code so I don't have to rerun the script!!!


if __name__=="__main__":
    app.run(debug=True)
# remember to create a virtual env before you create the
# flask application

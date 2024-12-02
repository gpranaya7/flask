from flask import Flask,render_template
FI=Flask(__name__)

@FI.route('/first')
def first():
    return 'this is my first flask project'


@FI.route('/secondhtml')
def secondhtml():
    return render_template('secondhtml.html',name='honey')
@FI.route('/UrlAsArg/<name>')
def UrlAsArg(name):
    return f'my name is {name}'

@FI.route('/staticImage')
def staticImage():
    return render_template('staticImage.html')




if __name__=='__main__':
    FI.run(debug=True)
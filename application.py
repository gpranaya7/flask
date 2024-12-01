from flask import Flask,render_template
FI=Flask(__name__)

@FI.route('/first')
def first():
    return 'this is my first flask project'


@FI.route('/secondhtml')
def secondhtml():
    return render_template('secondhtml.html')

if __name__=='__main__':
    FI.run(debug=True)
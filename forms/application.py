from flask import Flask,render_template,request
from wtforms import StringField,SubmitField
from flask_wtf import Form
fai=Flask(__name__)

@fai.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        return request.form['un']
       
    return render_template('htmlforms.html')

class webform(Form):
    name=StringField()
    submit=SubmitField()

@fai.route('/webforms',methods=['GET','POST'])
def webforms():
    form=webform()
    if request.method=='POST':
        FO=webform(request.form)
        
        if FO.validate():
            return f'{FO.name.data}'
    return render_template('webforms.html',form=form)





if __name__=='__main__':
    fai.run(debug=True)

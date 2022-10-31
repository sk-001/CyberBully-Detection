from flask import Flask, render_template ,request,jsonify
import pickle
import numpy as np
app = Flask(__name__,template_folder='templates')
model=pickle.load(open('model_cyber_last.pkl','rb'))


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def sentiment():
    int_feat= [(x) for x in request.form.values()]
    # final_feat=np.array([int_feat])

    prediction=model.predict(int_feat)

    output=round(prediction[0])
    return render_template('index.html',prediction_text='Cyber bully rate is : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
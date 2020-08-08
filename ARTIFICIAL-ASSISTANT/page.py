from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    symptom1 = request.form['sym1']
    symptom2 = request.form['sym2']
    symptom3 = request.form['sym3']
    print(type(symptom1), symptom2, symptom3)
    features = [0]*147
    dict = {' altered_sensorium':0, ' anxiety':1, ' blackheads':2, ' blister':3,
       ' bloody_stool':4, ' blurred_and_distorted_vision':5,
       ' breathlessness':6, ' bruising':7, ' burning_micturition':8,
       ' chest_pain':9, ' chills':10, ' cold_hands_and_feets':11,
       ' continuous_feel_of_urine':12, ' cough':13, ' dark_urine':14,
       ' dehydration':15, ' diarrhoea':16, ' dischromic _patches':17, ' dizziness':18,
       ' extra_marital_contacts':19, ' fatigue':20, ' foul_smell_of urine':21,
       ' headache':22, ' high_fever':23, ' hip_joint_pain':24, ' joint_pain':25,
       ' knee_pain':26, ' lethargy':27, ' loss_of_appetite':28, ' loss_of_balance':29,
       ' mood_swings':30, ' movement_stiffness':31, ' nausea':32, ' neck_pain':33,
       ' nodal_skin_eruptions':34, ' obesity':35, ' pain_in_anal_region':36,
       ' red_sore_around_nose':37, ' restlessness':38, ' scurring':39,
       ' silver_like_dusting':40, ' skin_peeling':41, ' spinning_movements':42,
       ' stomach_pain':43, ' sweating':44, ' swelling_joints':45,
       ' swelling_of_stomach':46, ' ulcers_on_tongue':47, ' vomiting':48,
       ' watering_from_eyes':49, ' weakness_of_one_body_side':50,
       ' weight_loss':51, ' yellowish_skin':52, ' acidity':53, ' anxiety':54,
       ' blackheads':55, ' bladder_discomfort':56, ' blister':57,
       ' breathlessness':58, ' bruising':59, ' chest_pain':60, ' chills':61,
       ' cold_hands_and_feets':62, ' cough':63, ' cramps':64, ' dehydration':65,
       ' dizziness':66, ' fatigue':67, ' foul_smell_of urine':68, ' headache':69,
       ' high_fever':70, ' indigestion':71, ' joint_pain':72, ' knee_pain':73,
       ' lethargy':74, ' loss_of_appetite':75, ' mood_swings':76, ' nausea':77,
       ' neck_pain':78, ' nodal_skin_eruptions':79,
       ' pain_during_bowel_movements':80, ' pain_in_anal_region':81,
       ' patches_in_throat':82, ' pus_filled_pimples':83, ' restlessness':84,
       ' shivering':85, ' skin_peeling':86, ' skin_rash':87, ' stiff_neck':88,
       ' stomach_pain':89, ' sunken_eyes':90, ' sweating':91, ' swelling_joints':92,
       ' ulcers_on_tongue':93, ' vomiting':94, ' weakness_in_limbs':95,
       ' weakness_of_one_body_side':96, ' weight_gain':97, ' weight_loss':98,
       ' yellowish_skin':99, ' acidity':100, ' anxiety':101, ' blackheads':102,
       ' bladder_discomfort':103, ' blister':104, ' breathlessness':105, ' bruising':106,
       ' chest_pain':107, ' chills':108, ' cold_hands_and_feets':109, ' cough':110,
       ' cramps':111, ' dehydration':112, ' dizziness':113, ' fatigue':114,
       ' foul_smell_of urine':115, ' headache':116, ' high_fever':117, ' indigestion':118,
       ' joint_pain':119, ' knee_pain':120, ' lethargy':121, ' loss_of_appetite':122,
       ' mood_swings':123, ' nausea':124, ' neck_pain':125, ' nodal_skin_eruptions':126,
       ' pain_during_bowel_movements':127, ' pain_in_anal_region':128,
       ' patches_in_throat':129, ' pus_filled_pimples':130, ' restlessness':131,
       ' shivering':132, ' skin_peeling':133, ' skin_rash':134, ' stiff_neck':135,
       ' stomach_pain':136, ' sunken_eyes':137, ' sweating':138, ' swelling_joints':139,
       ' ulcers_on_tongue':140, ' vomiting':141, ' weakness_in_limbs':142,
       ' weakness_of_one_body_side':143, ' weight_gain':144, ' weight_loss':145,
       ' yellowish_skin':146}
    symptoms = []
    symptoms.append(dict[symptom1])
    symptoms.append(dict[symptom2])
    symptoms.append(dict[symptom3])

    for i in range(147):
        if i in symptoms:
            features[i] = 1
    pred = model.predict(features)
    return render_template('index.html', prediction_text='Hey {}, symptoms are {}, {}, {} and probable disease is {}'.format(name, symptom1, symptom2, symptom3, pred))

if __name__ == '__main__':
    app.run(debug=True)

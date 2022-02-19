from flask import Flask, render_template, request
# from keras.applications import ResNet50
import pickle
import numpy as np
import pandas as pd




app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def index(): 
    return render_template("index.html")


@app.route("/prediction", methods=["POST", "GET"])
def prediction(): 
    data = 0
    columns = ['covered_area', 'total_area', 'place_Belgrano',
       'place_La Lucila', 'place_Las Lomas Village', 'place_Palermo',
       'place_Provincia', 'place_Puerto Madero', 'place_Recoleta', 'place_mdq',
       'place_pinamar', 'vivienda_casa', 'vivienda_departamento',
       'condition_new', 'condition_used']
    data = pd.DataFrame(columns = columns) 
    data.loc[0] = 0
    data.reset_index(drop=True, inplace=True)

    area = int(request.form["area"])
    data["covered_area"], data["total_area"] = area, area

    vivienda = request.form["vivienda"]
    if vivienda == "departamento": 
        data["vivienda_departamento"] = 1
    else: 
        data["vivienda_departamento"] = 1

    lugar = request.form["lugar"]
    if lugar == "Belgrano":
        data["place_Belgrano"] = 1
    elif lugar == "La Lucila":
        data["place_La Lucila"] = 1
    elif lugar == "Las Lomas Village":
        data["place_Las Lomas Village"] = 1
    elif lugar == "Palermo":
        data["place_Palermo"] = 1
    elif lugar == "Provincia":
        data["place_Provincia"] = 1
    elif lugar == "Recoleta":
        data["place_recoleta"] = 1
    elif lugar == "Puerto Madero":
        data["place_Puerto Madero"] = 1
    elif lugar == "mdq":
        data["place_mdq"] = 1
    elif lugar == "pinamar":
        data["place_pinamar"] = 1

    condicion = request.form["condicion"]
    if condicion == "new": 
        data["condition_new"] = 1
    else: 
        data["condition_used"] = 1


    # arr = np.array([[area]])
    prediction = model.predict(data)
    prediction = round(prediction[0])

    return render_template("index.html", scrollToAnchor="one", data = prediction)
    # return render_template('prediction.html', data=pred)


if __name__ == "__main__": 
    app.run(debug = True)



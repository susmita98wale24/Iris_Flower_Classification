from django.shortcuts import render
import joblib

model = joblib.load('iris_app\iris_model.pkl')
labels = ['Setosa', 'Versicolor', 'Virginica']

def predict_species(request):
    result = ""
    image_url = ""
    if request.method == "POST":
        sl = float(request.POST['sl'])
        sw = float(request.POST['sw'])
        pl = float(request.POST['pl'])
        pw = float(request.POST['pw'])

        prediction = model.predict([[sl, sw, pl, pw]])
        result = labels[prediction[0]]

        # Add image path
        if result == "Setosa":
            image_url = "images/setosa.jpg"
        elif result == "Versicolor":
            image_url = "images/versicolor.jpg"
        elif result == "Virginica":
            image_url = "images/virginica.jpg"

    return render(request, 'iris_form.html', {'result': result, 'image_url': image_url})

def home(request):
    return render(request, 'home.html')
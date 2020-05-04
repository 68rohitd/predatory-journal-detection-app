from django.shortcuts import render
from django.db.models import Q
from .models import Options, Parameter, Journal, JournalDatabase

# imports related to ml integration
from sklearn.externals import joblib
import numpy as np


def searchposts(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(journal_name__icontains=query)
            results = Journal.objects.filter(lookups).distinct()
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')


def post(request):
    query = request.GET.get('query_name')  # getting journal_name
    results = JournalDatabase.objects.filter(journal__journal_name=query)

    score = []
    print("Journal: ", query)
    for i in results:
        if i.parameter.parameter_name == 'PREDATORY (1) / NON PREDATORY (0):':
            pass
        else:
            score.append(i.chosen_option.score)

    print("Score list: ", score, "length: ", len(score))

    loadedModel = joblib.load(
        'C:\\Users\\ROHIT\\Desktop\\predatory\\pred\\mlModel\\DecisionTreeModel.pkl')
    score = np.asarray(score).reshape(1, -1)
    predict = loadedModel.predict(score)
    print("Predict: ", predict)
    if predict == 1:
        is_it_predatory = "It's a predatory journal!"
    else:
        is_it_predatory = "It's not a Predatory journal!"
    print("Prediction: ", is_it_predatory)

    context = {
        "link": request.GET.get('query_name'),
        "jd": results,
        "predicted": is_it_predatory
    }

    return render(request, 'form.html', context)

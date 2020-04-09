from django.shortcuts import render
from django.db.models import Q
from .models import Journaltable, Journaltable2

# imports related to ml integration
from sklearn.externals import joblib 
import numpy as np



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(Links__icontains=query) 
            results= Journaltable2.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')


def post(request):
    query = request.GET.get('query_name')
    lookups = Q(Links__icontains=query)
    results = Journaltable2.objects.filter(lookups).distinct().values() 
    results = list(results)
    # print(results[0])
    
    # logic for extracting weightage from results[0] -> its a dict {'id': 44, 'name': 'adfasf'...}
    excemption_list = ['id', 'Name_of_journal', 'Links', 'Category', 'Predatory_1_Non_predatory_0']
    weightage_list = []
    is_it_predatory = False
    for k, v in results[0].items():
        if k not in excemption_list:
            weightage_list.append(int(v))
    print(weightage_list)

    # loading ml model
    loadedModel = joblib.load('C:\\Users\\ROHIT\\Desktop\\predatory\\pred\\mlModel\\DecisionTreeModel.pkl') 
    weightage_list = np.asarray(weightage_list).reshape(1, -1)
    predict = loadedModel.predict(weightage_list)
    if predict == 1:
        is_it_predatory = True
    else:
        is_it_predatory = False

    metric = Journaltable2.Metric
    score = 0
    list_of_metrics = []
    for m in metric:
        list_of_metrics.append(m[0][0])

    for i in list_of_metrics:
        score += int(results[0][i])
    
    score = score/len(list_of_metrics)

    context = {"link": request.GET.get('query_name'),
                "info":results,
                "metric_list": metric,
                "m":results[0],
                "score": score,
                "is_it_predatory": is_it_predatory
            }

    return render(request, 'form.html', context)

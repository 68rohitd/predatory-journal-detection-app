from django.shortcuts import render
from django.db.models import Q
from .models import Journaltable


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(domain__icontains=query) | Q(topic__icontains=query) | Q(publisher__icontains=query) | Q(journal__icontains=query)
            results= Journaltable.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')


def post(request):
    query = request.GET.get('query_name')
    lookups = Q(journal__icontains=query)
    results = Journaltable.objects.filter(lookups).distinct().values() 
    results = list(results)

    metric = Journaltable.Metric
    # print("*******",metric,"*******")
    
    score = 0
    list_of_metrics = []
    for m in metric:
        list_of_metrics.append(m[0][0])

    for i in list_of_metrics:
        score += int(results[0][i])
    
    score = score/len(list_of_metrics)
    print("final Score: ", score)

    context = {"link": request.GET.get('query_name'),
                "info":results,
                "metric_list": metric,
                "m":results[0],
                "score": score
            }

    return render(request, 'form.html', context)

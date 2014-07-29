from django.shortcuts import render
from mangalore.models import Bus
from mangalore.forms import RouteForm
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def routes(request):
    print 'routes'
    if request.method == 'POST':
        print 'inside post'
        form = RouteForm(request.POST)
        if form.is_valid():
            print "valid"
            source = form.cleaned_data['source']
            destination = form.cleaned_data['destination']
            buses = Bus.objects.filter(Q(stops__icontains = source),Q(stops__icontains = destination))
            print buses
            if buses:
                i=[]
                for bus in buses:
                    print bus.stops
                    bus_str = bus.stops.replace(" ","")
                    bus_list = bus_str.split(',')
                    print bus_list
                    first = bus_list.index(str(source.replace(" ","")))
                    print first
                    last = bus_list.index(str(destination.replace(" ","")))
                    print last
                    intermediate = bus_list[first:last] 
                    if not intermediate:
                        intermediate = bus_list[last:first]
                        intermediate = intermediate[::-1]
                    print intermediate
                    via=[]
                    for inter in intermediate:
                        via.append(str(inter))
                    i.append(via)
                print i
                z = zip(buses,i)
                print z
                return render_to_response('index.html', locals(), context_instance=RequestContext(request))
        else:
            form = RouteForm()
            return render_to_response('index.html', locals(), context_instance=RequestContext(request))
    else:
        form = RouteForm()
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))
                    
                    


from django.shortcuts import render

# Create your views here

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import WatchsSerializer
from rest_framework import status
from .models import Watch

class WatchList(APIView):
    def get(self,request):
        all_watches = Watch.objects.all()
        serializers = WatchsSerializer(all_watches, many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers = WatchsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)  
        return Response("An error occured, check if you have duplicated data or added a wrong data type", status = status.HTTP_400_BAD_REQUEST)         

# class CreateOneWatch(APIView):
#     def post(self,request):
#         serializers = WatchsSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)  
#         return Response("An error occured")

class OneWatchType(APIView):
    def get( self, request, pk):
        get_one_watch = Watch.objects.get(pk=pk)
        serializers = WatchsSerializer(get_one_watch)
        return Response(serializers.data)  

        

    def delete(self, request, pk):
        delete_one_watch = Watch.objects.get(pk = pk)
        delete_one_watch.delete()
        return Response("This stock has been deleted", status=status.HTTP_204_NO_CONTENT) 

class UpdateWatch(APIView):
    def post( self, request, pk):
        update_one_watch = Watch.objects.get(pk =pk)
        serializers = WatchsSerializer(instance=update_one_watch, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response("An error occurred") 

def landing(request):
    return render( request, "landing.html")   

def watches(request):
    return render( request, "watches.html")                
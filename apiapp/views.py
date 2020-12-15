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
        return Response(serializers.data)       


class OneWatchType(APIView):
    def get( self, request, pk):
        get_one_watch = Watch.objects.get(pk=pk)
        serializers = WatchsSerializer(get_one_watch)
        return Response(serializers.data)  

    def put( self, request, pk):
        update_one_watch = Watch.objects.get(pk =pk)
        serializers = WatchsSerializer(update_one_watch, request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)    

    def delete(self, request, pk):
        delete_one_watch = Watch.objects.get(pk = pk)
        delete_one_watch.delete()
        return Response("This stock has been deleted")    
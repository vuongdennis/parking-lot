from .models import Space, History
from .serializers import ExitHistorySerializer, ExitSpaceSerializer, SpaceSerializer, HistorySerializer
from .ticketprice import TicketPrice
from .time import Time
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'spaces': reverse('spaces-list', request=request, format=format),
        'history': reverse('history-list', request=request, format=format)
    })

class SpaceView(APIView):
    def get(self, request):
        spaces = Space.objects.all()
        serializer = SpaceSerializer(spaces, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data.update({
            "time_in": Time.current_time(),
        })
        space_serializer = SpaceSerializer(data=data)
        history_serializer = HistorySerializer(data=data)
        if space_serializer.is_valid() and history_serializer.is_valid():
            space_serializer.save()
            history_serializer.save()
            return Response(space_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(space_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpaceDetail(APIView):
    def get_object(self, pk):
        try:
            return Space.objects.get(pk=pk)
        except Space.DoesNotExist:
            raise Http404

    def get_history_object(self, pk):
        try:
            return History.objects.get(pk=pk)
        except History.DoesNotExist:
            raise Http404

    def isAlreadyCheckedOut(self, space):
        return space.price == -1
        
    def get(self, request, pk, format=None):
        space = self.get_object(pk)
        serializer = SpaceSerializer(space)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = request.data
        space = self.get_object(pk)
        history = self.get_history_object(pk)

        if self.isAlreadyCheckedOut(space):
            time_out = Time.current_time()
            time_difference = Time.time_difference_minutes(space.time_in, time_out)
            price = TicketPrice.calculate(time_difference)
            data.update({'time_out': time_out, 'price': price})

        space_serializer = ExitSpaceSerializer(space, data=data)
        history_serializer = ExitHistorySerializer(history, data=data)
        
        if space_serializer.is_valid() and history_serializer.is_valid():
            space_serializer.save()
            history_serializer.save()
            return Response(SpaceSerializer(space).data)
        return Response(space_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        space = self.get_object(pk)
        space.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class HistoryView(APIView):
    def get(self, request):
        history = History.objects.all()
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)

    
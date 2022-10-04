from rest_framework.views import APIView
from rest_framework import status
from .serializers import MediaServiceSerializer
from rest_framework.response import Response
from .models import MediaService

class MediaServiceView(APIView):
    def post(self, request):
        mediaService = MediaService.objects.all()
        serializer = MediaServiceSerializer(data=request.data, context={"request": request})
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        file_url = request.query_params.get('url')
        print(file_url)

        url_m = str(file_url)
        url_m = url_m.split('media/')[1]
        print(url_m)
        
        mediaService = MediaService.objects.get(file_url=url_m)        
        
        assigned = self.request.data['assigned']
        print(assigned)
        
        print(assigned)
        assigned_boolean = 0
            
        if assigned == 'true':
            assigned_boolean = 1
        elif assigned == 'false':
            assigned_boolean = 0
        else:
            assigned_boolean = 0
        
        obj = {
            'id': mediaService.id,
            'created_at': mediaService.created_at,
            'assigned': assigned_boolean,
            'file_url': mediaService.file_url
        }
        
        serializer = MediaServiceSerializer(mediaService, data=obj, context={"request": request})
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
        
class MediaServiceDetailView(APIView):
    def get(self, request, pk):
        mediaService = MediaService.objects.get(pk=pk)
        serializer = MediaServiceSerializer(mediaService, context={"request": request})
        
        return Response(serializer.data)
    
    def delete(self, request, pk):
        mediaService = MediaService.objects.get(pk=pk)
        mediaService.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    







 
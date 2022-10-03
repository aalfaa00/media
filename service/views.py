from django.forms import Media
from rest_framework import views
from rest_framework import status
from .serializers import MediaServiceSerializer
from rest_framework.response import Response
from .models import MediaService
from django.shortcuts import get_object_or_404
from django.core.exceptions import BadRequest

class MediaServiceView(views.APIView):
    
    def check_query(self, request):
        items = []
        for item in request.query_params:
            items.append(item)
            
            if item != 'id' and item != 'url' and item != 'assigned':
                raise BadRequest()
            # elif item == 'id' and 'url':
            #     raise BadRequest()
            
        if len(items) == 2:
            if items[0] == 'id' and items[1] == 'url':
                raise BadRequest()
            elif items[1] == 'assigned' and items[0] == 'url':
                return 'assigned'
            elif items[0] == 'assigned' and items[1] == 'url':
                raise BadRequest()
        elif len(items) == 1:
            if items[0] == 'assigned':
                raise BadRequest()
        
        return True

    def get(self, request):
        id = request.query_params.get('id')
        url = request.query_params.get('url')
        ps = self.check_query(request)
        
        if id:
            mediaService = get_object_or_404(MediaService, id=id)
            serializer = MediaServiceSerializer(mediaService, context={"request": request})
            
            return Response(serializer.data)
        elif ps == 'assigned':
            assigned = request.query_params.get('assigned')
            url_m = str(url)
            url_m = url_m.split('media/')[1]
            
            mediaService = get_object_or_404(MediaService,file_url=url_m)
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
            
        else:
            mediaservice = MediaService.objects.all()
            serializer = MediaServiceSerializer(mediaservice, many=True, context={"request": request})
            
            return Response(serializer.data)
        
    def post(self, request):
        serializer = MediaServiceSerializer(data=request.data, context={"request": request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    

class MediaServiceDetailView(views.APIView):
    def delete(self, request, pk, format=None):
        mediaService = MediaService.objects.get(pk=pk)
        mediaService.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

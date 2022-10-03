from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
import uuid



class MediaService(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    file_url = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    assigned = models.BooleanField(default=False)




       

    
    
    


  
    

    
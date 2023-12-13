from rest_framework import views, permissions, status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from ..authentication import JWTAuthentication
from db.models import CustomUser as User
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest
from utils.permissions import role_required

# class UserView(views.APIView):
#     def post(self, request):
#       try:
#         serializer = UserSerializer(data=request.data) 
#         if serializer.is_valid():  
#             serializer.save() 
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#         else:  
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
#       except Exception as e:
#           return Response({"status":"error","message":"An unexpected error occured"})
    
#     def put(self, request:HttpRequest ):
#         try:
#             instance = CustomUser.objects.filter(username=request.POST.get('username',None)).first()
#             if instance == None:
#                 return Response({'status':'error','message':'invalid username'})
#             serializer = UserSerializer(instance=instance,data=request.data) 
#             if serializer.is_valid():  
#                 serializer.update() 
#                 return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#             else:  
#                 return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
#         except Exception as e:
#             return Response({"status":"internal-error","message":"An unexpected error occured"})
        
class VerificationView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        if request.user.is_authenticated:
            return Response({"status":"success",'data':{'verified':True,'verified_as':request.user.email,"role":request.user.user_role}})
        else:
            return Response({"status":"success",'data':{'verified':False}})


class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None or not user.password== password:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token,"role":user.user_role}, status=200)
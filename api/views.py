from rest_framework import request, status, viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer  

    
    @action(detail=True, methods=['post'])  
    def rate_meal(self, request, pk=None):
        if "starts" in request.data :
            username= request.data["user"]
            starts = request.data['starts']
            user=User.objects.get(username= username)
            meal= Meal.objects.get(id=pk)

            try: #to updata rating 

                rating = Rating.objects.get(user=user.id, meal=meal.id) # specific rate 
                rating.stars = starts
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                jsonmessage = {
                    'message': 'Meal Rate Updated',
                    'result': serializer.data
                }
                return Response(jsonmessage , status=status.HTTP_200_OK)
            
            except :#to create rating 

                rating = Rating.objects.create(stars=stars, user= user,meal= meal)
                serializer = RatingSerializer(rating, many=False)
                jsonmessage = {
                    'message': 'Meal Rate created',
                    'result': serializer.data
                }
                return Response(jsonmessage, status= status.HTTP_201_CREATED)
            
        else:
            message={ "message":"stars not provided"  }
            return Response(message,status= status.HTTP_400_BAD_REQUEST)    
        


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

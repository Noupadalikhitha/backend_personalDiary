from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile, DiaryEntry
from .serializers import UserSerializer, ProfileSerializer, DiaryEntrySerializer

# Create your views here.

@api_view(['POST'])
@ensure_csrf_cookie
@permission_classes([AllowAny])
def login_view(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        
        print(f"Login attempt for username: {username}")
        
        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(username=username, password=password)
        print(f"Authentication result for {username}: {'Success' if user else 'Failed'}")
        
        if user is not None:
            if not user.is_active:
                return Response(
                    {'error': 'This account is inactive'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            login(request, user)
            print(f"User {username} logged in successfully")
            print(f"Session ID: {request.session.session_key}")
            
            response = Response({
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })
            
            # Ensure the session cookie is set
            response.set_cookie(
                'sessionid',
                request.session.session_key,
                httponly=True,
                samesite='Lax'
            )
            
            return response
        
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        import traceback
        print(f"Error in login_view: {str(e)}")
        print(traceback.format_exc())
        return Response(
            {'error': 'Login failed', 'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def register_view(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Create a profile for the user
            Profile.objects.create(user=user, bio='')
            # Log the user in
            login(request, user)
            return Response({
                'message': 'Registration successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        import traceback
        print(f"Error in register_view: {str(e)}")
        print(traceback.format_exc())
        return Response(
            {'error': 'Registration failed', 'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        print(f"Logout attempt for user: {request.user.username}")
        print(f"Session ID before logout: {request.session.session_key}")
        
        # Perform logout
        logout(request)
        
        # Create response
        response = Response({'message': 'Logged out successfully'})
        
        # Clear session cookie
        response.delete_cookie('sessionid')
        
        # Clear CSRF cookie
        response.delete_cookie('csrftoken')
        
        print("Logout successful, cookies cleared")
        return response
    except Exception as e:
        print(f"Error in logout_view: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return Response(
            {'error': 'Logout failed', 'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DiaryEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DiaryEntrySerializer

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['GET'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
def user_info(request):
    try:
        profile, created = Profile.objects.get_or_create(
            user=request.user,
            defaults={'bio': ''}
        )
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'bio': profile.bio,
            'email': request.user.email
        })
    except Exception as e:
        import traceback
        print(f"Error in user_info: {str(e)}")
        print(traceback.format_exc())
        return Response(
            {'error': 'Failed to fetch user info', 'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

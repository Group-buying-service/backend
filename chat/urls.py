from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:room_id>/", views.chatRoomView.as_view(), name="room"),
    path("API/<int:room_id>/", views.ChatRoomAPIView.as_view(), name="roomAPI"),
]
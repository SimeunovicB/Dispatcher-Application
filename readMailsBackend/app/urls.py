from django.urls import path

from app.views import IndexView
from app.views import ReadMailsView
from app.views import UnreadMessagesView
from app.views import AllMessagesView
from app.authViews import RegisterView, RegisterAdminView, LoginView, UserView, LogoutView, UsersViewSet
from app.views import TestView


urlpatterns = [
    path('', IndexView.as_view()),
    path('read/mail', ReadMailsView.as_view()),
    path('unread/messages', UnreadMessagesView.as_view()),
    path('all/messages', AllMessagesView.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('test', TestView.as_view()),
    path('register/admin', RegisterAdminView.as_view()),
    path('users', UsersViewSet.as_view()),
]
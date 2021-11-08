from django.urls import path, include

from app.views import IndexView
from app.views import ReadMailsView
from app.views import UnreadMessagesView
from app.views import AllMessagesView
from app.authViews import RegisterView, RegisterAdminView, LoginView, UserView, LogoutView, UsersViewSet, ChangeUserActivityView
from app.views import TestView
from rest_framework import routers
from app.views import LeadViewSet
from app.leadViews import ClaimLeadView, UnclaimLeadView, SortedLeadsView
from app.leadViews import AddNoteView
from app.views import NoteViewSet

router = routers.DefaultRouter()
# router.register(r'leads', LeadViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
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
    path('user/activity', ChangeUserActivityView.as_view()),
    path('lead/claim', ClaimLeadView.as_view()),
    path('lead/unclaim', UnclaimLeadView.as_view()),
    path('leads/', SortedLeadsView.as_view()),
    path('note/', AddNoteView.as_view()),
]
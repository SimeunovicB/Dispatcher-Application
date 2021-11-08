from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import UserPermission
from .models import Lead
from .models import User
from .models import Note
from .serializers import LeadSerializer
import datetime
import operator


class ClaimLeadView(APIView):
    def put(self, request):
        print("Claim Lead View")
        print("ID LEAD ", request.data["idLead"])
        idLead = request.data["idLead"]
        print("ID USER ", request.data["idUser"])
        idUser = request.data["idUser"]
        if not UserPermission.has_permission(self, request):
            return Response({"detail": "Not authenticated."}, status=401)

        lead = Lead.objects.get(id=idLead)
        print(lead)
        user = User.objects.get(id=idUser)
        print(user)
        lead.agent = user;
        lead.save()

        leads = Lead.objects.order_by('id')
        serializer = LeadSerializer(leads, many=True)
        response = Response(serializer.data, content_type="application/json")
        return response


class UnclaimLeadView(APIView):
    def put(self, request):
        idLead = request.data["idLead"];
        lead = Lead.objects.get(id=idLead)
        lead.agent = None
        lead.save()
        leads = Lead.objects.order_by('id')
        serializer = LeadSerializer(leads, many=True)
        response = Response(serializer.data, content_type="application/json")
        return response


class SortedLeadsView(APIView):
    def get(self, request):
        print("Sorted Leads")
        leads = Lead.objects.order_by('id')
        serializer = LeadSerializer(leads, many=True)
        response = Response(serializer.data, content_type="application/json")
        return response


class AddNoteView(APIView):
    def post(self, request):
        print("AddNoteView")
        print("REQUEST ", request.data)
        sender_id = request.data["sender"]
        sender = User.objects.get(id=sender_id)
        lead_id = request.data["lead"]
        lead = Lead.objects.get(id=lead_id)
        message = request.data["message"]
        date_time = datetime.datetime.now()
        time = date_time.strftime("%b %d %Y %H:%M")
        note = Note.objects.create(sender=sender, lead=lead, message=message, time=time)
        note.save()
        response = Response("AddNoteView", content_type="application/json")
        return response

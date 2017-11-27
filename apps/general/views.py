from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response as ResponseApi
from rest_framework.views import APIView

from .models import State, Category, Criteria, DrillBit, Motive, Polymer, Section, SubSection
from utils.Response import Response
from utils.constants import CONTENT_TYPE_JSON

import logging
logger = logging.getLogger(__name__)


class StateApiView(APIView):

    def get(self, request, *args, **kw):
        pk = request.GET.get('pk', "")
        res = Response()
        data = None

        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("pk: {0}".format(pk))
            logger.debug(args)
            logger.debug(kw)

        try:
            if pk:
                data = State.objects.values('idState', 'nameState', 'status').get(pk=int(pk))
            else:
                states = State.objects.values('idState', 'nameState', 'status').all()
                # return ResponseApi(states, status=status.HTTP_200_OK)
                data = list(states)
            res.status = Response.STATUS_OK
            res.data = data
        except Exception as e:
            logger.error(e)
            res.status = Response.STATUS_EXCEPTION
            res.message = str(e)

        return HttpResponse(res.toJSON(), content_type=CONTENT_TYPE_JSON)

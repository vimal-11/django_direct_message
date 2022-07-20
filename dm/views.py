from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,

)
from .models import MessageModel, DialogsModel, UploadedFile
from .serializers import serialize_message_model, serialize_dialog_model, serialize_file_model
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.paginator import Page, Paginator
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse_lazy
from django.forms import ModelForm
import json


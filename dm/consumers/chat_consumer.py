import json
from typing import Optional, Dict, Tuple

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AbstractBaseUser

from .db_operations import get_groups_to_add, get_unread_count, get_user_by_pk, get_file_by_id, get_message_by_id, \
                            save_file_message, save_text_message, mark_message_as_read

from .message_types import MessageTypes, MessageTypeMessageRead, MessageTypeFileMessage, MessageTypeTextMessage, \
    OutgoingEventMessageRead, OutgoingEventNewTextMessage, OutgoingEventNewUnreadCount, OutgoingEventMessageIdCreated,\
    OutgoingEventNewFileMessage, OutgoingEventIsTyping, OutgoingEventStoppedTyping, OutgoingEventWentOnline, OutgoingEventWentOffline

from .errors import ErrorTypes, ErrorDescription
from dm.models import MessageModel, UploadedFile
from dm.serializers import serialize_file_model
from django.conf import settings
import logging
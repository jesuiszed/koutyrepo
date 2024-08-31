from django.shortcuts import render
from .models import Visitor, VisitorCount
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear



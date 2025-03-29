from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import WeightRecord
import json


# Get all records
def get_all(request, order=None):
    print("get_all()")
    records = WeightRecord.objects.all().values()
    

    if order is not None:
        if order == "dec":
            records = records.order_by("-date")
        elif order == "asc":
            records = records.order_by("date")

    return JsonResponse(list(records), safe=False)


# Add a new record
@csrf_exempt
def add_record(request):
    print("add_record()")
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            weight = body.get("weight")
            date = body.get("date")
            record = WeightRecord.objects.create(weight=weight, date=date)
            return JsonResponse({"message": "Record added successfully!", "id": record.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Edit an existing record
@csrf_exempt
def update_record(request, record_id):
    print("update_record()")
    if request.method == "PUT":
        try:
            body = json.loads(request.body)
            weight = body.get("weight")
            # date = body.get("date")
            record = WeightRecord.objects.get(id=record_id)
            record.weight = weight
            # record.date = date
            record.save()
            return JsonResponse({"message": "Record updated successfully!"}, status=200)
        except WeightRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Delete a record
@csrf_exempt
def delete_record(request, record_id):
    print("delete_record()")
    if request.method == "DELETE":
        try:
            record = WeightRecord.objects.get(id=record_id)
            record.delete()
            return JsonResponse({"message": "Record deleted successfully!"}, status=200)
        except WeightRecord.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
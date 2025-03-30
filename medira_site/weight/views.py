from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import WeightRecord
import json

batch = [
    { "weight": 107.1, "date": "2024-05-18T10:00:00.000Z" },
    { "weight": 105.3, "date": "2024-05-19T10:00:00.000Z" },
    { "weight": 106.7, "date": "2024-06-26T10:00:00.000Z" },
    { "weight": 104.8, "date": "2024-06-29T10:00:00.000Z" },
    { "weight": 104.9, "date": "2024-06-30T10:00:00.000Z" },
    { "weight": 105.3, "date": "2024-06-30T10:00:00.000Z" },
    { "weight": 105.4, "date": "2024-07-01T10:00:00.000Z" },
    { "weight": 106.2, "date": "2024-06-02T10:00:00.000Z" },
    { "weight": 106.7, "date": "2024-06-05T10:00:00.000Z" },
    { "weight": 105.7, "date": "2024-06-07T10:00:00.000Z" },
    { "weight": 108.3, "date": "2024-06-28T10:00:00.000Z" },
    { "weight": 107.75, "date": "2024-06-30T10:00:00.000Z" },
    { "weight": 107.75, "date": "2024-07-01T10:00:00.000Z" },
    { "weight": 108, "date": "2024-07-04T10:00:00.000Z" },
    { "weight": 106.7, "date": "2024-07-06T10:00:00.000Z" },
    { "weight": 107.5, "date": "2024-07-07T10:00:00.000Z" },
    { "weight": 108.4, "date": "2024-08-08T10:00:00.000Z" },
    { "weight": 105.9, "date": "2024-09-09T10:00:00.000Z" },
    { "weight": 107.5, "date": "2024-07-13T10:00:00.000Z" },
    { "weight": 106.9, "date": "2024-07-22T10:00:00.000Z" },
    { "weight": 108, "date": "2024-07-25T10:00:00.000Z" },
    { "weight": 109, "date": "2024-10-04T10:00:00.000Z" },
    { "weight": 114.8, "date": "2024-12-06T10:00:00.000Z" },
    { "weight": 112, "date": "2025-01-29T10:00:00.000Z" },
    { "weight": 111.5, "date": "2025-01-30T10:00:00.000Z" },
    { "weight": 111.1, "date": "2025-02-04T10:00:00.000Z" },
    { "weight": 109.4, "date": "2025-02-07T10:00:00.000Z" },
    { "weight": 111.4, "date": "2025-02-10T10:00:00.000Z" },
    { "weight": 109.8, "date": "2025-02-14T10:00:00.000Z" },
    { "weight": 110.6, "date": "2025-02-17T10:00:00.000Z" },
    { "weight": 110.5, "date": "2025-02-18T10:00:00.000Z" },
    { "weight": 110.3, "date": "2025-02-19T10:00:00.000Z" },
    { "weight": 110.2, "date": "2025-02-22T10:00:00.000Z" },
    { "weight": 110.8, "date": "2025-03-24T10:00:00.000Z" },
    { "weight": 110.8, "date": "2025-03-27T10:00:00.000Z" },
    { "weight": 109.7, "date": "2025-03-28T10:00:00.000Z" }
]


@csrf_exempt
def add_batch(request):
    if request.method == "POST":
        try:
            # Iterate over the batch list and create WeightRecord instances
            for entry in batch:
                WeightRecord.objects.create(weight=entry["weight"], date=entry["date"])
            return JsonResponse({"message": "Batch added successfully!"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

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
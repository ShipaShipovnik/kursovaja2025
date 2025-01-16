import os

def service_photo_path(instance, filename):
    service_id = instance.id if instance.id else "temp"  # Если объект еще не сохранен
    photo_number = len(instance.photos) + 1  # Номер фото
    ext = os.path.splitext(filename)[1]  # Расширение
    new_filename = f"service{service_id}_{photo_number}{ext}"
    return os.path.join('service_photos', new_filename)
from django.conf import settings


def upload_document(instance: "Contract" , filename: str) -> str:
    return f"{settings.STATIC_ROOT}/documents/{instance.name}/{filename}"

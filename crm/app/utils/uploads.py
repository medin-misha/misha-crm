from django.conf import settings


def upload_document(instance: "Contract", filename: str) -> str:
    return f"static/documents/{filename}"

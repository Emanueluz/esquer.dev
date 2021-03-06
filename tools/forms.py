from django import forms
from django.core.validators import FileExtensionValidator
from upload_validator import FileTypeValidator
from django_clamd.validators import validate_file_infection
from .validators import FileSizeValidator

allowed_types = [
    "application/epub+zip",
    "application/pdf",
    "application/vnd.oasis.opendocument.chart",
    "application/vnd.oasis.opendocument.formula",
    "application/vnd.oasis.opendocument.graphics",
    "application/vnd.oasis.opendocument.image",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/vnd.oasis.opendocument.text",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/x-bittorrent",
    "application/x-dtbncx+xml",
    "application/x-tar",
    "application/xhtml+xml",
    "application/zip",
    "audio/flac",
    "audio/mpeg",
    "audio/ogg",
    "audio/x-wav",
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/svg+xml",
    "image/tiff",
    "image/x-ms-bmp",
    "image/x-portable-pixmap",
    "text/css",
    "text/html",
    "text/plain",
    "video/mp4",
    "video/x-ms-wmv",
    "video/x-msvideo",
    "application/x-empty",
]

allowed_extensions = [
    "epub",
    "pdf",
    "odc",
    "odf",
    "odg",
    "odi",
    "odp",
    "ods",
    "odt",
    "pptx",
    "xlsx",
    "docx",
    "torrent",
    "ncx",
    "tar",
    "xht",
    "xhtml",
    "zip",
    "flac",
    "mp3",
    "m4a",
    "mp2",
    "mpega",
    "mpga",
    "opus",
    "ogg",
    "oga",
    "spx",
    "wav",
    "gif",
    "jpg",
    "jpeg",
    "jpe",
    "png",
    "svg",
    "svgz",
    "tif",
    "tiff",
    "bmp",
    "ppm",
    "css",
    "shtml",
    "html",
    "htm",
    "text",
    "txt",
    "mp4",
    "wmv",
    "avi",
]


class MetadataRemovalForm(forms.Form):
    file_to_clean = forms.FileField(
        label="Selecione um arquivo",
        max_length=100,
        allow_empty_file=True,
        validators=[
            FileSizeValidator(max_size=(1024*1024)*25),
            validate_file_infection,
            FileExtensionValidator(allowed_extensions=allowed_extensions),
            FileTypeValidator(allowed_types=allowed_types),
        ],
    )

from django.core.exceptions import ValidationError


def valid_size(value):
    max_size = 4 * 1024 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError('Слишком большой файл')


def valid_video(value):
    import os
    field = os.path.splitext(value.name)[1]
    if not field.lower() in ['.mp4', '.avi']:
        raise ValidationError('Формат не поддерживается, попробуйте другой')


def valid_image(value):
    import os
    field = os.path.splitext(value.name)[1]
    if not field.lower() in ['.png', '.jpg', '.jpeg']:
        raise ValidationError('Формат не поддерживается, попробуйте другой')

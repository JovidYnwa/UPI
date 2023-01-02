from xml.dom import ValidationErr


def get_path_upload_avatar(instance, file):
    """Path generator for user avatar
    format: (media)/avatar/user_id/photo.jpg
    """

    return f'avatar/{instance.user_id}/{file}'

def get_path_upload_merchant(instance, file):
    """Path generator for user avatar
    format: (media)/merchant_category/user_id/photo.jpg
    """

    return f'merchant/{instance}/{file}'

def validate_size_image(file_obj):
    """Chaking file size it should be <= 2 mb
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024**2:
        raise ValidationErr(f"File size should be not larger then {megabyte_limit}MB")
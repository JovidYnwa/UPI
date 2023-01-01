from xml.dom import ValidationErr


def get_path_upload_avatar(instance, file):
    """Path generator for user avatar
    format: (media)/avatar/user_id/photo.jpg
    """
    print(f'insgtance is {instance} and file {file}')
    return f'avatar/{instance.user_id}/{file}'

def validate_size_image(file_obj):
    """Chaking file size it should be <= 2 mb
    """

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024**2:
        raise ValidationErr(f"File size should be not larger then {megabyte_limit}MB")
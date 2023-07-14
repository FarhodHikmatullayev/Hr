
def avatar_path(instance, filename):
    return f'accounts/{instance.email}/avatar/{filename}'


def cv_path(instance, filename):
    return f'accounts/{instance.email}/cv/{filename}'

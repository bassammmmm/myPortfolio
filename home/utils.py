def project_image_path(instance, filename):
    return f"projects/{instance.title} Images/{filename}"

def project_images_path(instance, filename):
    return f"projects/{instance.project.title} Images/{filename}"

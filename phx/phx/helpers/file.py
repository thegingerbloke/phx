def file_size_string(size):
    """
    convert a file size into a friendly string
    """
    if size < 512000:
        size = size / 1024.0
        ext = 'kb'
    elif size < 4194304000:
        size = size / 1048576.0
        ext = 'mb'
    else:
        size = size / 1073741824.0
        ext = 'gb'
    return '{0} {1}'.format(str(round(size, 2)), ext)

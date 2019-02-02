import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print '%r took %2.2f ms to execute' % (method.__name__, (te - ts) * 1000)
        return result
    return timed

def get_file_size(file_obj):
    size = None
    try:
        size = os.fstat(file_obj.fileno()).st_size
    except:
        # Not all file objects implement fileno(),
        # so we fall back on this
        file_obj.seek(0, os.SEEK_END)
        size = file_obj.tell()
    return size

def get_inMemory_obj_size(obj):
    ''' Returns object size in MB'''
    return sys.getsizeof(obj) / (10**6)
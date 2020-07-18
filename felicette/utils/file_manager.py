import tempfile
import os
import requests
from tqdm import tqdm

workdir = os.path.join(os.path.expanduser("~"), "felicette-data")
data_path = os.path.join(workdir, "LC81390462020136")

if not os.path.exists(data_path):
    os.mkdir(data_path)


def save_to_file(url, filename):
    file_path = os.path.join(data_path, filename)
    response = requests.get(url, stream=True)
    with tqdm.wrapattr(open(file_path, "wb"), "write",
                   miniters=1, desc=filename,
                   total=int(response.headers.get('content-length', 0))) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
    fout.close()


def data_file_exists(filename):
    file_path = os.path.join(data_path, filename)
    return os.path.exists(file_path)

def file_paths_wrt_id(id):
    home_path_id = os.path.join(workdir, id)
    return {
        "base": home_path_id,
        "b4": os.path.join(home_path_id, "%s-b4.tiff" % (id)),
        "b3": os.path.join(home_path_id, "%s-b3.tiff" % (id)),
        "b2": os.path.join(home_path_id, "%s-b2.tiff" % (id)),
        "output_path": os.path.join(home_path_id, "%s-color-processed.tiff" % (id)),
        "output_path_jpeg": os.path.join(home_path_id, "%s-color-processed.jpeg" % (id))
    }
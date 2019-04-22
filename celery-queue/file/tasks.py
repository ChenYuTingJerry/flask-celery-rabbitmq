import zipfile

import requests
from celery import chain, group
from tqdm import tqdm

from celery_worker import app


@app.task(ignore_result=True)
def get_multi_python_packages(versions):
    job = group([get_python_package.s(v) for v in versions])
    job.apply_async()


@app.task(ignore_result=True)
def get_python_package(version):
    fileName = f"python-{version}-embed-amd64.zip"
    url = f'https://www.python.org/ftp/python/{version}/{fileName}'
    chain(download_file.s(url) | unzip_file.s()).apply_async()


@app.task
def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_size = int(r.headers.get('content-length', 0))
        with tqdm(total=file_size, initial=0, unit='KB') as pbar:
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        pbar.update(1024)

    return local_filename


@app.task(ignore_result=True)
def unzip_file(filename):
    import os
    dir = os.path.splitext(filename)[0]
    zf = zipfile.ZipFile(filename)
    zf.extractall(f'./extract/{dir}')

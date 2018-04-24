from pathlib import Path
from helpers.aws import s3client

if __name__ == '__main__':
    s3client.get_file(
        bucket='my_bucket',
        key='path/to/file/in/bucket',
        local_path=Path('/tmp/local_file.json'))

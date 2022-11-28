import requests

token = ''



def get_upload_link(disk_file_path):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {'Content-Type': 'application/json','Authorization': f'OAuth {token}'}
    params = {"path": disk_file_path, "overwrite": "true"}
    response = requests.get(upload_url, headers = headers, params=params)
    return response.json()


def upload_file_to_disk(disk_file_path, filename):
    href = get_upload_link(disk_file_path=disk_file_path).get("href", "")
    response = requests.put(href, data=open(filename, 'rb'))


if __name__ == '__main__':
    upload_file_to_disk("test/netology", "test.txt")
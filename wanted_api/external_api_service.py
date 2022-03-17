import requests

base_url = "https://api.fbi.gov/wanted/v1/list"

def get_wanted_list():
    wanted_list = []
    for page in range(1, 100):
        response = requests.get(base_url + "?page=" + str(page)).json()
        if "items" in response:
            wanted_list.extend(response["items"])
        else:
            break
    return wanted_list

def get_image(image_url):
    image_name = image_url.split('/')[-1]
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Connection': 'keep-alive'}
    response = requests.get(image_url, headers=hdr)
    response_type = response.headers["content-type"].split('/')[-1]
    if response_type == "jpeg" or response_type == "jpg":
        if not image_name.split('.')[-1] == "jpg":
            image_name = image_name + ".jpg"
    elif response_type == "png":
        if not image_name.split('.')[-1] == "png":
            image_name = image_name + ".png"
    return image_name, response.content

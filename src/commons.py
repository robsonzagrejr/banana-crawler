import os
import json
import requests


def download_file(url, file_path):
    return
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)


def create_new_json(json_in, path_out):
    new_json = {}
    values = []
    os.makedirs(path_out, exist_ok=True)
    for key, value in json_in.items():
        image = ''
        sound = ''
        if value.get("image"):
            img = value.get("image")
            if ".png" in img or ".jpg" in img: 
                file_name = img.split("/")[-1]
                file_path = path_out + file_name
                download_file(img, file_path)
                image = file_name
            else:
                image = img
        if value.get("sound"):
            sd = value.get("sound")
            if ".mp3" in sd or ".wav" in sd:
                file_name = sd.split("/")[-1]
                file_path = path_out + file_name
                download_file(sd, file_path)
                sound = file_name
            else:
                sound = sd
        text = value['text_tl']
        values.append(text)
        new_json[key] = {
            "text_tl": text,
            "image": image,
            "sound": sound,
            "text_nl": value["text_nl"]
        }
    return new_json 
 

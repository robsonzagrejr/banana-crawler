import os
import json
import argparse
import requests


def download_file(url, file_path):
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
        image = []
        sound = []
        if value.get("image"):
            images = value.get("image")
            for img in images:
                if ".png" in img or ".jpg" in img: 
                    file_name = img.split("/")[-1]
                    file_path = path_out + file_name
                    download_file(img, file_name)
                    image.append(file_path)
                else:
                    image.append(img)
        if value.get("sound"):
            sounds = value.get("sound")
            for sd in sounds:
                if ".mp3" in sd or ".wav" in sd:
                    file_name = sd.split("/")[-1]
                    file_path = path_out + file_name
                    download_file(sd, file_path)
                    sound.append(file_name)
                else:
                    sound.append(sd)
        if image:
            text = "; ".join(value.get("text"))
            if text not in values:
                values.append(text)
                new_json[key] = {
                    "text": text,
                    "image": image,
                    "sound": sound
                }
    return new_json 
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_in",
        help="Input where the Korean Json is",
        type=str
    )
    parser.add_argument(
        "-o", "--file_out",
        help="Output where the Korean Json will be putted",
        type=str
    )
    parser.add_argument(
        "-d", "--download_path",
        help="Path of the dir that data will be downloaded",
        type=str
    )
    args = parser.parse_args()

    json_in = {}
    with open(args.file_in, "rb") as f:
        json_in = json.load(f)

    json_out = create_new_json(json_in, args.download_path)
    with open(args.file_out, "w") as f:
        json_in = json.dump(json_out, f, indent=4)


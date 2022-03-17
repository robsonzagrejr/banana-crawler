import os
import json
import argparse
import requests

from commons import create_new_json

url = 'https://www.russianforeveryone.com/RufeA/Lessons/Introduction/Alphabet/'

def postprocess_russian(json_in, path_out):
    organise_json = {}
    values = []
    idx = 0
    skip = True
    for key, value in json_in.items():
        if skip:
            skip = False
            continue
        if value['text'] and value['text'][0] not in values:
            values.append(value['text'][0])
            sound = value['sound'][0].split("'")[1]
            organise_json[idx] = {
                "text_tl": value['text'][0],
                "image": f"{url}{value['image'][1]}", 
                "sound": f"{url}{sound}",
                "text_nl": value['text'][2] + ' '+ ''.join(value['text'][3:-3]),
            }
        idx += 1
    new_json = create_new_json(organise_json, path_out)

    return new_json 
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_in",
        help="Input where the Russian Json is",
        type=str
    )
    parser.add_argument(
        "-o", "--file_out",
        help="Output where the Russian Json will be putted",
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

    json_out = postprocess_russian(json_in, args.download_path)
    with open(args.file_out, "w") as f:
        json_in = json.dump(json_out, f, indent=4)


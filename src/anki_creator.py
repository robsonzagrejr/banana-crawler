import os
import json
import argparse
import genanki


model= genanki.Model(
  1111,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyImage'}, 
    {'name': 'MySound'}, 
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<div style="font-sinze:100; text-align:center">{{Question}}<br>{{MyImage}}<br>{{MySound}}</div>',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ]
)


def gen_anki_note(id, text_tl, text_nl, image, sound):
    return genanki.Note(
        model=model,
        fields=[text_tl, text_nl, f"<img src='{image}'>", f"[sound:{sound}]"]
    )


def gen_anki_deck(data, deck_name, midia_path, file_name):
    deck_id = 10101
    deck = genanki.Deck(deck_id, deck_name)

    for note_id, note_data in data.items():
        deck.add_note(gen_anki_note(
            id=note_id,
            text_tl=note_data["text_tl"],
            text_nl=note_data["text_nl"],
            image=note_data["image"],
            sound=note_data["sound"],
        ))

    package = genanki.Package(deck)
    midia_files = [f"{midia_path}{f}" for f in os.listdir(midia_path)]
    package.media_files = midia_files
    package.write_to_file(f'{file_name}.apkg')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_in",
        help="Input in Json format that's will be use to generate anki deck",
        type=str
    )
    parser.add_argument(
        "-n", "--deck_name",
        help="Name of the anki deck",
        type=str
    )
    parser.add_argument(
        "-m", "--midia_path",
        help="Path that midia is downloaded",
        type=str
    )
    parser.add_argument(
        "-o", "--file_out",
        help="Name of the file that will be generated",
        type=str
    )
    args = parser.parse_args()

    json_in = {}
    with open(args.file_in, "rb") as f:
        json_in = json.load(f)

    gen_anki_deck(json_in, args.deck_name, args.midia_path, args.file_out)


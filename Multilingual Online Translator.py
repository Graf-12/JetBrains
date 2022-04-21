import sys

import requests

from bs4 import BeautifulSoup

args = sys.argv
my_language = args[1].lower()
need_language = args[2].lower()
word = args[3]
headers = {'User-Agent': 'Mozilla/5.0'}
languages = ["all", "arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch", "polish",
             "portuguese", "romanian", "russian", "turkish"]
count = 0
words = []
examples = {}

if my_language not in languages:
    print(f"Sorry, the program doesn't support {my_language}")
    sys.exit()
if need_language not in languages:
    print(f"Sorry, the program doesn't support {need_language}")
    sys.exit()


def examples_():
    x = examples.keys()
    count = 0
    for i in x:
        if count == 1:
            break
        else:
            print(f"{i}:")
            print(examples[i])
            print()
            count += 1


def translate():
    req = requests.get(url, headers=headers)
    if req.status_code == 404:
        print(f"Sorry, unable to find {args[3]}")
        sys.exit()
    assert req.status_code == 200, "Something wrong with your internet connection"
    soup = BeautifulSoup(req.content, "html.parser")
    translate_words = soup.find(id="translations-content")
    words.clear()
    examples.clear()
    for word in translate_words:
        a = word.text.strip()
        if a == "":
            continue
        else:
            words.append(a)
    example = soup.find(id="examples-content").find_all(class_="example")
    for ex in example:
        b = ex.find(class_="src ltr").text.strip()
        c = ex.find(class_="src ltr").find_next_sibling().text.strip()
        examples[b] = c


with open(f"{word}.txt", "w") as file:
    if need_language == "all":
        for i in languages[1:]:
            if i == my_language:
                continue
            else:
                url = f"https://context.reverso.net/translation/{my_language}-{i}/{word}"
                translate()
                print()
                print(f"{i} Translations:")
                print(words[0])
                print()
                print(f"{i} Example:")
                examples_()
                file.write(f"{i} Translations:\n")
                file.write(f"{words[0]}\n")
                file.write("\n")
                file.write(f"{i} Example:\n")
                x = list(examples)
                file.write(f"{x[0]}:\n")
                file.write(f"{examples[x[0]]}\n\n\n")

    else:
        url = f"https://context.reverso.net/translation/{my_language}-" \
              f"{need_language}/{word}"
        translate()
        print()
        print(f"{need_language} Translations:")
        print(words[0])
        print()
        print(f"{need_language} Example:")
        examples_()
        file.write(f"{need_language} Translations:\n")
        file.write(f"{words[0]}\n")
        file.write("\n")
        file.write(f"{need_language} Example:\n")
        x = list(examples)
        file.write(f"{x[0]}:\n")
        file.write(f"{examples[x[0]]}\n\n\n")

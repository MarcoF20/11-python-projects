import re


text = input("Escribe algo que pienses:")


def wordCounter(text):
    str(text)
    if (len(text) != 0):
        trimmed_words = text.strip()
        text_no_blankspace = re.sub(' +', ' ', text)
        separated_words = text_no_blankspace.split(" ")
        print(f"Tu texto tiene {len(separated_words)} palabra/s!")
    else:
        print("Parece que no escribiste alguna palabra")


wordCounter(text)

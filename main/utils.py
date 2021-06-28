import math


def safe_html_trim(note):
    note_length = len(note)
    if len(note) <= 2000:
        return note
    else:
        quarter_of_note = math.floor(0.45*note_length)
        excerpt = note[:quarter_of_note]
        last_index = excerpt.rindex('</')
        if last_index != -1:
            return note[:last_index] + '...'

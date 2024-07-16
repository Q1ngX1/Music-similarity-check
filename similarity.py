from third_party.pretty_midi import PrettyMIDI
import numpy as np


def calculate_similarity(original_midi, generated_midi):
    # 读取MIDI文件
    original = PrettyMIDI(original_midi)
    generated = PrettyMIDI(generated_midi)


    original_notes = []
    generated_notes = []
    for instrument in original.instruments:
        for note in instrument.notes:
            original_notes.append((note.pitch, note.start, note.end))
    for instrument in generated.instruments:
        for note in instrument.notes:
            generated_notes.append((note.pitch, note.start, note.end))


    original_notes.sort()
    generated_notes.sort()
    distance = np.abs(len(original_notes) - len(generated_notes)) + \
               np.sum(np.minimum(np.abs(np.array(original_notes) - np.array(generated_notes)), axis=1))


    max_length = max(len(original_notes), len(generated_notes))
    similarity = (1 - distance / max_length) * 100

    return similarity


original_midi_path = 'path_to_original_midi_file.mid'
generated_midi_path = 'path_to_generated_midi_file.mid'
similarity_percentage = calculate_similarity(original_midi_path, generated_midi_path)
print(f"The similarity index is: {similarity_percentage:.2f}%")
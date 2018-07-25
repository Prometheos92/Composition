import os, mido


def midi2keyboard():
    """takes path to midi file and converts it to a keyboard file for NNs"""
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    track.append(mido.MetaMessage('set_tempo', tempo=4000000, time=0))
    track.append(mido.Message('note_on', note=75, velocity=64, time=0))
    track.append(mido.Message('note_off', note=75, velocity=64, time=64))
    track.append(mido.Message('note_on', note=73, velocity=64, time=0))
    track.append(mido.Message('note_off', note=73, velocity=64, time=64))
    track.append(mido.Message('note_on', note=72, velocity=64, time=0))
    track.append(mido.Message('note_off', note=72, velocity=64, time=64))
    track.append(mido.Message('note_on', note=73, velocity=64, time=0))
    track.append(mido.Message('note_off', note=73, velocity=64, time=64))
    track.append(mido.Message('note_on', note=76, velocity=64, time=0))
    track.append(mido.Message('note_off', note=76, velocity=64, time=256))
    mid.save('new_song.mid')


def keyboard2midi():
    mid = mido.MidiFile('dies4c_IsaeMozart1.mid')
    mymid = mido.MidiFile()
    track1 = mid.tracks[0]
    track1[0] = mido.MetaMessage('set_tempo', tempo=1600000, time=0)
    track2 = mid.tracks[1]
    mymid.tracks.append(track1)
    mymid.tracks.append(track2)
    mymid.save('onevoice.mid')
    print(1)


keyboard2midi()
#midi2keyboard()
from pydub import AudioSegment
from pydub.generators import Sine

# Parameters
frequency = 2000  # Frequency of the tone in Hz (higher values are shriller)
duration_ms = 30000  # Duration of the tone in milliseconds
volume_in_db = 20  # Volume in decibels

# Generate the tone
tone = Sine(frequency).to_audio_segment(duration=duration_ms)

# Increase the volume to make it loud
loud_tone = tone + volume_in_db

# Export the tone to a file
loud_tone.export("shrill_tone.wav", format="wav")

print("Shrill tone generated and saved as 'shrill_tone.wav'")

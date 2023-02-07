import pyaudio
import wave
import const
import warnings

warnings.filterwarnings("ignore")


def recording():
    p = pyaudio.PyAudio()
    stream = p.open(format=const.FORMAT,
                    channels=const.CHANNELS,
                    rate=const.RATE,
                    input=True,
                    #input_device_index=3,
                    frames_per_buffer=const.CHUNK)
    print("* recording")

    frames = []
    for i in range(0, int(const.RATE / const.CHUNK * const.RECORD_SECONDS)):
        data = stream.read(const.CHUNK, exception_on_overflow = False)
        frames.append(data)
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(const.WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(const.CHANNELS)
    wf.setsampwidth(p.get_sample_size(const.FORMAT))
    wf.setframerate(const.RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

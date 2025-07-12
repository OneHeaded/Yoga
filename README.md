# 🎙️ YOGA - Voice-Controlled Virtual Assistant

YOGA is a Python-based virtual assistant designed to respond to voice commands and execute simple tasks such as web browsing, audio playback, and file operations.

## 🚀 Features

- 🔗 Open popular websites like Google and YouTube
- 🎶 Play songs defined in `musicLib.py`
- 🗒️ Record voice notes and store them in a `.txt` file
- 📖 Read the contents of the `.txt` file aloud
- 🧹 Format (clear) the contents of the file
- 💬 Respond to basic user questions like “What are you doing?”

## 🛠️ Requirements

Install necessary modules with:

```bash
pip install speechrecognition pyttsx3
```

> Make sure `musicLib.py` is available and contains a dictionary named `music` mapping song names to URLs.

## 🧠 How to Use

To activate the assistant, say: "YOGA"

Once active, try the following voice commands:

| Command           | Action                                       |
|------------------|----------------------------------------------|
| `Open Google`     | Opens Google in your browser                 |
| `Open YouTube`    | Opens YouTube in your browser                |
| `Play <song>`     | Plays the song from `musicLib.py`           |
| `Open Book`       | Records a voice note and appends to `demo.txt` |
| `Read`            | Reads out contents of `demo.txt`            |
| `Format`          | Clears all contents of `demo.txt`           |
| `What are you doing?` | Assistant gives a witty response      |

## 🔊 Voice Customization

Change the voice output by modifying:

```python
engine.setProperty('voice', voices[1].id)
```

Try values `0`, `1`, or `2` for different voice types.

## 📓 Note Storage

Your notes are stored in `demo.txt`. The assistant can:
- Append new notes via voice
- Read all existing notes
- Format (erase) the file

## 💡 Expandability

Want to build more?
- Integrate OpenAI’s API for smarter Q&A
- Enhance TTS with Google Cloud API
- Add more voice commands and intents

## 📎 Misc Notes

- Microphone permissions are essential
- Tune the timeout values in `listen()` for responsiveness
- Speech recognition relies on ambient noise calibration

---

Made witH Python. Explore, expand, and enjoy!
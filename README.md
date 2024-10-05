
```markdown
# GenAi-Project by SaiAryan1784

Welcome to **GenAi-hackathon-Blurock**, a transcription and modification app that allows users to upload audio or video files, transcribe them, modify the transcriptions, and save them directly to Google Docs. This application leverages the power of OpenAI's Whisper for transcription and Groq for text modifications.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)
- [Contributing](#contributing)

## Features
- **Audio/Video Upload:** Upload both audio and video files for transcription.
- **Transcription:** Uses Whisper to transcribe audio to text.
- **Text Modification:** Modify the transcription using Groq AI.
- **Save to Google Docs:** Save the modified transcription directly to your Google Docs.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GenAi-hackathon-Blurock.git
   cd GenAi-hackathon-Blurock
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Open your web browser and navigate to:
   ```plaintext
   http://127.0.0.1:5000
   ```

3. Upload your audio or video file using the "Upload Audio File" button.

4. Wait for the transcription process to complete. The transcription will automatically display in the text area after 2-3 minutes.

5. Enter your modification instructions in the "Modify Transcription" section and click "Modify".

6. Once modified, you can click the "Save to Google Docs" button to save the document.

## How It Works
The application uses Flask as a web framework, OpenAI's Whisper for transcription, and Groq for text modification. When an audio or video file is uploaded, it is processed, and the transcription is displayed. You can then modify the transcription and save it to Google Docs, making it an efficient tool for managing transcribed content.

## License
This project is licensed under the MIT License.

## Contributing
We welcome contributions! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---

Feel free to adjust the text to match your project specifics, especially in the sections for **License** and **Contributing**. Let me know if you need any more customization or additions!

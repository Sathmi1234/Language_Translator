# Language Translator Chatbot

A modern, web-based translation application that combines an interactive chatbot interface with powerful multi-language translation capabilities.

## Overview

Language Translator is a full-stack application built with **FastAPI** (backend) and **HTML/CSS/JavaScript** (frontend) that allows users to translate text between multiple languages in real-time. The application features automatic language detection and a beautiful, responsive chatbot interface.

## Features

- ✨ **Real-time Translation** - Instantly translate text to multiple target languages
- 🌍 **Automatic Language Detection** - Automatically detects the source language of input text
- 💬 **Interactive Chat Interface** - Clean, modern chatbot UI with message animations
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🔄 **CORS Enabled** - Backend configured for cross-origin requests
- 🎨 **Modern UI** - Gradient backgrounds, smooth animations, and intuitive layout

## Technology Stack

### Frontend
- **HTML5** - Structure and markup
- **CSS3** - Styling with gradients and animations
- **JavaScript** - Client-side logic and API communication

### Backend
- **FastAPI** - High-performance Python web framework
- **Pydantic** - Data validation using Python type hints
- **deep_translator** - Google Translate integration
- **langdetect** - Source language detection
- **CORS Middleware** - Cross-origin resource sharing support

## Project Structure

```
Language_Translator/
├── index.html          # Frontend chatbot interface
├── main.py             # FastAPI application and routes
├── translator.py       # Translation logic and language detection
└── README.md           # This file
```

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd Language_Translator
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn deep_translator langdetect python-multipart
   ```

## Running the Application

### Start the Backend Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Access the Frontend

Open `index.html` in your web browser 

## API Endpoints

### 1. Home Endpoint
- **URL**: `GET /`
- **Description**: Health check endpoint
- **Response**: 
  ```json
  {
    "message": "Translator Chatbot is running 🚀"
  }
  ```

### 2. Translation Endpoint
- **URL**: `POST /translate`
- **Description**: Translates text to target language with automatic source language detection
- **Request Body**:
  ```json
  {
    "text": "Hello, how are you?",
    "target_language": "es"
  }
  ```
- **Response**:
  ```json
  {
    "bot_message": "I translated it for you 😊",
    "translation": "Hola, ¿cómo estás?"
  }
  ```

## Supported Languages

The application supports all languages that Google Translate supports. Common language codes include:

- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ja` - Japanese
- `zh-CN` - Simplified Chinese
- `ar` - Arabic
- `ru` - Russian
- And many more...

## How to Use

1. **Start the backend server** (if not already running)
2. **Open the chatbot interface** in your browser
3. **Type your message** in the input field at the bottom
4. **Select your target language** from the language dropdown
5. **Click "Send"** or press Enter to translate
6. **View the translation** displayed in the chat interface

## Features in Detail

### Automatic Language Detection
The translator automatically detects the source language of your input using the `langdetect` library, so you don't need to manually specify it.

### Interactive Chat Interface
- Messages from you appear on the right with a purple gradient background
- Bot responses appear on the left with a white background
- Smooth fade-in animations for new messages
- Auto-scrolling chat window

### Responsive Design
The interface adapts to different screen sizes, making it usable on:
- Desktop browsers
- Tablets
- Mobile devices

## Development

### File Descriptions

**main.py**: FastAPI application
- Sets up the web server
- Defines API routes
- Handles CORS configuration
- Manages HTTP requests and responses

**translator.py**: Translation logic
- `translate_text()` function handles translation
- Uses GoogleTranslator for actual translation
- Detects source language automatically
- Returns structured translation data

**index.html**: Frontend interface
- Complete HTML, CSS, and JavaScript in one file
- Asynchronous communication with backend API
- Real-time message display
- Language selection dropdown

## Error Handling

The application includes error handling for:
- Invalid language codes
- Network errors
- Empty input text
- API communication failures

## Future Enhancements

Potential improvements for future versions:
- User preference saving
- Translation history
- Multiple API provider support
- Offline translation capability
- Text-to-speech integration
- File upload and translation
- Batch translation requests

## License

This project is open source and available for personal and educational use.

## Support

If you encounter any issues:
1. Ensure all dependencies are installed correctly
2. Verify the FastAPI server is running on port 8000
3. Check your internet connection (required for Google Translate)
4. Review browser console for any JavaScript errors

---

**Enjoy translating! 🌍**

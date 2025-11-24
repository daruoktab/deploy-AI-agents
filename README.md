# 🤖 AI Utility Agent

A production-ready AI agent powered by **GPT-5 Nano** and **LangGraph**, deployed on **Vercel**. This agent provides intelligent utility functions including calculations, text analysis, JSON formatting, and more.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)
![Vercel](https://img.shields.io/badge/Deployed-Vercel-black.svg)

## ✨ Features

The AI agent comes with 5 powerful tools:

- **🧮 Calculator** - Perform complex mathematical calculations with support for functions like sqrt, sin, cos, log, etc.
- **📊 Text Analyzer** - Get detailed statistics about any text (word count, reading time, sentence analysis)
- **📝 JSON Formatter** - Validate and beautify JSON strings
- **🕐 DateTime** - Get current date and time in UTC
- **🔤 Case Converter** - Convert text between different cases (camelCase, snake_case, kebab-case, etc.)

## 🚀 Live Demo

Visit the deployed application: [Your Vercel URL]

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **AI Framework**: LangChain + LangGraph
- **LLM**: OpenAI GPT-5 Nano
- **Frontend**: HTML/CSS/JavaScript (Vanilla)
- **Deployment**: Vercel Serverless Functions
- **Package Manager**: pip

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Vercel account (for deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/daruoktab/deploy-AI-agents.git
   cd deploy-AI-agents
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the development server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8000`

## 🌐 Deployment to Vercel

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Deploy

```bash
vercel --prod
```

### Step 3: Add Environment Variables

```bash
vercel env add OPENAI_API_KEY
```

When prompted:
- Paste your OpenAI API key
- Select all environments (Production, Preview, Development)

### Step 4: Redeploy

```bash
vercel --prod
```

Your app will be live at `https://your-project.vercel.app`

## 📖 Usage Examples

### Calculate
```
"What's 25 * 48 + sqrt(144)?"
"Calculate sin(pi/2)"
"What's 15% of 250?"
```

### Text Analysis
```
"Analyze this text: The quick brown fox jumps over the lazy dog"
"How many words are in this paragraph: [your text]"
```

### JSON Formatting
```
"Format this JSON: {name:'John',age:30,city:'NYC'}"
"Validate and prettify: {'key': 'value', 'nested': {'a': 1}}"
```

### Date & Time
```
"What's the current date and time?"
"Get current UTC time"
```

### Case Conversion
```
"Convert 'Hello World' to snake_case"
"Change 'user_profile_data' to camelCase"
"Transform 'MyClassName' to kebab-case"
```

## 🗂️ Project Structure

```
deploy-AI-agents/
├── agent.py              # AI agent with tools definition
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
├── vercel.json          # Vercel configuration
├── .env                 # Environment variables (local only)
├── .gitignore           # Git ignore rules
├── .vercelignore        # Vercel ignore rules
├── templates/
│   └── index.html       # Web interface
└── README.md            # This file
```

## 🔧 Configuration

### `vercel.json`

```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## 🧪 API Endpoints

### `GET /`
Returns the web interface (HTML page)

### `POST /agent`
Invoke the AI agent with a prompt

**Request Body:**
```json
{
  "prompt": "Calculate 25 * 48"
}
```

**Response:**
```json
{
  "response": "Result: 1200"
}
```

## 🎯 Why Serverless-Compatible Tools?

The original version used file-based tools (read/write notes), which don't work in Vercel's serverless environment because:

1. **Ephemeral Filesystem**: Each serverless function invocation gets a clean, temporary filesystem
2. **No State Persistence**: Files written during one request won't exist in the next request
3. **Read-Only**: The deployment directory is read-only

This version uses **stateless utility tools** that work perfectly in serverless environments.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the AI framework
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Vercel](https://vercel.com/) for serverless deployment
- [OpenAI](https://openai.com/) for GPT-5 Nano

## 📧 Contact

Daru Okta Buana - [@daruoktab](https://github.com/daruoktab)

Project Link: [https://github.com/daruoktab/deploy-AI-agents](https://github.com/daruoktab/deploy-AI-agents)

---

Made with ❤️ using LangGraph and FastAPI

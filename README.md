# GitHub Profile Analyzer MCP Server

An AI-powered GitHub Profile Analyzer built using **Python**, **FastMCP**, and the **GitHub REST API**.
This MCP server analyzes GitHub developers, repositories, programming languages, coding activity, and learning trends while providing AI-style insights and developer summaries.

Deployed remotely using **Render** with **SSE transport** for cloud-based MCP connectivity.

---

# 🚀 Features

## 👤 Profile Analysis

* GitHub username details
* Followers & following count
* Public repositories
* Account creation date
* Most active repositories

## 💻 Language Analysis

* Most used programming languages
* Language percentage breakdown
* Primary tech stack detection
* Language usage insights

## 📦 Repository Insights

* Most starred repository
* Most forked repository
* Largest repository
* Recently updated repositories
* Inactive repositories

## 📈 Activity Analysis

* Developer activity score
* Contribution consistency
* Weekly/monthly activity estimation
* Commit frequency insights

## 📚 Learning Rate Analysis

* Technology growth detection
* New tech adoption analysis
* Repository complexity evolution
* Learning trend estimation

## 🤖 AI Insights

* Developer summaries
* Skill gap detection
* Recommended technologies
* Project recommendations

## 📝 README Analyzer

* README quality scoring
* Missing documentation sections
* Improvement suggestions

## 😄 Fun Features

* GitHub roast mode
* Developer personality analysis
* “What type of developer are you?” summary

---

# 🛠 Tech Stack

* Python
* FastMCP
* GitHub REST API
* AsyncIO
* HTTPX
* Uvicorn
* SSE (Server-Sent Events)
* Render Cloud Deployment
* Claude Desktop MCP
* JSON APIs

---

# 📂 Project Structure

```bash id="lq8n31"
github-profile-analyzer/
│
├── server.py
├── tools/
│   ├── profile_tools.py
│   ├── language_tools.py
│   ├── activity_tools.py
│   ├── repo_tools.py
│   └── ai_tools.py
│
├── services/
│   ├── github_api.py
│   ├── analyzer.py
│   └── ai_service.py
│
├── utils/
│   ├── helpers.py
│   └── formatter.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚡ MCP Tools

| Tool                      | Description                   |
| ------------------------- | ----------------------------- |
| `analyze_profile`         | Analyze GitHub profile        |
| `analyze_languages`       | Analyze programming languages |
| `repo_insights`           | Repository intelligence       |
| `activity_score`          | Developer activity analysis   |
| `learning_rate`           | Learning trend analysis       |
| `generate_summary`        | AI developer summary          |
| `github_roast`            | Fun GitHub roast mode         |
| `project_recommendations` | AI project suggestions        |

---

# 🌐 Live MCP Endpoint

```txt id="9mxq22"
https://github-profile-analyzer-jm21.onrender.com/sse
```

---

# 🔗 Claude Desktop MCP Configuration

Add this to your `claude_desktop_config.json`:

```json id="p7vm40"
{
  "mcpServers": {
    "github-analyzer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://github-profile-analyzer-jm21.onrender.com/sse"
      ]
    }
  }
}
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash id="d2ms81"
git clone https://github.com/Developer007-web/github-profile-analyzer.git
```

---

## 2. Navigate to Project

```bash id="xk2u71"
cd github-profile-analyzer
```

---

## 3. Create Virtual Environment

```bash id="m5fj20"
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```powershell id="r4aa71"
.\venv\Scripts\Activate.ps1
```

### Linux/Mac

```bash id="u7cq82"
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash id="t9nv33"
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env`

```env id="c3qp19"
GITHUB_TOKEN=your_github_token
```

---

# ▶️ Run Locally

```bash id="z7jw44"
python server.py
```

---

# ☁️ Cloud Deployment

This project is deployed using:

* [Render](https://render.com?utm_source=chatgpt.com)

Deployment uses:

* SSE transport
* Uvicorn server
* FastMCP remote hosting

---

# 🧠 Example Usage

```txt id="k4wq55"
Use analyze_profile for "torvalds"
```

```txt id="v8pr12"
Use github_roast for "octocat"
```

```txt id="s1dx88"
Use analyze_languages for "gaearon"
```

---

# 🏗 Architecture

```txt id="y2tn30"
Claude Desktop
       ↓
MCP Protocol
       ↓
FastMCP Server
       ↓
GitHub REST API
       ↓
AI Analysis Engine
       ↓
Structured JSON Responses
```

---

# 🔒 Security

* API keys stored using `.env`
* `.gitignore` protects secrets
* GitHub tokens never exposed publicly

---

# 📌 Future Improvements

* GitHub Battle Mode
* Compare Developers
* AI README Review
* Contribution Heatmaps
* React Dashboard
* Resume Generator
* OpenAI/Gemini Integration

---

# 👨‍💻 Author

**Aman Pratap Singh**

GitHub:
[Developer007-web](https://github.com/Developer007-web?utm_source=chatgpt.com)

---

# ⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Share feedback
* Contribute improvements

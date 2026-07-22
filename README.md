<div align="center">

# 🎓 Campus Helpdesk Assistant

### AI-Powered Multi-Agent Campus Support Platform using RAG, FastAPI, React & ChromaDB

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/React-18-20232A?style=for-the-badge&logo=react"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-VectorDB-blueviolet?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LangGraph-Multi--Agent-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-LPU-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LLaMA-3.3--70B-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Firebase-Authentication-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>

</p>

<p align="center">

<img src="https://img.shields.io/github/license/prakashprajapati-git/campus-helpdesk-assistant?style=flat-square"/>
<img src="https://img.shields.io/github/last-commit/prakashprajapati-git/campus-helpdesk-assistant?style=flat-square"/>
<img src="https://img.shields.io/github/repo-size/prakashprajapati-git/campus-helpdesk-assistant?style=flat-square"/>
<img src="https://img.shields.io/github/languages/top/prakashprajapati-git/campus-helpdesk-assistant?style=flat-square"/>

</p>

</div>

---

## 📖 Overview

**Campus Helpdesk Assistant** is a production-grade AI-powered campus support platform developed during my internship at **NathCorp** for **Amity University Jharkhand**.

The platform enables students to interact with university resources through natural language conversations while providing administrators with a centralized dashboard for document management, notices, grievance tickets, and campus support.

Unlike conventional chatbots, the application leverages a **Multi-Agent Retrieval-Augmented Generation (RAG) architecture** that intelligently classifies user intent, retrieves semantically relevant information from institutional documents, validates generated responses, and escalates low-confidence queries whenever necessary.

The system combines **FastAPI**, **React**, **LangGraph**, **ChromaDB**, **Groq LLaMA 3.3-70B**, **Firebase Authentication**, and **WebSocket-based real-time communication** to deliver a scalable enterprise-style AI application.

---

## ✨ Key Highlights

- 🤖 Multi-Agent RAG architecture built using **LangGraph**
- 📄 Semantic document search powered by **ChromaDB**
- 🧠 Groq LLaMA 3.3 70B for ultra-fast inference
- 🔍 Source-grounded AI responses with verification workflow
- 🎫 Intelligent ticket generation from student conversations
- 🔔 Campus notice management system
- 📚 Knowledge Base PDF ingestion pipeline
- 👨‍💼 Enterprise Admin Dashboard
- 🔐 Firebase Google Authentication
- ⚡ WebSocket-powered live ticket synchronization
- 📱 Responsive React + Tailwind frontend
- 🚀 Production-ready FastAPI backend

---

# 📑 Table of Contents

- [🎯 Project Goals](#-project-goals)
- [📌 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
  - [🤖 AI-Powered Student Assistant](#-ai-powered-student-assistant)
  - [🎓 Student Portal](#-student-portal)
  - [🛠️ Administrative Portal](#️-administrative-portal)
  - [⚡ AI & Backend Features](#-ai--backend-features)
- [🏗️ System Architecture](#️-system-architecture)
- [📸 Application Screenshots](#-application-screenshots)
  - [🏠 Landing Page](#-landing-page)
  - [👨‍🎓 Student Login](#-student-login)
  - [🤖 AI Campus Assistant](#-ai-campus-assistant)
  - [📢 Campus Notice Board](#-campus-notice-board)
  - [🎫 Student Ticket Management](#-student-ticket-management)
  - [🛠️ Administrative Dashboard](#️-administrative-dashboard)
  - [👥 Administrator Management](#-administrator-management)
  - [🤖 Administrative AI Assistant](#-administrative-ai-assistant)
- [🛠️ Technology Stack](#️-technology-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
- [⚙️ Backend Setup](#️-backend-setup)
- [💻 Frontend Setup](#-frontend-setup)
- [🔑 Environment Variables](#-environment-variables)
- [🔮 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)
- [👨‍💻 Author](#-author)
- [⭐ Support](#-support)

---

## 🎯 Project Goals

The primary objective of this project was to build a production-style AI helpdesk capable of answering campus-related queries using university documents instead of relying solely on Large Language Models.

The platform was designed with the following goals:

- Reduce repetitive student support queries
- Provide document-grounded AI responses
- Automate grievance ticket creation
- Offer real-time communication between students and administrators
- Enable administrators to manage campus notices and documents
- Demonstrate enterprise-scale AI system design using modern technologies

---

---

# 📌 Project Overview

Campus Helpdesk Assistant is an AI-powered support platform designed to streamline campus communication and administrative services for students and staff. Instead of navigating multiple portals or waiting for manual responses, users can interact with an intelligent chatbot that retrieves accurate information from institutional documents and performs administrative actions in real time.

The system combines **Retrieval-Augmented Generation (RAG)** with a **Multi-Agent Architecture** to deliver context-aware, reliable, and production-ready assistance. Students can instantly access academic policies, notices, and support services, while administrators can efficiently manage tickets, broadcast announcements, and maintain the institutional knowledge base.

Built using **LangGraph**, **FastAPI**, **React**, **Firebase Authentication**, and **ChromaDB**, the application demonstrates modern AI engineering principles including semantic search, workflow orchestration, real-time communication, and scalable backend architecture.

---

# ✨ Key Features

## 🤖 AI-Powered Student Assistant

- 💬 Natural language conversations powered by Large Language Models
- 📚 Retrieval-Augmented Generation (RAG) for accurate document-based responses
- 🔍 Semantic search over institutional knowledge base
- 📖 Source-backed answers with citation references
- 📝 Persistent conversation history

---

## 🎓 Student Portal

- 🔐 Secure Email & Google Authentication
- 📢 Campus notice board with categorized announcements
- 🎫 Complaint and support ticket management
- 📈 Ticket lifecycle tracking
- 💬 Intelligent campus assistant for instant help

---

## 🛠️ Administrative Portal

- 👥 Role-based administrator access
- 📚 Knowledge Base management
- 📤 Broadcast notices across campus
- 🎫 Ticket moderation and status updates
- 🤖 AI assistant for institutional document retrieval
- 👤 Administrator management

---

## ⚡ AI & Backend Features

- 🧠 Multi-Agent workflow using LangGraph
- 📄 Retrieval-Augmented Generation (RAG)
- 🔍 Vector similarity search with ChromaDB
- ⚡ FastAPI REST backend
- 🔄 WebSocket-based real-time updates
- 🔐 Firebase Authentication
- 🗂️ PostgreSQL database integration

---

# 🏗️ System Architecture

<p align="center">
  <img src="assets/architecture.png" alt="System Architecture" width="100%">
</p>

The platform follows a modern multi-layer architecture consisting of:

- **React Frontend** for responsive user interaction
- **FastAPI Backend** exposing REST APIs and WebSocket services
- **LangGraph Multi-Agent Engine** for intelligent workflow orchestration
- **RAG Pipeline** for context-aware document retrieval
- **ChromaDB** for semantic vector search
- **PostgreSQL** for transactional application data
- **Firebase Authentication** for secure identity management
- **LLM Integration** for natural language understanding and response generation

The modular design enables scalability, maintainability, and clear separation between user interface, business logic, AI orchestration, and persistent storage.

---

# 📸 Application Screenshots

## 🏠 Landing Page

<p align="center">
  <img src="assets/landing-page.png" alt="Landing Page" width="100%">
</p>

The landing page provides a clean entry point for both students and administrators, featuring secure authentication options and a modern AI-powered interface.

---

## 👨‍🎓 Student Login

<table>
<tr>
<td width="50%">

### Email Authentication

<img src="assets/student-email-login.png" alt="Student Email Login">

</td>

<td width="50%">

### Admin Authentication

<img src="assets/admin-login.png" alt="Admin Login">

</td>
</tr>
</table>

Secure authentication is powered by Firebase Authentication, supporting institutional email login and administrator access with role-based authorization.

---

## 🤖 AI Campus Assistant

<p align="center">
  <img src="assets/student-chat.png" alt="Student AI Assistant" width="100%">
</p>

Students can interact with an AI-powered campus assistant that retrieves accurate information from institutional documents using Retrieval-Augmented Generation (RAG). Every response is supported with document citations, ensuring reliable and transparent answers.

---

## 📢 Campus Notice Board

<p align="center">
  <img src="assets/student-notices.png" alt="Campus Notice Board" width="100%">
</p>

A centralized bulletin board enables students to browse categorized announcements, academic updates, placement notifications, events, and administrative notices through an intuitive interface.

---

## 🎫 Student Ticket Management

<p align="center">
  <img src="assets/student-ticket-dashboard.png" alt="Student Ticket Dashboard" width="100%">
</p>

Students can create support requests, monitor ticket status, review communication history, and track the complete lifecycle of each issue from submission to resolution.

---

## 🛠️ Administrative Dashboard

<p align="center">
  <img src="assets/admin-dashboard.png" alt="Admin Dashboard" width="100%">
</p>

The administrative control panel provides a unified interface for ticket moderation, knowledge base management, broadcast announcements, and institutional administration.

---

## 👥 Administrator Management

<p align="center">
  <img src="assets/admin-user-management.png" alt="Administrator Management" width="100%">
</p>

Authorized administrators can securely manage system access by adding new administrators and maintaining role-based permissions.

---

## 🤖 Administrative AI Assistant

<p align="center">
  <img src="assets/admin-chat.png" alt="Administrative AI Assistant" width="100%">
</p>

Administrators can leverage the AI assistant to retrieve policy information, summarize institutional documents, and access knowledge from the campus database using semantic search and Retrieval-Augmented Generation.

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| **Frontend** | React, TypeScript, Vite, Tailwind CSS |
| **Backend** | FastAPI, Python |
| **AI Framework** | LangGraph, LangChain |
| **Large Language Model** | Llama 3 (Groq API) |
| **Vector Database** | ChromaDB |
| **Database** | PostgreSQL |
| **Authentication** | Firebase Authentication |
| **Real-Time Communication** | WebSockets |
| **Document Processing** | PyPDF, Recursive Text Splitter |
| **Deployment Ready** | Docker, Uvicorn |
| **Version Control** | Git & GitHub |

---

# 📂 Project Structure

```text
campus-helpdesk-assistant/
│
├── assets/                     # README images and project visuals
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── services/
│   │   ├── websocket/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── chroma_db/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── contexts/
│   │   └── App.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Git

---

## Clone the Repository

```bash
git clone https://github.com/prakashprajapati-git/campus-helpdesk-assistant.git

cd campus-helpdesk-assistant
```

---

# ⚙️ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

Backend will be available at:

```
http://localhost:8000
```

---

# 💻 Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend will be available at:

```
http://localhost:5173
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

```env
DATABASE_URL=your_database_url

GROQ_API_KEY=your_groq_api_key

FIREBASE_PROJECT_ID=your_project_id

FIREBASE_API_KEY=your_api_key

CHROMA_DB_DIRECTORY=./chroma_db
```

Update the values according to your local configuration.

---

# 🔮 Future Enhancements

The project has been designed with scalability in mind. Some planned improvements include:

- 🔔 Real-time push notifications for important campus announcements
- 📱 Mobile application for Android and iOS
- 🌐 Multi-language support for regional accessibility
- 📅 Academic calendar and timetable integration
- 🎓 Student profile personalization
- 📊 Analytics dashboard for administrators
- 🤖 AI-powered ticket prioritization and categorization
- 📂 OCR support for scanned PDF documents
- 🔍 Hybrid Search (Vector + Keyword Search)
- ☁️ Cloud-native deployment with Kubernetes

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve the project:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add your feature"
```

4. Push the branch

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

Please ensure that your code follows the existing project structure and coding conventions.

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more details.

---

# 🙏 Acknowledgements

This project was built using several outstanding open-source technologies.

Special thanks to the communities behind:

- FastAPI
- React
- LangGraph
- LangChain
- ChromaDB
- PostgreSQL
- Firebase
- Tailwind CSS
- Vite
- Groq
- GitHub

Their tools and documentation made this project possible.

---

# 👨‍💻 Author

**Prakash Kumar Prajapati**

- GitHub: [prakashprajapati-git](https://github.com/prakashprajapati-git)
- LinkedIn: [Prakash Kumar Prajapati](https://linkedin.com/in/prakash-kumar-prajapati-026101306)

---

# ⭐ Support

If you found this project useful or interesting:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🐞 Report bugs
- 💡 Suggest new features

Your support helps improve the project and encourages future development.

---

<p align="center">

### ⭐ If you like this project, consider giving it a Star ⭐

Built with ❤️ using FastAPI, React, LangGraph, ChromaDB, PostgreSQL & LLMs.

</p>

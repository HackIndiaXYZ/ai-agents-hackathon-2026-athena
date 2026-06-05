# Ai-Agents-Hackathon-2026-Athena
Hackathon team repository for Athena - [hackindia-team:ai-agents-hackathon-2026:athena]

# 🎓 TutorPilot AI

## Multilingual Adaptive STEM Tutor using RAG and Generative AI

TutorPilot AI is an intelligent learning platform that provides personalized STEM education through Retrieval-Augmented Generation (RAG), adaptive assessments, and AI-powered tutoring. The platform helps students learn complex concepts, evaluate their understanding, and receive customized learning recommendations based on their performance.

---

## Problem Statement

Students often struggle with STEM subjects due to:

* Lack of personalized learning support
* Limited access to instant doubt resolution
* One-size-fits-all educational resources
* Absence of adaptive learning pathways
* Insufficient progress tracking and performance analysis

TutorPilot AI addresses these challenges by providing an interactive, multilingual, and adaptive learning environment powered by Artificial Intelligence.

---

## Solution Overview

TutorPilot AI combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and learning analytics to create a personalized educational experience.

The platform:

1. Answers STEM-related questions using an AI Tutor.
2. Retrieves relevant educational content from a custom knowledge base.
3. Generates topic-specific quizzes.
4. Evaluates student performance.
5. Creates adaptive learning plans.
6. Tracks learning progress over time.

---

## Key Features

### 🤖 AI Tutor

* Answers STEM questions in natural language.
* Uses Gemini AI for intelligent explanations.
* Supports multilingual educational content.

### 📚 Retrieval-Augmented Generation (RAG)

* Retrieves relevant learning materials from a STEM knowledge base.
* Uses ChromaDB vector search.
* Improves factual grounding and contextual relevance.

### 📝 AI Quiz Generator

* Dynamically generates quizzes.
* Supports multiple difficulty levels.
* Topic-specific assessment generation.

### 📊 Performance Evaluation

* Calculates student performance metrics.
* Categorizes learners into skill levels.
* Provides actionable feedback.

### 🎯 Adaptive Learning Planner

* Creates personalized learning pathways.
* Recommends next learning steps based on performance.
* Encourages continuous improvement.

### 📈 Progress Analytics

* Stores assessment history.
* Tracks learning growth over time.
* Visualizes performance trends.

---

## System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ├── AI Tutor
 ├── Quiz Generator
 ├── Progress Dashboard
 │
 ▼
TutorPilot Backend
 │
 ├── Teacher Agent
 ├── Quiz Generator Agent
 ├── Evaluator Agent
 └── Learning Planner Agent
 │
 ▼
RAG Layer
 │
 ├── ChromaDB
 ├── Embeddings
 └── Retrieval Engine
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
Personalized Responses
```

---

## Technology Stack

| Category        | Technology            |
| --------------- | --------------------- |
| Frontend        | Streamlit             |
| LLM             | Gemini 2.5 Flash      |
| Vector Database | ChromaDB              |
| Embeddings      | Sentence Transformers |
| Database        | SQLite                |
| Data Processing | Pandas                |
| Language        | Python                |
| Visualization   | Matplotlib            |

---

## Project Structure

```text
TutorPilot/
│
├── agents/
│   ├── teacher.py
│   ├── quiz_generator.py
│   ├── evaluator.py
│   └── planner.py
│
├── rag/
│   ├── vector_store.py
│   └── retrieval.py
│
├── database/
│   └── db.py
│
├── data/
│   └── stem_dataset.csv
│
├── chroma_db/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd TutorPilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Build Vector Database

```bash
python rag/vector_store.py
```

### Run Application

```bash
streamlit run main.py
```

---

## Usage

### AI Tutoring

Ask STEM-related questions and receive contextual explanations.

### Quiz Generation

Generate quizzes based on topic and difficulty level.

### Performance Evaluation

Analyze quiz performance and determine learning level.

### Adaptive Planning

Receive personalized recommendations for future learning.

### Progress Tracking

Monitor historical learning performance through analytics.

---

## Future Enhancements

* Voice-based tutoring
* OCR for handwritten problem solving
* Real-time collaborative learning
* Advanced learner profiling
* Gamification and achievement badges
* Multi-user authentication
* Cloud deployment
* Teacher analytics dashboard

---

## Impact

TutorPilot AI aims to make quality STEM education:

* More accessible
* More personalized
* More engaging
* More data-driven
* More adaptive to individual learning needs

---

## Authors

Kavya Sahu

---

## License

This project is developed for educational and hackathon purposes.

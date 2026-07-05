# Disaster Relief Hub Coordinator

An AI-powered multi-agent disaster management system that helps emergency response teams coordinate relief operations efficiently during disasters like floods, cyclones, earthquakes, and tsunamis.

---

# Project Overview

Disaster Relief Hub Coordinator uses a multi-agent workflow to analyze emergency situations, allocate resources, fetch live weather intelligence, identify safe routes, and generate AI-powered recommendations in real time.

This project was built for the **Agents for Good** track.

---

# Problem Statement

During large-scale disasters, emergency teams face challenges such as:

* Slow emergency analysis
* Inefficient resource allocation
* Lack of real-time weather intelligence
* Unsafe transportation routes
* Delayed decision making

This system automates these operations using AI agents to improve disaster response coordination.

---

# Features

* AI-based disaster severity analysis
* Dynamic resource allocation from warehouses
* Live weather intelligence using OpenWeather API
* Route intelligence with blocked route detection
* AI-generated disaster response recommendations
* Severity color indicators
* Warehouse memory management
* Restock warehouse functionality
* Real-time frontend dashboard

---

# Multi-Agent Architecture

The system consists of multiple collaborating AI agents:

### 1. Triage Agent

Analyzes disaster prompts and extracts:

* severity
* affected people
* required resources
* constraints

### 2. Resource Matching Agent

Allocates available resources from warehouses dynamically.

### 3. Weather Intelligence Agent

Fetches live weather conditions using OpenWeather API.

### 4. Route Intelligence Agent

Identifies safe routes and blocked transportation paths.

### 5. Recommendation Agent

Generates final AI-powered disaster response recommendations.

---

# Workflow

User Prompt
⬇
Triage Agent
⬇
Resource Matching Agent
⬇
Weather Intelligence Agent
⬇
Route Intelligence Agent
⬇
Recommendation Agent
⬇
Final Disaster Response Output

---

# Tech Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python
* FastAPI

## APIs & AI

* Groq API
* OpenWeather API

## Concepts Used

* Multi-Agent Systems
* Workflow Orchestration
* Tool Integration
* Memory Management
* AI Reasoning

---

# Project Structure

```bash
Disaster Relief Hub Coordinator/
│
├── api/
│   └── app.py
│
├── agents/
│   ├── triage_agent.py
│   ├── matcher_agent.py
│   ├── weather_agent.py
│   ├── route_agent.py
│   └── recommendation_agent.py
│
├── orchestration/
│   └── workflow.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── warehouse.json


```

---

# Setup Instructions

## 1. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

# Run Backend

```bash
uvicorn api.app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# Run Frontend

Open `frontend/index.html` using Live Server in VS Code.

Frontend URL:

```text
http://127.0.0.1:5500
```

---

# Example Disaster Prompts

## Green Low Severity

```text
Small fire accident in Hyderabad affecting 20 people.
```

## Yellow Medium Severity

```text
Moderate flood in Pune affecting 500 people.
```

## Light Red High Severity

```text
Severe cyclone in Chennai affecting 5000 people.
```

## Dark Red Critical Severity

```text
Massive tsunami in Andhra Pradesh affecting 30000 people.
```

---

#  Security

* API keys stored securely using `.env`
* Secrets excluded using `.gitignore`
* No sensitive data exposed publicly

---

# Evaluation

The system was tested using multiple disaster scenarios:

* floods
* earthquakes
* cyclones
* tsunamis

Evaluation focused on:

* severity detection
* resource allocation accuracy
* weather intelligence
* route generation
* AI recommendation quality

---

# Demo Highlights

* Multi-agent workflow
* Live disaster analysis
* Dynamic warehouse updates
* Real-time weather intelligence
* Route recommendations
* AI-generated response planning

---

# License

This project is created for educational and hackathon purposes.

# 🚀 Day 5 – GitHub Profile Analyzer

A Python-based tool that analyzes a GitHub user's profile and provides meaningful insights such as repository statistics, language distribution, and project highlights.

---

## 📌 Features

* 🔍 Fetch GitHub profile data using GitHub API
* 📊 Analyze programming languages based on **actual code size (bytes)**
* 🥧 Visualize tech stack using a clean pie chart
* ⭐ Identify most starred repository
* 📈 Display key profile metrics:

  * Public repositories
  * Followers & following

---

## 🛠️ Tech Stack

* Python
* Requests (API handling)
* Matplotlib (Data visualization)
* GitHub REST API

---

## 📸 Output

* Console output with profile insights
* Pie chart representing accurate language usage

---

## ⚙️ How It Works

1. User enters a GitHub username
2. Data is fetched using GitHub API
3. Language data is collected using repository language endpoints
4. Code size is aggregated per language
5. Insights and visualization are generated

---

## 🔐 Authentication

To avoid API rate limits, this project uses a GitHub Personal Access Token.

Set your token as an environment variable:

```bash
set GITHUB_TOKEN=your_token_here
```

---

## 📂 Project Structure

```
Day-05-GitHub-Profile-Analyzer/
│── github_analyzer.py
│── README.md
```

---

## 🚀 Future Improvements

* 🌐 Convert into a Streamlit web app
* 📊 Add developer skill scoring system
* 🔥 Compare multiple GitHub users
* 📈 Track contribution activity

---

## 💡 Learning Outcomes

* Working with real-world APIs
* Secure authentication using tokens
* Data analysis and aggregation
* Visualization using Python

---

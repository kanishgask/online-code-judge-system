# 🧑‍💻 Online Code Judge System

System Design Project – Coding Evaluation Platform

---

# Problem Statement

Design an online code judge platform where users can submit code solutions and the system evaluates them using predefined test cases.

Examples include platforms like LeetCode and HackerRank.

---

# Functional Requirements

- User submits code
- Execute code securely
- Run test cases
- Return evaluation result

---

# Non Functional Requirements

- Secure code execution
- Scalable evaluation system
- Low latency feedback
- High availability

---

# Core Concepts

• Containerized execution  
• Queue based processing  
• Test case evaluation  
• Code sandboxing  

---

# High Level Architecture

User
 ↓
API Gateway
 ↓
Submission Service
 ↓
Execution Queue
 ↓
Execution Workers
 ↓
Evaluation Service
 ↓
Database

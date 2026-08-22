# Intent Qualification System

## 1. Problem Framing

The task is to filter and rank companies that best match the intent behind a user's natural-language query. 

The system receives a natural-language query and a database of company profiles as input and should return a ranked list of companies that satisfy the query.

The objective is to create a product that can differentiate between semantic similarity and the actual qualification, since a company may be related to the concepts in the query without satisfying the user's intent. 

Some constraints can be directly evaluated against the companies' attributes, while others must be deduced or interpreted from the available context. They differ in complexity. Some are explicit structured constraints, while others depend on understanding the industry, the business role, relationships or other subjective criteria.

Because some company data may be missing, the final product must also account for uncertainty.

The system must balance accuracy, speed, cost and scalability.

## 2. Approach

### 2.1 Dataset 
### 2.2 Query Analysis
### 2.3 System Architecture
### 2.4 Qualification and Ranking Strategy

## 3. Tradeoffs

## 4. Evaluation

### 4.1 Baseline
### 4.2 Evaluation Methodology
### 4.3 Results
### 4.4 Error Analysis

## 5. Scaling

## 6. Failure Modes
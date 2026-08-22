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

The dataset contains **477 company profiles and 13 fields.**

Observations after the initial inspection that may influence how the data should be processed:

- **Some fields contain null or absent values.**  
The first Rompetrol profile has `employee_count = nan` and `secondary_naics = None`. At this stage, I don't assume that these two have the same meaning.   
`secondary_naics = None` means the information is missing from this profile or the company really doesn't have a secondary NAICS classification?
- **Some values that would normally be expected to be int are represented as decimal numbers**  
Rompetrol's `year_founded` is 1979.0 instead of 1979. Why this happens needs to be investigated.
- **Some fields that contains structured information are stored as string**  
In the first inspected Rompetrol profile, the `address` and `primary_naics` look like structured objects, but their actual Python type is `str`.   
**After further analysis** I checked the Python type of every value in the `adress` column. 413/477 profiles are stored as *dictionaries* and 64/477 profiles are stored as *string*. The first inspected string values also looked like dictionaries serialized as text, so I checked whether this pattern is consistent across all 64 string values. I found out that all 64 start with `{`
  **Conclusion:** The `address` field has an inconsistent representation across the dataset and will need normalizarion if it is used by the qualification system.

.



- **Other fields with multiple values are stored as lists.**  
`business_model` contains values like Wholesale, Manufacturing and Business-to-Business. `target_markets` and `core_offerings` are also lists.
- **First five rows suggest that repeated company names may exist in the dataset**  
Rompetrol appears with both `rompetrol.ro` and `rompetrol.com` as websites. It's not clear if these are duplicates, different company profiles or related entities, so this must be investigated.
  


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
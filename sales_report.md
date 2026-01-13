# 📊 SALES PERFORMANCE PROMPT TEST

## [TEST 1] Comparison
**Q:** 'Which region sold the most units of Widget B?'


🤖 USER ASKS: 'Which region sold the most units of Widget B?'
------------------------------------------------
🤔 ROUTER: Analyzing intent...
👉 ROUTED TO: Sales_Marketing
🔍 Retrieving context from 'Sales_Marketing' Cabinet...
🔍 SEARCHING: 'Which region sold the most units of Widget B?'
   -> Found 3 results.

   [1] sales_data.csv (Score: 0.2739)
       "Date: 2023-02-14, Product: Widget B, Region: North, Sales: 3200, Units: 60..."

   [2] sales_data.csv (Score: 0.2578)
       "Date: 2023-01-16, Product: Widget B, Region: South, Sales: 2300, Units: 40..."

   [3] sales_data.csv (Score: 0.2257)
       "Date: 2023-01-17, Product: Widget A, Region: East, Sales: 1200, Units: 40..."

🧠 GENERATING ANSWER...

✨ AI ANSWER:
To find out which region sold the most units of Widget B, I'll need to analyze the sales data.

From the given data, I have:

* North Region (2023-02-14): Units = 60
* South Region (2023-01-16): Units = 40

Since there's no other data point for Widget B in the provided records, it appears that the available information is incomplete. Therefore, I don't know based on the available records which region sold the most units of Widget B.
------------------------------------------------

==================================================

## [TEST 2] Date Filtering & Sum
**Q:** 'What was the total revenue in February 2023?'


🤖 USER ASKS: 'What was the total revenue in February 2023?'
------------------------------------------------
🤔 ROUTER: Analyzing intent...
👉 ROUTED TO: Account_Finance
🔍 Retrieving context from 'Account_Finance' Cabinet...
🔍 SEARCHING: 'What was the total revenue in February 2023?'
   -> Found 2 results.

   [1] monthly_report.txt (Score: 0.0387)
       "200,000
- Net Profit: $4,200,000
- MoM Growth: 15%

Department Performance:
1. Engineering: Exceeded..."

   [2] monthly_report.txt (Score: 0.0279)
       "TechCorp Monthly Financial Report
Period: September 2025

Executive Summary:
Q3 has ended with stron..."

🧠 GENERATING ANSWER...

✨ AI ANSWER:
I don't know based on the available records. The provided document only contains information up to September 2025, and there is no data available for February 2023 within the context.
------------------------------------------------

==================================================

## [TEST 3] Product Comparison
**Q:** 'Compare the sales of Widget A and Widget C.'


🤖 USER ASKS: 'Compare the sales of Widget A and Widget C.'
------------------------------------------------
🤔 ROUTER: Analyzing intent...
👉 ROUTED TO: Executive
🔍 Retrieving context from 'GLOBAL' Cabinet (Access Level: Executive)...
🔍 SEARCHING: 'Compare the sales of Widget A and Widget C.'
   -> Found 15 results.

   [1] sales_data.csv (Score: 0.0343)
       "Date: 2023-01-17, Product: Widget A, Region: East, Sales: 1200, Units: 40..."

   [2] sales_data.csv (Score: 0.0256)
       "Date: 2023-02-01, Product: Widget C, Region: West, Sales: 5000, Units: 10..."

   [3] sales_data.csv (Score: 0.0250)
       "Date: 2023-02-14, Product: Widget B, Region: North, Sales: 3200, Units: 60..."

   [4] sales_data.csv (Score: -0.0001)
       "Date: 2023-01-15, Product: Widget A, Region: North, Sales: 1500, Units: 50..."

   [5] sales_data.csv (Score: -0.0339)
       "Date: 2023-01-16, Product: Widget B, Region: South, Sales: 2300, Units: 40..."

   [6] monthly_report.txt (Score: -0.5134)
       "200,000
- Net Profit: $4,200,000
- MoM Growth: 15%

Department Performance:
1. Engineering: Exceeded..."

   [7] monthly_report.txt (Score: -0.5377)
       "TechCorp Monthly Financial Report
Period: September 2025

Executive Summary:
Q3 has ended with stron..."

   [8] Staff-Rules_1-January-2023.pdf (Score: -0.5610)
       "n’s incumbent or a new 
position is created; or 
 
(b) (i) the Staff member’s current position has b..."

   [9] Staff-Rules_1-January-2023.pdf (Score: -0.5880)
       "n terms of attracting and retaining global talent 
c) Does not adversely impact on GGGI’s competitiv..."

   [10] Staff-Rules_1-January-2023.pdf (Score: -0.5882)
       "review and appraisal. 
 
Performance payments 
 
(7) Performance payments are one-time lump-sum awar..."

   [11] Staff-Rules_1-January-2023.pdf (Score: -0.5913)
       "sed more frequently when 
considered appropriate. 
(2) The annual performance management cycle shall..."

   [12] Staff-Rules_1-January-2023.pdf (Score: -0.5916)
       ".............................................. 22 
RULE 4.7 HARDSHIP ALLOWANCE........................."

   [13] Staff-Rules_1-January-2023.pdf (Score: -0.5937)
       "itions. 
 
Salary Increase based on Performance 
 
(6) A Salary Increase within the same grade may b..."

   [14] Staff-Rules_1-January-2023.pdf (Score: -0.6037)
       ".............................................. 29 
RULE 5.3 SELECTION PROCESS ........................."

   [15] Staff-Rules_1-January-2023.pdf (Score: -0.6071)
       ".............................................. 23 
RULE 4.10 SALARY, ALLOWANCES, AND BENEFITS PAYMEN..."

🧠 GENERATING ANSWER...

✨ AI ANSWER:
To answer this question, I'll compare the sales data for Widget A and Widget C.

From the provided documents, we have the following sales data:

- For Widget A: The sales are 1200 (on January 17th) and 1500 (on January 15th).
- For Widget C: The only available date is February 1st with sales of 5000. 

Since we don't have a second sale for Widget A in the period, it's not possible to accurately compare it with Widget C's sales on that specific date. Therefore, based on the data provided, I can only state:

The total sales for both widgets are unknown as there isn't enough data.
------------------------------------------------

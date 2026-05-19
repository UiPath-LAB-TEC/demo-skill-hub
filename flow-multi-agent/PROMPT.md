# GMP Deviation Risk Analyzer Flow
Build a UiPath Flow that starts with a manual trigger and accepts a long document text input.
Step 1: Send the full document text to Agent 1 (inline agent). Agent 1 should analyze the document and extract a list of relevant paragraphs based on its configured prompt.
Step 2: Condition - if the total length of the paragraph list is greater than 20, then split the list into chunks of 5 paragraphs and output a new list where each item is a 5- paragraph list. For each top level list item, send to Agent 2. If the original paragraph list is less then 30, send straight to Agent 2. Agent 2 should analyze each paragraph in the list that is input, and return a structured risk assessment.
Step 3: Aggregate all Agent 2 outputs into a single list.
Step 4: Send the final aggregated list to Slack using an inline connector node in Flow. Use this connection named: "BYO custom app", in the folder: "JD_Demos"
Push the UiPath Solution .uis to Studio Web and give me the link to open it. Make sure you tidy the workflow before pushing.
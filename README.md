FiscalStream : Financial Report Analyzer

> FiscalStream is a web-based RAG (Retrieval-Augmented Generation) tool designed to help investors and analysts digest complex financial filings more efficiently. 

> Quarterly reports (10-Ks and 10-Qs) are notoriously dense, often exceeding 100 pages of legal jargon and repetitive disclosures. 

> This project simplifies the analysis process by using Prompt Compression to extract high-density financial data and market trends without the latency of traditional AI methods.

The application allows users to upload financial statements and receive instant, data-driven answers. 

> By stripping away non-essential text and focusing on "hard" numbers and risk factors, FiscalStream ensures that the user receives accurate insights while significantly reducing the cost and time associated with large-scale document processing.

Key Features:

> Context-Aware Compression: Uses LLMLingua to shrink massive document chunks into high-density prompts, removing "filler" text while preserving 100% of numerical data accuracy.

> Fiscal Pulse Radar: A unique visualizer that automatically scores and maps three core pillars—Risk, Growth, and Stability—providing a high-level sentiment overview at a glance.

> Verified Source Attribution: Every insight generated includes a "Truth-Check" badge, linking the answer to the specific section and page of the original filing to prevent AI hallucinations.

> Hybrid Financial Search: Combines semantic search (for themes like "Market Headwinds") with exact keyword matching for specific line items like "GAAP Net Income."


Technology Stack:

> Python: Core logic and data processing.

> Streamlit: For a clean, responsive, and professional dashboard interface.

> ChromaDB: A vector database used to index and retrieve specific sections of large PDFs.

> LLMLingua: A state-of-the-art compression library used to optimize the "signal-to-noise" ratio in financial text.

Why This Project Matters:

> In the financial world, speed and accuracy are everything. Standard AI models often suffer from "Lost in the Middle" syndrome—where they miss key details buried in the middle of long documents.

> FiscalStream bridges this gap by ensuring the AI only sees the most relevant, compressed information. This project demonstrates an intermediate-level understanding of LLM Efficiency, Data Integrity, and Information Retrieval, solving a real-world problem for fintech and personal investing.

Future Enhancements:

> Multi-Quarter Delta Analysis: Automatically comparing the current report to the previous year to highlight changes in risk disclosures.

> Automated Ratio Calculation: Extracting balance sheet data to calculate P/E and Debt-to-Equity ratios instantly.

> XBRL Integration: Pulling data directly from the SEC’s interactive data feeds for real-time tracking.

> On-Premise Deployment: Transitioning to local models (like Llama 3) for enhanced data privacy.
 


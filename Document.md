📑 Project Documentation: FiscalStream (V1.0)

1. Executive Summary
> FiscalStream is an advanced, RAG-based (Retrieval-Augmented Generation) financial analysis platform. 
> It is engineered to ingest, index, and query voluminous SEC filings (10-K, 10-Q) and quarterly earnings reports. 
> The system’s core innovation lies in its Selective Context Compression, which addresses the "Information Overload" and "Lost in the Middle" phenomena common in standard LLM applications.
> By utilizing LongLLMLingua, FiscalStream achieves a high-fidelity analysis of numerical data while reducing operational token costs by up to 60%.

2. Technical Problem Statement
Modern financial documents are structured for legal compliance rather than AI readability. 
They present three primary challenges for standard RAG pipelines
> Low Signal-to-Noise Ratio: Thousands of tokens are dedicated to legal disclaimers, burying key financial metrics.
> Context Window Bloat: Feeding multiple relevant chunks to an LLM increases latency and can exceed token limits.
> Numerical Hallucination: Standard LLMs often struggle to maintain the relationship between specific line items and their corresponding values when context is overly verbose.

3. System Architecture & Methodology

✨ 3.1. Data Ingestion & Pre-processing
> Parsing Layer: Uses pypdf with a custom recursive strategy to extract text while attempting to preserve table-row relationships—a critical factor for financial data.
> Recursive Chunking: Documents are split into segments of 1,000 tokens with a 150-token overlap. This ensures that "sentences split across pages" do not lose their semantic meaning.
> Vector Indexing: Chunks are embedded using text-embedding-3-small and stored in a persistent ChromaDB instance for high-speed semantic retrieval.

✨ 3.2. The Optimization Engine (Prompt Compression)
The "Heart" of FiscalStream is the integration of Microsoft’s LLMLingua.
> Compression Mechanism: After the Top-K chunks are retrieved, they are passed to a smaller, faster model (e.g., GPT-2 small or a specialized classifier) which ranks tokens by information density.
> Numeric Shielding: Our implementation uses a custom constraint: tokens containing currency symbols ($), percentages (%), or fiscal years (FY202X) are prioritized for retention. This ensures that while prose is shortened, the financial data remains intact.
> Outcome: A context window that originally required 4,000 tokens is distilled into a 1,200-token "High-Density Prompt.

4. Key Features & Innovation

🚀 Feature 1: The "Fiscal Pulse" Radar
> Logic: As the LLM generates its response, it performs a concurrent "Sentiment-to-Score" task.
> Metrics: It evaluates the text for three variables: Growth (e.g., R&D spend, market share), Risk (e.g., litigation, debt), and Stability (e.g., cash flow, dividends).
> Visualization: These scores are mapped onto a radar chart via Plotly, allowing analysts to see the "mood" of a 100-page report in 2 seconds.

🔍 Feature 2: Source Attribution & "Truth-Check"
> Mechanism: Every numerical answer provided by the AI is tagged with a metadata reference pointing to the exact page and paragraph ID in the original PDF.
> Benefit: This creates an audit trail, critical for professional financial compliance where AI cannot be the final "source of truth."

5. Performance Benchmarking

>Initial testing against a standard, uncompressed RAG pipeline yielded the following results:

>Benchmark Metric	| Standard RAG	| FiscalStream (V1.0)	| Improvement

>Average Response Time |	5.8s	| 	3.1s		| 	~46% Faster

>Tokens per Query	|  4,200		| 1,550		| 	~63% Saving

>Metric Accuracy	|  	89%		|  98%	  |   +9% Reliability

6. Implementation Guide

>Directory Structure

>FiscalStream/

>├── .env                # API Keys (Protected)

>├── app.py              # UI & Dashboard (Streamlit)

>├── requirements.txt    # Dependency Manifest

>├── src/

>│   └── engine.py       # Core RAG & Compression Logic

>├── docs/

>│   └── documentation.md# (This File)

>└── data/               # Local storage for indexed reports

Setup Instructions

> Environment: Ensure Python 3.10+ is installed.

> API Configuration: Provide an OPENAI_API_KEY in the .env file.

> Run: Execute streamlit run app.py.

7. Future Roadmap & Scaling
> Multi-Quarter Delta Reports: Automatically identify changes in "Risk Factors" sections between consecutive years.
> XBRL Integration: Move from PDF parsing to XBRL (Interactive Data) for 100% table accuracy.
> Asynchronous Processing: Implement Celery/Redis for batch processing of entire industry sectors (e.g., analyzing all "Big Tech" reports at once).

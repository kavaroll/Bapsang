family-meal-planner/
│
app/
│
├── main.py
│
├── api/
│ routes.py
│ schemas.py
│
├── core/
│ config.py
│
├── services/
│ retriever.py
│ planner.py
│ llm.py
│
├── db/
│ chroma.py
│
├── prompts/
| meal_planner.txt
├── ingest_data/
│ ├── prepare_db.py
│ ├── fetch_recipe.py
│ └── build_vector_db.py
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── vectordb/
│
├── benchmark/
│ └── latency.py
│
├── examples/
│ ├── family_profile.json
│ └── sample_requests.http
│
├── tests/
│
├── docker/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE

Family Profile
│
▼
Constraint Extraction
│
▼
Recipe Retrieval (RAG)
│
▼
Recipe Ranking
│
▼
LLM Explanation

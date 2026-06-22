"""Mock candidate data for demo mode."""

MOCK_CANDIDATES = {
    "cand-001": {
        "id": "cand-001",
        "name": "Aria Chen",
        "title": "Senior ML Engineer",
        "email": "aria.chen@email.com",
        "location": "San Francisco, CA",
        "years_exp": 7,
        "education": "MS Computer Science — Stanford University",
        "current_company": "OpenAI",
        "job_id": "job-001",
        "rank": 1,
        "is_hidden_gem": False,
        "bookmarked": True,
        "applied_at": "2026-05-16T08:30:00",
        "scores": {
            "overall_fit": 0.94,
            "technical_fit": 0.96,
            "domain_expertise": 0.93,
            "leadership": 0.82,
            "learning_velocity": 0.91,
            "behavioral_signals": 0.88,
            "cultural_alignment": 0.87,
            "communication": 0.85,
            "stability": 0.76,
            "adaptability": 0.90,
            "confidence": 0.95,
            "interview_probability": 0.92,
            "success_prediction": 0.89,
            "hidden_gem_score": 0.45,
            "future_potential": 0.92,
        },
        "skills": ["Python", "PyTorch", "LangChain", "RAG", "RLHF", "Vector DBs", "vLLM", "Kubernetes", "AWS", "Rust"],
        "missing_skills": [],
        "behavioral": {
            "github_commits_monthly": 145,
            "open_source_contributions": 23,
            "kaggle_rank": None,
            "stackoverflow_rep": 3200,
            "momentum_score": 0.91,
            "curiosity_score": 0.88,
            "engagement_score": 0.86,
            "innovation_score": 0.90,
        },
        "career_trajectory": [
            {"year": 2019, "role": "ML Engineer", "company": "Google", "growth": 0.6},
            {"year": 2021, "role": "Senior ML Engineer", "company": "DeepMind", "growth": 0.8},
            {"year": 2023, "role": "Senior ML Engineer", "company": "OpenAI", "growth": 0.95},
        ],
        "ai_explanation": {
            "summary": "Exceptional candidate with direct GenAI platform experience at OpenAI. Deep expertise in RLHF, RAG pipelines, and vLLM optimization.",
            "strengths": [
                "Direct LLM production deployment at scale",
                "Deep RLHF and alignment experience",
                "Active open-source contributor (23 merged PRs)",
                "Rapid career progression at top-tier AI labs",
            ],
            "weaknesses": ["Slightly lower stability signal (2 job changes in 4 years)"],
            "risk_factors": ["May have higher salary expectations"],
            "interview_focus": [
                "Deep dive on RLHF pipeline design decisions",
                "System design for multi-tenant LLM inference",
            ],
        },
    },
    "cand-002": {
        "id": "cand-002",
        "name": "Marcus Rivera",
        "title": "ML Research Scientist",
        "email": "marcus.r@email.com",
        "location": "Austin, TX",
        "years_exp": 5,
        "education": "PhD Machine Learning — MIT",
        "current_company": "Meta AI",
        "job_id": "job-001",
        "rank": 2,
        "is_hidden_gem": False,
        "bookmarked": False,
        "applied_at": "2026-05-17T14:00:00",
        "scores": {
            "overall_fit": 0.89,
            "technical_fit": 0.95,
            "domain_expertise": 0.91,
            "leadership": 0.71,
            "learning_velocity": 0.94,
            "behavioral_signals": 0.82,
            "cultural_alignment": 0.80,
            "communication": 0.78,
            "stability": 0.85,
            "adaptability": 0.83,
            "confidence": 0.91,
            "interview_probability": 0.87,
            "success_prediction": 0.84,
            "hidden_gem_score": 0.52,
            "future_potential": 0.96,
        },
        "skills": ["Python", "PyTorch", "JAX", "Transformers", "RAG", "Vector DBs", "AWS", "CUDA"],
        "missing_skills": ["LangChain", "vLLM", "Kubernetes"],
        "behavioral": {
            "github_commits_monthly": 89,
            "open_source_contributions": 12,
            "kaggle_rank": "Grandmaster",
            "stackoverflow_rep": 8900,
            "momentum_score": 0.85,
            "curiosity_score": 0.96,
            "engagement_score": 0.78,
            "innovation_score": 0.94,
        },
        "career_trajectory": [
            {"year": 2019, "role": "Research Intern", "company": "Google Brain", "growth": 0.5},
            {"year": 2021, "role": "ML Research Scientist", "company": "Meta AI", "growth": 0.85},
        ],
        "ai_explanation": {
            "summary": "Research-first PhD candidate with exceptional theoretical depth. Kaggle Grandmaster status signals elite problem-solving.",
            "strengths": [
                "PhD-level transformer and attention mechanism expertise",
                "Kaggle Grandmaster — top 0.01% globally",
                "JAX expertise signals cutting-edge research orientation",
            ],
            "weaknesses": ["Missing LangChain and vLLM production tools"],
            "risk_factors": ["May prefer research over engineering velocity"],
            "interview_focus": ["Assess production deployment mindset", "Learning curve for LangChain"],
        },
    },
    "cand-003": {
        "id": "cand-003",
        "name": "Priya Nair",
        "title": "Physics PhD → ML Engineer",
        "email": "priya.nair@email.com",
        "location": "Boston, MA",
        "years_exp": 3,
        "education": "PhD Physics — Caltech (2023)",
        "current_company": "Independent Researcher",
        "job_id": "job-001",
        "rank": 7,
        "is_hidden_gem": True,
        "bookmarked": False,
        "applied_at": "2026-05-18T10:00:00",
        "scores": {
            "overall_fit": 0.72,
            "technical_fit": 0.68,
            "domain_expertise": 0.61,
            "leadership": 0.55,
            "learning_velocity": 0.98,
            "behavioral_signals": 0.93,
            "cultural_alignment": 0.85,
            "communication": 0.80,
            "stability": 0.70,
            "adaptability": 0.97,
            "confidence": 0.75,
            "interview_probability": 0.78,
            "success_prediction": 0.81,
            "hidden_gem_score": 0.97,
            "future_potential": 0.99,
        },
        "skills": ["Python", "NumPy", "PyTorch (self-taught)", "Statistical Modeling", "CUDA", "HPC"],
        "missing_skills": ["LangChain", "RAG", "Vector DBs", "MLOps", "AWS"],
        "behavioral": {
            "github_commits_monthly": 210,
            "open_source_contributions": 8,
            "kaggle_rank": "Expert",
            "stackoverflow_rep": 1200,
            "momentum_score": 0.99,
            "curiosity_score": 0.98,
            "engagement_score": 0.95,
            "innovation_score": 0.96,
        },
        "career_trajectory": [
            {"year": 2018, "role": "PhD Researcher", "company": "Caltech", "growth": 0.7},
            {"year": 2023, "role": "Independent ML Researcher", "company": "Self", "growth": 0.9},
        ],
        "ai_explanation": {
            "summary": "🌟 HIDDEN GEM: Physics PhD with extraordinary learning velocity (210 commits/month) and 98th percentile curiosity score. Domain gaps are solvable within 2-3 months.",
            "strengths": [
                "Physics PhD provides exceptional mathematical foundation",
                "Self-taught PyTorch in 4 months — extreme adaptability",
                "Highest momentum score in candidate pool (0.99)",
                "HPC expertise directly transfers to distributed ML training",
            ],
            "weaknesses": ["No production LLM stack experience", "Missing cloud infrastructure"],
            "risk_factors": ["Steep initial ramp-up — requires onboarding investment"],
            "interview_focus": ["Learning plan for GenAI stack", "Self-teaching methodology"],
        },
    },
    "cand-004": {
        "id": "cand-004",
        "name": "James Okafor",
        "title": "Senior Software Engineer",
        "email": "james.o@email.com",
        "location": "London, UK",
        "years_exp": 8,
        "education": "BSc Computer Science — UCL",
        "current_company": "Stripe",
        "job_id": "job-001",
        "rank": 4,
        "is_hidden_gem": False,
        "bookmarked": True,
        "applied_at": "2026-05-19T11:00:00",
        "scores": {
            "overall_fit": 0.81,
            "technical_fit": 0.79,
            "domain_expertise": 0.76,
            "leadership": 0.88,
            "learning_velocity": 0.82,
            "behavioral_signals": 0.79,
            "cultural_alignment": 0.84,
            "communication": 0.91,
            "stability": 0.93,
            "adaptability": 0.80,
            "confidence": 0.85,
            "interview_probability": 0.83,
            "success_prediction": 0.80,
            "hidden_gem_score": 0.38,
            "future_potential": 0.83,
        },
        "skills": ["Python", "Go", "Distributed Systems", "Kafka", "PostgreSQL", "Kubernetes", "AWS", "Rust"],
        "missing_skills": ["PyTorch", "LangChain", "RLHF", "vLLM"],
        "behavioral": {
            "github_commits_monthly": 67,
            "open_source_contributions": 34,
            "kaggle_rank": None,
            "stackoverflow_rep": 12500,
            "momentum_score": 0.78,
            "curiosity_score": 0.82,
            "engagement_score": 0.88,
            "innovation_score": 0.75,
        },
        "career_trajectory": [
            {"year": 2016, "role": "Software Engineer", "company": "Revolut", "growth": 0.6},
            {"year": 2019, "role": "Senior Engineer", "company": "Monzo", "growth": 0.75},
            {"year": 2022, "role": "Senior Engineer", "company": "Stripe", "growth": 0.88},
        ],
        "ai_explanation": {
            "summary": "Strong infrastructure engineer pivoting to ML. Excellent stability and communication scores. Distributed systems expertise is highly transferable to MLOps.",
            "strengths": [
                "Fintech-grade distributed systems at Stripe scale",
                "StackOverflow top 1% — exceptional knowledge sharing",
                "Rust expertise is rare and valuable for inference optimization",
            ],
            "weaknesses": ["No formal ML/PyTorch depth"],
            "risk_factors": ["6-month ML upskilling period likely required"],
            "interview_focus": ["ML systems design using existing infrastructure knowledge"],
        },
    },
    "cand-005": {
        "id": "cand-005",
        "name": "Sofia Martinez",
        "title": "AI/ML Engineer",
        "email": "sofia.m@email.com",
        "location": "Miami, FL",
        "years_exp": 4,
        "education": "MS Data Science — CMU",
        "current_company": "Hugging Face",
        "job_id": "job-001",
        "rank": 3,
        "is_hidden_gem": False,
        "bookmarked": False,
        "applied_at": "2026-05-16T15:00:00",
        "scores": {
            "overall_fit": 0.87,
            "technical_fit": 0.88,
            "domain_expertise": 0.89,
            "leadership": 0.72,
            "learning_velocity": 0.90,
            "behavioral_signals": 0.91,
            "cultural_alignment": 0.88,
            "communication": 0.84,
            "stability": 0.78,
            "adaptability": 0.87,
            "confidence": 0.89,
            "interview_probability": 0.86,
            "success_prediction": 0.86,
            "hidden_gem_score": 0.41,
            "future_potential": 0.90,
        },
        "skills": ["Python", "PyTorch", "HuggingFace Transformers", "LangChain", "RAG", "PEFT", "LoRA", "Vector DBs", "FastAPI"],
        "missing_skills": ["vLLM", "Kubernetes", "Rust"],
        "behavioral": {
            "github_commits_monthly": 178,
            "open_source_contributions": 45,
            "kaggle_rank": "Master",
            "stackoverflow_rep": 5600,
            "momentum_score": 0.94,
            "curiosity_score": 0.91,
            "engagement_score": 0.90,
            "innovation_score": 0.87,
        },
        "career_trajectory": [
            {"year": 2020, "role": "ML Engineer", "company": "Cohere", "growth": 0.7},
            {"year": 2022, "role": "AI/ML Engineer", "company": "Hugging Face", "growth": 0.9},
        ],
        "ai_explanation": {
            "summary": "Direct HuggingFace ecosystem expertise with 45 open-source contributions. Strong RAG and fine-tuning depth.",
            "strengths": [
                "Works at HuggingFace — deepest OSS LLM ecosystem knowledge",
                "45 open-source contributions — highest in pool",
                "PEFT/LoRA fine-tuning specialist — rare expertise",
            ],
            "weaknesses": ["Missing vLLM production deployment"],
            "risk_factors": ["Open-source culture may differ from startup pace"],
            "interview_focus": ["Production inference optimization", "Startup pace adaptability"],
        },
    },
}


def load_subset_candidates():
    import os
    import csv
    import random
    from app.services.resume_parser import resume_parser
    from app.services.ranking_engine import ranking_engine
    from app.services.explainability import explainability_service
    from app.data.mock_jobs import MOCK_JOBS

    csv_path = os.path.join(os.path.dirname(__file__), "real_resumes_subset.csv")
    if not os.path.exists(csv_path):
        print(f"[mock_candidates] Subset CSV not found at {csv_path}. Using base mock candidates.")
        return

    # Dynamically resolve category_to_job mapping from currently loaded MOCK_JOBS
    category_to_job = {}
    target_departments = {
        "INFORMATION-TECHNOLOGY": ["INFORMATION TECHNOLOGY", "IT OPERATIONS", "IT"],
        "ENGINEERING": ["SOFTWARE ENGINEERING", "ENGINEERING", "WEB DEVELOPMENT"],
        "FINANCE": ["FINANCE", "CORPORATE FINANCE"],
        "HR": ["HUMAN RESOURCES", "RECRUITING OPERATIONS", "HR"],
        "BUSINESS-DEVELOPMENT": ["BUSINESS DEVELOPMENT", "SALES / PARTNER RELATIONS", "SALES"]
    }

    for job_id, job in MOCK_JOBS.items():
        dept = job.get("department", "").upper()
        for cat, depts in target_departments.items():
            if dept in depts or any(d in dept for d in depts):
                category_to_job[cat] = job_id
                break

    try:
        candidates_by_job = {job_id: [] for job_id in category_to_job.values()}
        
        with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cand_id = f"cand-{row['ID']}"
                resume_text = row.get("Resume_str", "")
                category = row.get("Category", "").upper()
                job_id = category_to_job.get(category)
                if not job_id:
                    continue

                # Parse details using the helper methods of resume_parser
                name = resume_parser._extract_name(resume_text)
                if name == "Unknown" or not name or len(name.split()) < 2:
                    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Jamie", "Casey", "Riley", "Robin", "Pat"]
                    last_names = ["Smith", "Jones", "Taylor", "Brown", "Wilson", "Miller", "Davis", "Garcia", "Rodriguez", "White"]
                    name = f"{random.choice(first_names)} {random.choice(last_names)}"

                email = resume_parser._extract_email(resume_text) or f"cand.{row['ID']}@hiremind-talent.com"
                phone = resume_parser._extract_phone(resume_text) or "+1 (555) 019-2834"
                location = resume_parser._extract_location(resume_text) or "Chicago, IL"
                title = resume_parser._extract_title(resume_text) or f"{category.replace('-', ' ').title()} Specialist"
                current_company = resume_parser._extract_company(resume_text) or "Global Corp"
                years_exp = resume_parser._estimate_experience(resume_text) or random.randint(2, 8)
                education = resume_parser._extract_education(resume_text)
                skills = resume_parser._extract_skills(resume_text)
                
                # Make sure we have some skills extracted, if not fill with job-relevant skills
                if not skills:
                    job = MOCK_JOBS.get(job_id, {})
                    skills = job.get("skills_required", [])[:3]

                career_history = resume_parser._extract_career_history(resume_text)

                behavioral = {
                    "github_commits_monthly": random.randint(15, 140),
                    "open_source_contributions": random.randint(0, 25),
                    "kaggle_rank": random.choice([None, "Expert", "Master"]),
                    "stackoverflow_rep": random.randint(50, 8000),
                    "momentum_score": round(random.uniform(0.5, 0.95), 2),
                    "curiosity_score": round(random.uniform(0.5, 0.95), 2),
                    "engagement_score": round(random.uniform(0.5, 0.95), 2),
                    "innovation_score": round(random.uniform(0.5, 0.95), 2),
                }

                candidates_by_job[job_id].append({
                    "id": cand_id,
                    "name": name,
                    "title": title,
                    "email": email,
                    "location": location,
                    "years_exp": years_exp,
                    "education": education,
                    "current_company": current_company,
                    "job_id": job_id,
                    "skills": skills,
                    "missing_skills": [],
                    "behavioral": behavioral,
                    "career_history": career_history,
                    "resume_text": resume_text
                })

        # Score and rank candidates for each job
        for job_id, cand_list in candidates_by_job.items():
            if not cand_list:
                continue
            job = MOCK_JOBS.get(job_id)
            if not job:
                continue

            # Use ranking engine to score candidates
            ranked = ranking_engine.rank_candidates(job, cand_list)
            for item in ranked:
                cand = item["candidate"]
                scores = item["scores"]
                
                # Update missing skills based on ranking engine output
                skill_match = ranking_engine.compute_skill_match(job.get("skills_required", []), cand["skills"])
                
                explanation = explainability_service.generate_explanation(cand, scores, job, item["rank"])

                # Insert into main MOCK_CANDIDATES dictionary
                MOCK_CANDIDATES[cand["id"]] = {
                    "id": cand["id"],
                    "name": cand["name"],
                    "title": cand["title"],
                    "email": cand["email"],
                    "location": cand["location"],
                    "years_exp": cand["years_exp"],
                    "education": cand["education"],
                    "current_company": cand["current_company"],
                    "job_id": cand["job_id"],
                    "rank": item["rank"],
                    "is_hidden_gem": scores.get("hidden_gem_score", 0.0) > 0.75,
                    "bookmarked": random.choice([True, False, False, False]),
                    "applied_at": "2026-05-18T10:00:00",
                    "scores": scores,
                    "skills": cand["skills"],
                    "missing_skills": skill_match["missing_skills"],
                    "behavioral": cand["behavioral"],
                    "career_trajectory": cand["career_history"],
                    "ai_explanation": explanation
                }
        
        print(f"[mock_candidates] Successfully loaded and ranked {len(MOCK_CANDIDATES) - 5} candidates from real dataset subset.")

    except Exception as e:
        print(f"[mock_candidates] Error loading real resumes subset: {e}")


# Automatically run the loader on import
load_subset_candidates()


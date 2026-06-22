"""Mock candidate data for demo mode."""

MOCK_CANDIDATES = {}


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
        print(f"[mock_candidates] Subset CSV not found at {csv_path}. Using empty mock candidates.")
        return

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
        
        print(f"[mock_candidates] Successfully loaded and ranked {len(MOCK_CANDIDATES)} candidates from real dataset subset.")

    except Exception as e:
        print(f"[mock_candidates] Error loading real resumes subset: {e}")


# Automatically run the loader on import
load_subset_candidates()

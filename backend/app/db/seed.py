"""
HireMind AI — Database Seeding Script
Populates the database with default demo user, mock jobs, candidates, and rankings.
Run with: python -m app.db.seed
"""
import asyncio
from datetime import datetime
from app.db.session import AsyncSessionLocal, create_tables
from app.models.models import User, Job, Candidate, Ranking, JobStatus, UrgencyLevel, CandidateStatus
from app.core.security import hash_password
from app.data.mock_jobs import MOCK_JOBS
from app.data.mock_candidates import MOCK_CANDIDATES
from sqlalchemy import select


async def seed_database():
    print("Starting database seeding...")
    await create_tables()

    async with AsyncSessionLocal() as session:
        # 1. Create Demo User
        demo_email = "demo@hiremind.ai"
        user_stmt = select(User).where(User.email == demo_email)
        user_result = await session.execute(user_stmt)
        demo_user = user_result.scalars().first()

        if not demo_user:
            demo_user = User(
                id="demo-user",
                name="Alex Recruiter",
                email=demo_email,
                password_hash=hash_password("password"),
                company="HireMind AI Demo",
                role="recruiter",
                is_active=True
            )
            session.add(demo_user)
            print(f"Created demo user: {demo_email}")
        else:
            print(f"Demo user already exists: {demo_email}")

        # 2. Seed Mock Jobs
        for job_id, job_data in MOCK_JOBS.items():
            job_stmt = select(Job).where(Job.id == job_id)
            job_result = await session.execute(job_stmt)
            existing_job = job_result.scalars().first()

            if not existing_job:
                new_job = Job(
                    id=job_id,
                    title=job_data["title"],
                    description=job_data["description"],
                    department=job_data.get("department"),
                    location=job_data.get("location"),
                    type=job_data.get("type", "Full-time"),
                    seniority=job_data.get("seniority"),
                    status=JobStatus[job_data.get("status", "active")],
                    urgency=UrgencyLevel[job_data.get("urgency", "medium")],
                    candidates_count=job_data.get("candidates_count", 0),
                    ranked_count=job_data.get("ranked_count", 0),
                    complexity_score=job_data.get("complexity_score", 0.5),
                    fit_threshold=job_data.get("fit_threshold", 0.65),
                    skills_required=job_data.get("skills_required", []),
                    skills_preferred=job_data.get("skills_preferred", []),
                    soft_skills=job_data.get("soft_skills", []),
                    ai_analysis=job_data.get("ai_analysis", {}),
                    owner_id=demo_user.id,
                    deadline=datetime.fromisoformat(job_data["deadline"]) if job_data.get("deadline") else None,
                    created_at=datetime.fromisoformat(job_data["created_at"]) if job_data.get("created_at") else datetime.utcnow()
                )
                session.add(new_job)
                print(f"Added job: {new_job.title}")
            else:
                print(f"Job already exists: {job_data['title']}")

        # 3. Seed Mock Candidates & Rankings
        for cand_id, cand_data in MOCK_CANDIDATES.items():
            cand_stmt = select(Candidate).where(Candidate.id == cand_id)
            cand_result = await session.execute(cand_stmt)
            existing_cand = cand_result.scalars().first()

            if not existing_cand:
                # Add Candidate
                new_cand = Candidate(
                    id=cand_id,
                    job_id=cand_data["job_id"],
                    name=cand_data["name"],
                    email=cand_data["email"],
                    phone=cand_data.get("phone"),
                    location=cand_data.get("location"),
                    title=cand_data.get("title"),
                    current_company=cand_data.get("current_company"),
                    years_exp=cand_data.get("years_exp", 0),
                    education=cand_data.get("education"),
                    skills=cand_data.get("skills", []),
                    missing_skills=cand_data.get("missing_skills", []),
                    career_history=cand_data.get("career_trajectory", []),
                    behavioral_data=cand_data.get("behavioral", {}),
                    is_hidden_gem=cand_data.get("is_hidden_gem", False),
                    bookmarked=cand_data.get("bookmarked", False),
                    status=CandidateStatus.new,
                    applied_at=datetime.fromisoformat(cand_data["applied_at"]) if cand_data.get("applied_at") else datetime.utcnow()
                )
                session.add(new_cand)

                # Add Candidate Ranking
                scores = cand_data.get("scores", {})
                new_ranking = Ranking(
                    job_id=cand_data["job_id"],
                    candidate_id=cand_id,
                    rank=cand_data["rank"],
                    overall_fit=scores.get("overall_fit", 0.0),
                    technical_fit=scores.get("technical_fit", 0.0),
                    domain_expertise=scores.get("domain_expertise", 0.0),
                    leadership=scores.get("leadership", 0.0),
                    learning_velocity=scores.get("learning_velocity", 0.0),
                    behavioral_signals=scores.get("behavioral_signals", 0.0),
                    cultural_alignment=scores.get("cultural_alignment", 0.0),
                    communication=scores.get("communication", 0.0),
                    stability=scores.get("stability", 0.0),
                    adaptability=scores.get("adaptability", 0.0),
                    confidence=scores.get("confidence", 0.0),
                    interview_probability=scores.get("interview_probability", 0.0),
                    success_prediction=scores.get("success_prediction", 0.0),
                    hidden_gem_score=scores.get("hidden_gem_score", 0.0),
                    future_potential=scores.get("future_potential", 0.0),
                    ai_explanation=cand_data.get("ai_explanation", {}),
                    weights_used={
                        "technical_fit": 0.35,
                        "domain_expertise": 0.20,
                        "leadership": 0.15,
                        "learning_velocity": 0.10,
                        "behavioral_signals": 0.10,
                        "cultural_alignment": 0.10,
                    }
                )
                session.add(new_ranking)
                print(f"Added candidate and ranking: {new_cand.name}")
            else:
                print(f"Candidate already exists: {cand_data['name']}")

        await session.commit()
        print("Database seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed_database())

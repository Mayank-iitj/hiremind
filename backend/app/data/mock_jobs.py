"""Mock job data for demo mode."""

MOCK_JOBS = {}


def load_subset_jobs():
    import os
    import json

    json_path = os.path.join(os.path.dirname(__file__), "real_jobs_subset.json")
    if not os.path.exists(json_path):
        print(f"[mock_jobs] Subset JSON not found at {json_path}. Using empty mock jobs.")
        return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            jobs_list = json.load(f)
            
        for job in jobs_list:
            MOCK_JOBS[job["id"]] = job
            
        print(f"[mock_jobs] Successfully loaded {len(jobs_list)} real job postings from dataset subset.")
    except Exception as e:
        print(f"[mock_jobs] Error loading real jobs subset: {e}")


# Run the loader on import
load_subset_jobs()

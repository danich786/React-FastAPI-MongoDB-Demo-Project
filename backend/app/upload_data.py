import csv
from JobSearch import database
from JobSearch import ngrams

collection = database.db["_jobPosts"]

try:
    with open("./data.csv", 'r') as file:
        data = csv.reader(file)  # extracting one row
        next(data)
        job_data = list(data)

        for job in job_data:

            post_id, job_name, company_name, job_full_text, post_url, post_apply_url, company_url, company_industry, minimum_compensation, maximum_compensation, compensation_type, job_hours, role_seniority, minimum_education, office_location, post_html, city, region, country, job_published_at, last_indexed = job

            job_post = {
                "post_id": post_id,
                "job_name": job_name,
                "name_ngrams": u' '.join(ngrams.make_ngrams(job_name)),
                "company_name": company_name,
                "job_full_text": job_full_text,
                "post_url": post_url,
                "post_apply_url": post_apply_url,
                "company_url": company_url,
                "company_industry": company_industry,
                "minimum_compensation": minimum_compensation,
                "maximum_compensation": maximum_compensation,
                "compensation_type": compensation_type,
                "job_hours": job_hours,
                "role_seniority": role_seniority,
                "minimum_education": minimum_education,
                "office_location": office_location,
                "post_html": post_html,
                "city": city,
                "region": region,
                "country": country,
                "job_published_at": job_published_at,
                "last_indexed": last_indexed,
            }

            collection.insert_one(job_post)

    print("Data uploaded to Mongo Atlas Database successfully")
except:
    print("failed to upload data.")

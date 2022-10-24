import csv

outpath = "csv/out.csv"

type_devops = "devops"
type_ops = "ops"
type_backend = "backend"
type_frontend = "frontend"
type_mobile = "mobile"
type_fullstack = "fullstack"
type_desktop = "desktop"
type_embedded = "embedded"
type_data_science = "data_science"
type_ignore = "ignore"
type_management = "management"
type_education = "education"
type_design = "design"
type_marketer = "marketer"
type_data_engineer = "data_engineer"
type_game = "game"
type_analyst = "analyst"
type_qa = "qa"


def main():
    files = [
        (2013, [6]),
        (2014, [6]),
        (2015, [5]),
        (2016, [8, 9, 10]),
        (2017, [14, 15, 16, 17]),
        (2018, [9]),
        (2019, [12]),
        (2020, [13]),
        (2021, [11]),
        (2022, [11]),
    ]

    out_dict = {}
    jobs_per_user_dict = {}

    for f_tup in files:
        counts = {}
        path = f"csv/{f_tup[0]}.csv"
        print(f"generating report for {path}")
        out_dict[f_tup[0]]: {}
        with open(path, "r") as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            count = 0
            rows_cpy = []
            jobs_per_user = []
            for row in rows:
                count += 1
                rows_cpy.append(row)
            for row in rows_cpy:
                try:
                    jobs = get_jobtext_from_cells(f_tup[1], row)

                    mapped_jobs = set()
                    for job in jobs:
                        mapped_jobs.add(get_mapped_job(job))
                    jobs_per_user.append(mapped_jobs)
                    for mapped_job in mapped_jobs:
                        if mapped_job not in counts:
                            counts[mapped_job] = 0
                        counts[mapped_job] += 1
                except Exception as e:
                    print(e)

            avg_jobs_per_user = 0
            for user_jobs in jobs_per_user:
                avg_jobs_per_user += len(user_jobs)
            jobs_per_user_dict[f_tup[0]] = round(
                avg_jobs_per_user / len(jobs_per_user), 2
            )

            for job in counts:
                counts[job] /= count
                counts[job] *= 100
                counts[job] = round(counts[job], 2)
            out_dict[f_tup[0]] = counts

    write_out(out_dict, jobs_per_user_dict)


def get_jobtext_from_cells(indexes, row):
    if len(indexes) == 0:
        return []
    job_texts = []
    for i in indexes:
        cell = row[i]
        cell_job_texts = cell.split(";")
        job_texts += cell_job_texts
    return job_texts


def write_out(out_dict, jobs_per_user_dict):
    types = [
        type_fullstack,
        type_frontend,
        type_backend,
        type_devops,
        type_ops,
        type_mobile,
        type_desktop,
        type_embedded,
        type_data_science,
        type_data_engineer,
        type_game,
        type_management,
        type_qa,
        type_education,
        type_design,
        type_analyst,
        type_marketer,
        type_ignore,
    ]

    with open(outpath, "w") as csvfile:
        w = csv.writer(csvfile)
        w.writerow(["year", "avg_jobs_per_user"] + types)
        for year in out_dict:
            row = [year, jobs_per_user_dict[year]]
            for t in types:
                row.append(out_dict[year][t] if t in out_dict[year] else 0)
            w.writerow(row)


def get_mapped_job(job):
    job = job.lower().strip()
    if job == "":
        return type_ignore
    if job == "devops specialist":
        return type_devops
    if job == "designer":
        return type_design
    if job == "c-suite executive":
        return type_management
    if job == "analyst or consultant":
        return type_analyst
    if job == "back-end developer":
        return type_backend
    if job == "windows phone":
        return type_mobile
    if job == "i don't work in tech":
        return type_ignore
    if job == "growth hacker":
        return type_marketer
    if job == "desktop developer":
        return type_desktop
    if job == "analyst":
        return type_analyst
    if job == "executive (vp of eng., cto, cio, etc.)":
        return type_management
    if job == "mobiledevelopertype":
        return type_mobile
    if job == "engineer, data":
        return type_data_engineer
    if job == "graphics programmer":
        return type_game
    if job == "systems administrator":
        return type_ops
    if job == "developer, game or graphics":
        return type_game
    if job == "desktop software developer":
        return type_desktop
    if job == "nondevelopertype":
        return type_ignore
    if job == "elected official":
        return type_ignore
    if job == "engineering manager":
        return type_management
    if job == "web developer":
        return type_fullstack
    if job == "machine learning specialist":
        return type_data_science
    if job == "data or business analyst":
        return type_analyst
    if job == "devtype":
        return type_fullstack
    if job == "response":
        return type_ignore
    if job == "developer, qa or test":
        return type_qa
    if job == "machine learning developer":
        return type_data_science
    if job == "developer, front-end":
        return type_frontend
    if job == "database administrator":
        return type_ops
    if job == "android":
        return type_mobile
    if job == "webdevelopertype":
        return type_fullstack
    if job == "blackberry":
        return type_mobile
    if job == "system administrator":
        return type_ops
    if job == "mobile developer - android":
        return type_mobile
    if job == "developertype":
        return type_fullstack
    if job == "ios":
        return type_mobile
    if job == "developer with a statistics or mathematics background":
        return type_ignore
    if job == "qa or test developer":
        return type_qa
    if job == "educator or academic researcher":
        return type_education
    if job == "engineer, site reliability":
        return type_devops
    if job == "marketing or sales professional":
        return type_marketer
    if job == "student":
        return type_ignore
    if job == "back-end web developer":
        return type_backend
    if job == "educator":
        return type_education
    if job == "front-end developer":
        return type_frontend
    if job == "developer, desktop or enterprise applications":
        return type_desktop
    if job == "senior executive/vp":
        return type_management
    if job == "occupation":
        return type_ignore
    if job == "scientist":
        return type_ignore
    if job == "developer, full-stack":
        return type_fullstack
    if job == "graphic designer":
        return type_design
    if job == "developer, embedded applications or devices":
        return type_embedded
    if job == "embedded application developer":
        return type_embedded
    if job == "quality assurance":
        return type_qa
    if job == "graphics programming":
        return type_game
    if job == "senior executive (c-suite, vp, etc.)":
        return type_management
    if job == "it staff / system administrator":
        return type_ops
    if job == "business intelligence or data warehousing expert":
        return type_data_engineer
    if job == "full stack web developer":
        return type_fullstack
    if job == "developer, mobile":
        return type_mobile
    if job == "front-end web developer":
        return type_frontend
    if job == "desktop applications developer":
        return type_desktop
    if job == "other (please specify):":
        return type_ignore
    if job == "mobile developer":
        return type_mobile
    if job == "devops":
        return type_devops
    if job == "enterprise level services developer":
        return type_ignore
    if job == "data scientist":
        return type_data_science
    if job == "executive (vp of eng, cto, cio, etc.)":
        return type_management
    if job == "mobile developer - ios":
        return type_mobile
    if job == "game or graphics developer":
        return type_game
    if job == "which of the following best describes your occupation?":
        return type_ignore
    if job == "other":
        return type_ignore
    if job == "desktop or enterprise applications developer":
        return type_desktop
    if job == "c-suite executive (ceo, cto, etc.)":
        return type_management
    if job == "embedded applications/devices developer":
        return type_embedded
    if job == "product manager":
        return type_ignore
    if job == "mobile application developer":
        return type_mobile
    if job == "mobile developer - windows phone":
        return type_mobile
    if job == "data scientist or machine learning specialist":
        return type_data_science
    if job == "educator or academic":
        return type_education
    if job == "embedded applications or devices developer":
        return type_embedded
    if job == "quality assurance engineer":
        return type_qa
    if job == "enterprise level services":
        return type_ignore
    if job == "full-stack developer":
        return type_fullstack
    if job == "na":
        return type_ignore
    if job == "academic researcher":
        return type_education
    if job == "manager of developers or team leader":
        return type_management
    if job == "marketing or sales manager":
        return type_marketer
    if job == "developer, back-end":
        return type_backend
    if job == "full-stack web developer":
        return type_fullstack
    if job == "designer or illustrator":
        return type_design
    if job == "programmer":
        return type_ignore
    if job == "developer":
        return type_ignore
    if job == "manager":
        return type_management
    if job == "engineer":
        return type_ignore
    if job == "sr. developer":
        return type_ignore
    if job == "full stack overflow developer":
        return type_fullstack
    if job == "ninja":
        return type_ignore
    if job == "mobile dev (android, ios, wp & multi-platform)":
        return type_mobile
    if job == "expert":
        return type_ignore
    if job == "rockstar":
        return type_ignore
    if job == "hacker":
        return type_ignore
    if job == "guru":
        return type_ignore
    if job == "self_identification":
        return type_ignore
    if job == "occupation_group":
        return type_ignore
    if job == "cloud infrastructure engineer":
        return type_devops
    if job == "project manager":
        return type_management
    if job == "security professional":
        return type_ops
    if job == "blockchain":
        return type_backend
    if (
        job
        == "mathematics developers (data scientists, machine learning devs & devs with stats & math backgrounds)"
    ):
        return type_data_science
    raise Exception(f"job not mapped: {job}")


main()

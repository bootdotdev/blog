import csv


def main():
    files = [
        (2013, 6),
        (2014, 6),
        (2015, 5),
        (2016, 9),
        (2017, 14, 15, 16, 17),
        (2018, 9),
        (2019, 12),
        (2020, 13),
        (2021, 11),
    ]

    out_dict = {}

    for f_tup in files:
        counts = {}
        path = f"csv/{f_tup[0]}.csv"
        print(f"generating report for {path}")
        out_dict[f_tup[0]]: {}
        count = 0
        with open(path, "r") as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            count = 0
            rows_cpy = []
            for row in rows:
                count += 1
                rows_cpy.append(row)
            for row in rows_cpy:
                try:
                    cell = row[f_tup[1]]
                    if len(f_tup) == 5:
                        cell += f";{row[f_tup[2]]}"
                        cell += f";{row[f_tup[3]]}"
                        cell += f";{row[f_tup[4]]}"
                    jobs = cell.split(";")
                    for job in jobs:
                        job = get_mapped_job(job)
                        if job not in counts:
                            counts[job] = 0
                        counts[job] += 1
                except Exception as e:
                    print(e)

            for job in counts:
                counts[job] /= count
                counts[job] *= 100
                counts[job] = round(counts[job], 2)
            out_dict[f_tup[0]] = counts

    with open("csv/out.csv", "w") as csvfile:
        w = csv.writer(csvfile)
        w.writerow(
            [
                "year",
                "devops",
                "backend",
                "frontend",
                "mobile",
                "fullstack",
                "desktop",
                "embedded",
                "database",
                "data science",
            ]
        )
        for year in out_dict:
            row = [
                year,
                out_dict[year]["devops"] if "devops" in out_dict[year] else 0,
                out_dict[year]["backend"] if "backend" in out_dict[year] else 0,
                out_dict[year]["frontend"] if "frontend" in out_dict[year] else 0,
                out_dict[year]["mobile"] if "mobile" in out_dict[year] else 0,
                out_dict[year]["fullstack"] if "fullstack" in out_dict[year] else 0,
                out_dict[year]["desktop"] if "desktop" in out_dict[year] else 0,
                out_dict[year]["embedded"] if "embedded" in out_dict[year] else 0,
                out_dict[year]["database"] if "database" in out_dict[year] else 0,
                out_dict[year]["data science"]
                if "data science" in out_dict[year]
                else 0,
            ]
            w.writerow(row)


def get_mapped_job(job):
    job = job.lower()
    if "devops" in job:
        return "devops"
    if "back" in job:
        return "backend"
    if "front" in job:
        return "frontend"
    if "mobile" in job:
        return "mobile"
    if "full" in job:
        return "fullstack"
    if "desktop" in job:
        return "desktop"
    if "embedded" in job:
        return "embedded"
    if "database" in job:
        return "database"
    if "data sc" in job:
        return "data science"
    return "other"


main()

import datetime
import os
import re
from typing import Mapping, Tuple, NamedTuple

FILENAME_REGEX = r"(\d{4})(\d{2})(\d{2}).csv"
COUNTRY_REGEX = r"(.*),(\d+),(\d+)"
available_dates: Tuple[datetime.datetime, ...] = ()
global_mapping: Mapping[str, Mapping[datetime.datetime, Tuple[int, int]]] = {}


class WhatToShow(NamedTuple):
    record_type: bool = True
    deaths: bool = True
    infections: bool = True


def parse_file(filename: str, file_date: datetime) -> None:
    with open(filename, "r") as f:
        for line in f.readlines():
            if len(line) < 2:
                continue
            parsed_country_record = re.search(COUNTRY_REGEX, line).groups()
            country = parsed_country_record[0]
            infected = int(parsed_country_record[1])
            dead = int(parsed_country_record[2])
            if global_mapping.get(country) is None:
                global_mapping[country] = {}
            global_mapping[country][file_date] = (infected, dead)


def parse_csv_files(src_dir: str) -> Tuple[datetime.datetime, ...]:
    now = datetime.datetime.now()
    directory = os.path.abspath(src_dir)
    dates = ()
    for filename in os.listdir(directory):
        file_date = datetime.datetime(*[int(g) for g in re.search(FILENAME_REGEX, filename).groups()])
        if file_date > now:
            continue
        print(f"processing \"{filename}\"...")
        parse_file(os.path.join(directory, filename), file_date)
        print(f"\"{filename}\" processed!")
        dates += (file_date,)
    return dates


def prepare_overall_stats(result_filename: str, show: WhatToShow) -> None:
    country_mappings = global_mapping.items()
    with open(os.path.abspath(result_filename), "w") as f:
        file_header = "date"
        dead_record_type = ""
        infected_record_type = ""
        if show.record_type:
            file_header += ",record type"
            dead_record_type = ",dead"
            infected_record_type = ",infected"
        file_header += "," + ",".join(country for country, _ in country_mappings)
        f.write(file_header + "\n")
        for d in sorted(available_dates):
            infected_row = ()
            dead_row = ()
            for country, ds in country_mappings:
                country_infected, country_dead = ds.get(d, (0, 0))
                infected_row += (str(country_infected),)
                dead_row += (str(country_dead),)
            if show.deaths:
                f.write(f"{d}{dead_record_type},{','.join(dead_row)}\n")
            if show.infections:
                f.write(f"{d}{infected_record_type},{','.join(infected_row)}\n")


if __name__ == "__main__":
    available_dates = parse_csv_files("./src")
    prepare_overall_stats("./reports/d-results.csv", WhatToShow(deaths=True, infections=False, record_type=False))
    prepare_overall_stats("./reports/i-results.csv", WhatToShow(deaths=False, infections=True, record_type=False))

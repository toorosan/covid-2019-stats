import datetime
import os
import re
from typing import Mapping, Tuple

FILENAME_REGEX = r"(\d{4})(\d{2})(\d{2}).csv"
COUNTRY_REGEX = r"(.*),(\d+),(\d+)"
global_mapping: Mapping[str, Mapping[datetime.datetime, Tuple[int, int]]] = {}


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


def main(result_filename: str):
    now = datetime.datetime.now()
    directory = os.path.abspath("./src")
    dates = ()
    for filename in os.listdir(directory):
        file_date = datetime.datetime(*[int(g) for g in re.search(FILENAME_REGEX, filename).groups()])
        if file_date > now:
            continue
        print(f"processing \"{filename}\"...")
        parse_file(os.path.join(directory, filename), file_date)
        print(f"\"{filename}\" processed!")
        dates += (file_date,)
    country_mappings = global_mapping.items()
    with open(os.path.join(directory, f"../{result_filename}"), "w") as f:
        f.write(f"date,record type,{','.join(country for country, _ in country_mappings)}\n")
        for d in sorted(dates):
            infected_row = ()
            dead_row = ()
            for country, ds in country_mappings:
                country_infected, country_dead = ds.get(d, (0, 0))
                infected_row += (str(country_infected),)
                dead_row += (str(country_dead),)
            f.write(f"{d},infected,{','.join(infected_row)}\n")
            f.write(f"{d},dead,{','.join(dead_row)}\n")


if __name__ == "__main__":
    main("result.csv")

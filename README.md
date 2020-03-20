# Covid-2019 stats

Got the statistics from ["Сoronavirus outbreak" telegram channel](https://t.me/coronavirus_outbreak), using following algorithm: 
1. Copy the message with the stats by the start of the day.
2. Apply following replacements to the text, until nothing left to be replaced in the source text:
    - `(Latest updates on the Wuhan coronavirus outbreak:|\+| • |\n\n|^ |\*)` -> `empty string`
    - `( - | / )` -> `,`
    - `(\d)-` -> `$1`
3. Save result as `YYYYMMDD.csv` (e.g. `20200320.csv`) file in `src` directory
4. Run parser to get overall `result.csv` file, fixed country name and numbers related issues.

## Requirements
- Python3.6+

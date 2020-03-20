# Covid-2019 stats

## Google Sheets charts build from sources:
![Infections global - China - Italy](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=1201767191&format=image)
![Deaths global - China - Italy](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=228379056&format=image)
![Infections, Italy](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=437717484&format=image)
![Deaths, Italy](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=1628789429&format=image)
![Infections, China (up to 40k infections)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=2010688729&format=image)
![Deaths, China (up to 40k infections)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSQpSVqADWMEZZH15SXbz4RTUPwhcLqbSIQTkHA4XgMJ5zhH4Zs7cO6T188XNxrnGlFQ8hQQO1Ywpk-/pubchart?oid=403228266&format=image)


## Background

Got the statistics from ["Сoronavirus outbreak" telegram channel](https://t.me/coronavirus_outbreak), using following algorithm: 
1. Copy the message with the stats by the start of the day.
2. Apply following replacements to the text, until nothing left to be replaced in the source text:
    - `(Latest updates on the Wuhan coronavirus outbreak:|\+| • |\n\n|^ |\*)` -> `empty string`
    - `( - | / )` -> `,`
    - `(\d)-` -> `$1`
3. Save result as `YYYYMMDD.csv` (e.g. `20200320.csv`) file in `src` directory
4. Run parser to get overall `result.csv` file, fixed country name and numbers related issues.

## Parser requirements
- Python3.6+

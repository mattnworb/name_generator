## About

Script to generate random names (first and last names) based on how often the names are used in Census data (although any type of data can be used as long as it is in CSV format).

## Usage

    usage: name_generator.py [-h] firstnames lastnames [N]

    Generates random names.

    positional arguments:
      firstnames  Path to CSV file of first names
      lastnames   Path CSV file of last names
      N           Optional, number of names to generate (default=1)

    optional arguments:
      -h, --help  show this help message and exit

    The CSV files must contain a name in the first column and a weight in the
    second column. The weights can be in any format/range as long as they are
    positive numbers; the math works out the same if a weight of 10% is expressed
    as "10" or "0.10".


The name data is taken from http://names.mongabay.com/male_names_alpha.htm and http://names.mongabay.com/most_common_surnames.htm.

[Matt Brown](www.mattnworb.com) <matt@mattnworb.com>
11/28/2011

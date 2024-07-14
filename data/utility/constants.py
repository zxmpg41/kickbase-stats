from datetime import datetime

import pytz

TIMEZONE_DE = pytz.timezone('Europe/Berlin')

# 2 Bayern
# 3 BVB
# 4 Frankfurt
# 5 Freiburg
# 7 Bayer
# 8 Schalke
# 9 Stuttgart
# 10 Bremen
# 11 Wolfsburg
# 13 Augsburg
# 14 Hoffenheim
# 15 Gladbach
# 18 Mainz
# 24 Bochum
# 40 Union
# 43 Leipzig
# 50 Heidenheim
# 39 Pauli
# 51 Kiel
TEAM_IDS = [2, 3, 4, 5, 7, 9, 10, 11, 13, 14, 15, 18, 24, 39, 40, 43, 50, 51]

POSITIONS = {1: 'TW', 2: 'ABW', 3: 'MF', 4: 'ANG'}

CUTOFF_DATE = datetime(2024, 7, 17, tzinfo=TIMEZONE_DE)
CUTOFF_DATE_STRING = '2024-07-17T00:00:00.000Z'

MATCH_DAYS = {
    1: datetime(2024, 8, 16, 20, 30, tzinfo=TIMEZONE_DE),
    2: datetime(2024, 8, 23, 20, 30, tzinfo=TIMEZONE_DE),
    3: datetime(2024, 8, 30, 20, 30, tzinfo=TIMEZONE_DE),
    4: datetime(2024, 9, 13, 20, 30, tzinfo=TIMEZONE_DE),
    5: datetime(2024, 9, 20, 20, 30, tzinfo=TIMEZONE_DE),
    6: datetime(2024, 9, 27, 20, 30, tzinfo=TIMEZONE_DE),
    7: datetime(2024, 10, 4, 20, 30, tzinfo=TIMEZONE_DE),
    8: datetime(2024, 10, 18, 20, 30, tzinfo=TIMEZONE_DE),
    9: datetime(2024, 10, 26, 20, 30, tzinfo=TIMEZONE_DE),
    10: datetime(2024, 11, 1, 20, 30, tzinfo=TIMEZONE_DE),
    11: datetime(2024, 11, 8, 20, 30, tzinfo=TIMEZONE_DE),
    12: datetime(2024, 11, 22, 20, 30, tzinfo=TIMEZONE_DE),
    13: datetime(2024, 11, 29, 20, 30, tzinfo=TIMEZONE_DE),
    14: datetime(2024, 12, 6, 20, 30, tzinfo=TIMEZONE_DE),
    15: datetime(2024, 12, 13, 20, 30, tzinfo=TIMEZONE_DE),
    16: datetime(2024, 12, 20, 20, 30, tzinfo=TIMEZONE_DE),
    17: datetime(2025, 1, 10, 20, 30, tzinfo=TIMEZONE_DE),
    18: datetime(2025, 1, 17, 20, 30, tzinfo=TIMEZONE_DE),
    19: datetime(2025, 1, 24, 20, 30, tzinfo=TIMEZONE_DE),
    20: datetime(2025, 1, 31, 20, 30, tzinfo=TIMEZONE_DE),
    21: datetime(2025, 2, 7, 20, 30, tzinfo=TIMEZONE_DE),
    22: datetime(2025, 2, 14, 20, 30, tzinfo=TIMEZONE_DE),
    23: datetime(2025, 2, 21, 20, 30, tzinfo=TIMEZONE_DE),
    24: datetime(2025, 2, 28, 20, 30, tzinfo=TIMEZONE_DE),
    25: datetime(2025, 3, 7, 20, 30, tzinfo=TIMEZONE_DE),
    26: datetime(2025, 3, 14, 20, 30, tzinfo=TIMEZONE_DE),
    27: datetime(2025, 3, 28, 20, 30, tzinfo=TIMEZONE_DE),
    28: datetime(2025, 4, 4, 20, 30, tzinfo=TIMEZONE_DE),
    29: datetime(2025, 4, 11, 20, 30, tzinfo=TIMEZONE_DE),
    30: datetime(2025, 4, 18, 20, 30, tzinfo=TIMEZONE_DE),
    31: datetime(2025, 4, 25, 20, 30, tzinfo=TIMEZONE_DE),
    32: datetime(2025, 5, 2, 20, 30, tzinfo=TIMEZONE_DE),
    33: datetime(2025, 5, 9, 20, 30, tzinfo=TIMEZONE_DE),
    34: datetime(2025, 5, 17, 20, 30, tzinfo=TIMEZONE_DE)
}
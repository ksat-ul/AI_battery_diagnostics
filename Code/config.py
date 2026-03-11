from enum import IntEnum
import numpy as np


# --- path definitions --- ToDo: you have to adjust these paths! -------------------------------------------------------
CSV_RESULT_DIR = "/Users/33574/Projects/Battery/Results/"  # ToDo: change path to where you place the .csv files

LOG_DIR = CSV_RESULT_DIR + "log\\"  # sub-directory for Python script logs
IMAGE_OUTPUT_DIR = CSV_RESULT_DIR + "images\\"  # output directory for images (e.g., .png, .pdf, .html)
CHECK_OUTPUT_DIR = CSV_RESULT_DIR + "check\\"  # output for plausibility check file


# CSV row names
CSV_SEP = ";"
CSV_NEWLINE = "\n"
CSV_NAN = "nan"
DELTA_T_LOG = 1.99950336  # CM0 * 2^16 / f_STM = 3051 * 65536 / 100 000 000
DELTA_T_STM_TICK = 0.01048576  # seconds per STM tick
DELTA_T_REBOOT = 4  # assume a reboot takes 4 seconds

# slave general configuration
NUM_SLAVES_MAX = 20
NUM_CELLS_PER_SLAVE = 12
NUM_POOLS_PER_TMGMT = 4
NUM_PELTIERS_PER_POOL = 4


AGE_TEMPERATURE_UNDEFINED = 126
AGE_TEMPERATURE_MANUAL = 127

AGE_SOC_UNDEFINED = 254
AGE_SOC_MANUAL = 255

AGE_RATE_UNDEFINED = 0

AGE_PROFILE_TEXTS = ["none", "test", "WLTP 3b complete, SoC: 10 - 100 %",
                     "WLTP 3b complete, SoC: 10 - 90 %", "WLTP 3b extra high, SoC: 10 - 90 %"]
AGE_PROFILE_TEXTS_SHORT = ["-", "test profile", "10-100 %, +0.33 Cc, WLTP 3b",
                           "10-90 %, +0.33 Cc, WLTP 3b", "10-90 %, +1.67 Cc, WLTP 3b high"]

AGE_PROFILE_SOC_MIN = [np.nan, 10, 10, 10, 10]
AGE_PROFILE_SOC_MAX = [np.nan, 90, 100, 90, 90]
AGE_PROFILE_CHG_RATE = [np.nan, 90, 100, 90, 90]


# definitions for experiment
EXPERIMENT_START_TIMESTAMP = 1665593100  # -> Mi, 12.10.2022  16:45:00 UTC see schedule_2022-10-12_experiment_LG_HG2.txt
# FIRST_USE_START_TIMESTAMP = EXPERIMENT_START_TIMESTAMP - (5 * 60)  # in LOG ext, delete data >5 min before experiment
FIRST_USE_START_TIMESTAMP = 1665598800  # in LOG ext, delete data before Mi, 12.10.2022  18:20:00 UTC, because there
# were issues with slave 4 (needed multiple reboots, first few hundred data sets have invalid timestamps with test data

CELL_PRODUCTION_TIMESTAMP = 1606392000  # 26.11.2020 12:00 UTC (estimated, based on the printed "+DT331K262A -")
CELL_STORAGE_VOLTAGE = 3.5558  # in V, +/- 50 mV, voltage at which the cell was stored before experiment (as it arrived)
# CELL_STORAGE_SOC = 26.7  # in % (100 = 100%), +/- 1%, SoC at which the cell was stored before the experiment
CELL_STORAGE_TEMPERATURE = 18  # in °C, average (estimated) temperature at which the cell was stored before experiment

CELL_CAPACITY_NOMINAL = 3.0  # in Ah
CELL_ENERGY_NOMINAL = 11.0  # in Wh

CELL_CAPACITY_MAX_PLAUSIBLE_CHG = 1.05 * CELL_CAPACITY_NOMINAL  # 3.15 Ah
CELL_CAPACITY_MAX_PLAUSIBLE_DISCHG = 1.05 * CELL_CAPACITY_NOMINAL  # 3.15 Ah
CELL_ENERGY_MAX_PLAUSIBLE_CHG = 1.2 * CELL_ENERGY_NOMINAL  # 13.2 Wh
CELL_ENERGY_MAX_PLAUSIBLE_DISCHG = 1.2 * CELL_ENERGY_NOMINAL  # 13.2 Wh


LIMIT_END_OF_LIFE_CAPACITY_FAC_CU = 0.5
LIMIT_END_OF_LIFE_CAPACITY_FAC_CYC = 0.4
LIMIT_END_OF_LIFE_IMPEDANCE_FAC_IMP = 3.0

T0 = 273.15  # in Kelvin, temperature at 0°C


# Programmers:  Hazel, Jalen Henderson
# Course:  CS151, Zelalem Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: This program is designed to compute change in population of a certain country.
# Data In: birth rate, death rate, migration rate, current population, number of years into future
# Data Out:  Future population, whether it has increased or decreased

#Store variable to represent number of seconds per year
seconds_per_year = 31536000

#Prompt user to enter inputs.
birth_rate = float(input("How many seconds between births?"))
death_rate = float(input("How many seconds between deaths?"))
migration_rate = float(input("How many seconds between immigrations?"))
current_population = float(input("What is the current population?"))
future_years = float(input("How many years in the future?"))

#Calculate future population
future_population = ((seconds_per_year / birth_rate) - (seconds_per_year / death_rate) +
                     (seconds_per_year / migration_rate)) * future_years

#
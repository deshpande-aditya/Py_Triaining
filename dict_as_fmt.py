
##Dictionary - these are similar to formats in sas.
days_ofweek = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

print(days_ofweek.get(1, "Only 7 days in a week - Stupid!"))
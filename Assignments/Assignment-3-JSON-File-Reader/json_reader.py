# SkillNexis Python Programming
# Week 2 - Assignment 3
# JSON File Reader

import json


def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        print("\n========== JSON DATA ==========")
        print(json.dumps(data, indent=4))
        print("===============================")

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    except Exception as e:
        print("Error:", e)


print("================================")
print("        JSON FILE READER")
print("================================")

filename = input("Enter JSON file name: ")

read_json_file(filename)
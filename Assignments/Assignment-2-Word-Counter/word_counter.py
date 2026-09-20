# SkillNexis Python Programming
# Week 2 - Assignment 2
# Word Counter from Text File


def count_text_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        print("\n========== FILE STATISTICS ==========")
        print("Number of lines:", len(lines))
        print("Number of words:", len(words))
        print("Number of characters:", characters)
        print("=====================================")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)


print("================================")
print("       WORD COUNTER")
print("================================")

filename = input("Enter text file name: ")

count_text_file(filename)
"""
chargen.py
Problem: Generate a description for a fantasy role-playing character.
Target Users: Me and my friends
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: Print out the character sheet
		        User must be able to input the character's
 			name, description, gender and race
Testing: Simple run test
Maintainer: maintainer@website.com
"""

__version__ = 0.1

Name = ""
Desc = ""
Gender = ""
Race = ""

# Prompt user for use-defined information
Name = input('What us your Name? ')
Desc = input('Describle yourself: ')
Gender = input('What Gender are you? (male / female / unsure): ')
Race = input('What fantasy Race are you? - (Pixie / Vulcan / Gelfling / Troll): ')

# Output the character sheet
fancy_line = "<~~==|#|==~~++**\@/**++~~|#|==~~>"
print("\n", fancy_line)
print("\t", Name)
print("\t", Race, Gender)
print("\t", Desc)
print(fancy_line, "\n")

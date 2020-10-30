# Communtiy Bot

This is a bot created so that developers of all skill levels can contribute to this project.

# Before Contributing

To make this bot easy for people to upgrade and contribute in the future, certain coding guidelines need
to be followed.

Before developing, create a text file "creds" with no extension. This is where you add your discord API token.
Make sure you don't upload this along with your project.

1. Add your discord tag at the top of the main.py file.
2. Update the end of this README file to give a description of your contributions.
3. Please comment your code! Make sure that people who may upgrade your future are able to easily understand your code.
4. Follow PEP8 styling guides.

This bot uses sqlite3 to store data. If you're doing anything related with data it's crucial you store all of it in the
communitybot.db file. SQL has very simple syntax and can be learned in under an hour.

# Features

When adding to the bottom of this file, please follow the format that's used in the "Leveling System" description.

# Leveling System

Feature Creator: Anton#2908
Files: main.py, sqlActions.py
Description: Leveling system based on a radical function.

Breakdown:
When a user sends a message, their xp is updated and stored in the database. When a user runs the !level command,
a query is sent to the database to retrieve their xp. After that, their level is multiplied by the "curve" variable.
This value is then square rooted and all the decimals are removed. This is their level.

This command is actually ran each time a message is set. Using this logic, if the new level is higher than the old
level then a message is sent to the channel.
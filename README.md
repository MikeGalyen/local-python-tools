# A Collection of Tools to be Used for Local Tasks
### Clone this repo: `git clone <repo url>`
### This project is set up as a uv project so .py files can be run with either:
`uv run <tool-name>.py` 
### or  
`python <tool-name>.py`
##
## Tools
- **file_name_formatter.py** formats files and dirs to use a standard format. Converts directory names to be all uppercase, file names to be all lowercase, and converts hyphens to underscores. There are lists of files and dirs to not skip without changing the name. I like to use this format for document directories mainly. I wouldn't use it for code directories usually but for now some typical code project patterns will be included in ignore list just in case.

- ### Upcoming changes to add to the file formatter:
        - The ability to use wilcard patterns in the ignore list
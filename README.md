# discogs-collection-export

A simple script that exports your Discogs collection data to a CSV file.

# Initial setup:
1. Install the <b>python3-discogs-client</b> and <b>pandas</b> Python libraries. To install, run the following in the command prompt/terminal:
- <i>pip install python3-discogs-client</i>
- <i>pip install pandas</i>

2. Generate a user token for you Discogs account. To do so:
- Log in to your Discogs account.
- Click on your user account (top right of screen.)
- Click "Settings” and then “Developers.”
- Click “Generate new token."

3. Copy token and paste it into the "MyToken" variable in the script.

# Notes
- The collection will be exported as <b>discogs-collection.csv</b>.
- The export is sorted by artist name, and then album release year.

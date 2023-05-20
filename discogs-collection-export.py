import discogs_client
import pandas as pd

#Enter your token below:
MyToken = ""

if MyToken == "":
        exit("Please enter your Discogs token before running this script!")

#Connects to Discogs profile
d = discogs_client.Client('my_user_agent/1.0', user_token=MyToken)
me = d.identity()

#Grabs collection
print ("Grabbing collection data...")
Collection = [r.release for r in me.collection_folders[0].releases]

#Creates dataframe and column names
df = pd.DataFrame(columns = ['Artist', 'Title', 'PrimaryGenre', 'SecondaryGenres', 'Year', 'Format'])

#Loops through each record in collection and grabs column info
print ("Generating CSV...")
for r in Collection:

    #Artist column
    Artists = [a.name for a in r.artists] #Grabs first artist in list
    Artist = str(Artists[0]) #Converts artist name to string
 
    #Title column
    Title = str(r.title)

    #PrimaryGenre and SecondyGenre columns    
    PrimaryGenre = r.genres[0]      #only grabs first Genre in the list
    if len(r.genres) > 1:           #Adds Secondary Genres if Genres list contains more than one item
        SecondaryGenres = ", ".join(r.genres[1:])
    else:
        SecondaryGenres = "N/A"
    
    #Year Column    
    Year = str(r.year)
    if Year == "0":     #Albums with no year listed will appear as 'N/A'
        Year = "N/A"

    #Format column
    Format = str(r.formats) 
    if "Vinyl" in Format:         #Sets column based on contents of string
        Format = "Vinyl"
    elif "CD" in Format:
        Format = "CD"
    elif "Cassette" in Format:
        Format = "Cassette"
    else:
        Format = "Other"

    #Adds record to row
    df.loc[len(df.index)] = [Artist, Title, PrimaryGenre, SecondaryGenres, Year, Format]

#Sorts by Artist and album release year
df = df.sort_values(by=["Artist", "Year"])

#Exports dataframe to CSV
df.to_csv('discogs-collection.csv', index=False)

print ("DONE! Discogs collection exported to discogs-collection.csv")
input("Press Enter to complete.")
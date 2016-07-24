text = "Zip is a file format used for data compression and archiving. A zip file contains one or more files that have been compressed, to reduce file size, or stored as is. The zip file format permits a number of compression algorithms."

# ENTER CODE BELOW HERE
text = text.lower()
newtext = text.find('zip')
newtext = text.find('zip', newtext + 1)

print newtext

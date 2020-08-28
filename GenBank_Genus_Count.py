from Bio import Entrez

def genbank(genus, dtstart, dtend):
	Entrez.email = "aia5618@psu.edu"
	term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend)
	handle = Entrez.esearch(db="nucleotide", term=term)
	record = Entrez.read(handle)
	return record["Count"]

# Tests
print (genbank("Bothrocophias", "2001/10/19", "2008/02/22"))

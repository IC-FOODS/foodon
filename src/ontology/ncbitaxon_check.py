content_dict = set();

for file_name in ['imports/ncbitaxon', 'imports/ncbitaxon2']:
	print ();
	print ("Checking for missing ids in", file_name + '_import.owl')
	with open(file_name + '_import.owl', 'r') as owl_handler:

		for term in owl_handler.read().splitlines():
			term = term.strip();
			if term.split('_')[0] == '<owl:Class rdf:about="http://purl.obolibrary.org/obo/NCBITaxon':
				id = term.split('_')[1].split('"')[0];
				content_dict.add(id);

	with open(file_name + '_ontofox.txt', 'r') as lookup_handler:

		for term in lookup_handler.read().splitlines():
			if term.split('_')[0] == 'http://purl.obolibrary.org/obo/NCBITaxon':
				id = term.split('_')[1].split(' ')[0].split('\t')[0];
				if id not in content_dict:
					print ('['+id+']', );



To regenerate an owl file from a robot template, run this style of command:
NOTE: --input command ONLY ALLOWS ONE INPUT file; if you do multiple --input
only LAST one is used.

robot template --template wine.tsv \
  --input "../general_import.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_wine.owl" \
  --output ../robot_wine.owl

robot template --template pasta.tsv \
  --input "../general_import.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_pasta.owl" \
  --output ../robot_pasta.owl

robot template --template fdc.tsv \
  --input "../general_import.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_fdc.owl" \
  --output ../robot_fdc.owl

robot template --template plant_parts.tsv \
  --input "../../foodon-merged.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_plant_parts.owl" \
  --output ../robot_plant_parts.owl


robot template --template process.tsv\
  --input "../../foodon-merged.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_process.owl" \
  --output ../robot_process.owl

robot template --template dietary_supplement.tsv\
  --input "../../foodon-merged.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/dietary_supplement_import.owl" \
  --output ../robot_dietary_supplement.owl

robot template --template animals.tsv\
  --input "../../foodon-merged.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_animals.owl" \
  --output ../robot_animals.owl

robot template --template seafood.tsv\
  --input "../../foodon-merged.owl" \
  --ontology-iri "http://purl.obolibrary.org/obo/foodon/imports/robot_seafood.owl" \
  --output ../robot_seafood.owl

The --input parameter is used to bring in .owl entities that are referenced in axioms
The --prefix parameter is used to expand abbreviated namespace URLs.
All output files get delivered to parent directory.  Manually import them in FoodOn (in Active Ontology -> Ontology Imports section of Protege.

from qwikidata.sparql import return_sparql_query_results

# get country name and URL of flag image
sparql_query = """
SELECT DISTINCT ?nameLabel ?urlLabel
WHERE {
  ?country wdt:P31 wd:Q6256.
  ?country wdt:P163 ?flag.
  ?country wdt:P17 ?name.
  ?flag wdt:P18 ?url.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""
res = return_sparql_query_results(sparql_query)
flags = dict()

for country in res['results']['bindings']:
    flags[country['nameLabel']['value']] = country['urlLabel']['value']

print(flags)

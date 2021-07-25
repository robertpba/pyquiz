from qwikidata.sparql import return_sparql_query_results

# get country name and URL of flag image
sparql_query = """
SELECT DISTINCT ?nameLabel ?urlLabel
WHERE {
  ?country wdt:P31 wd:Q6256.    # get all countries
  ?country wdt:P163 ?flag.      # get flag of country
  ?country wdt:P17 ?name.       # get name of country
  ?flag wdt:P18 ?url.           # get url of flag svg image
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""
res = return_sparql_query_results(sparql_query)
flags = dict()

for country in res['results']['bindings']:
    flags[country['nameLabel']['value']] = country['urlLabel']['value']

print(flags)

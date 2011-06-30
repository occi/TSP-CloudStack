__author__ = 'machar_s'


from io import StringIO
from lxml import etree #http://pypi.python.org/pypi/lxml/2.3

app_path = 'C:\\#STAGE_final\\TSP-CloudStack\\src\\it\\tsp\\cloudstack\\orbac'

xsd_file = open( app_path + '\\XOrbac\\db_orbac_organizations.xsd', mode='r')
schema = xsd_file.read()
#schema = schema[3:]
print (schema)
schema = StringIO(schema)
xmlschema_doc = etree.parse(schema)
print(xmlschema_doc)
#xmlschema = etree.XMLSchema(xmlschema_doc)
#f = StringIO(xsd_file.read(xsd_file) )



"""/
xmlschema_doc = etree.parse(f)
xmlschema = etree.XMLSchema(xmlschema_doc)



valid = StringIO('<a><b></b></a>')
doc = etree.parse(valid)
print(xmlschema.validate(doc))


invalid = StringIO('<a><b></b></a>')
doc2 = etree.parse(invalid)
print(doc2)

print (xmlschema.validate(doc2))
#xmlschema.assertValid(doc2)
xmlschema.assert_(doc2)
"""
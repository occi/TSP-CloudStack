__author__ = 'machar_s'

from lxml import etree #for x in list(dir(etree)): print (x)
from copy import deepcopy


app_path = 'C:\\#STAGE_final\\TSP-CloudStack\\src\\it\\tsp\\cloudstack\\orbac'
f= open( app_path + '\\XOrbac\\organizations.xml', mode='r')
root = etree.XML(f.read())
#print (etree.tostring(root))
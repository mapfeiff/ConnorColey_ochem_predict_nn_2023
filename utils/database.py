#from pymongo import MongoClient    # mongodb plugin
#client = MongoClient('mongodb://username:password@server.com/authenticationDB', 27017)

#Referencing Post: https://stackoverflow.com/questions/27527982/read-bson-file-in-python
#As well as: https://pymongo.readthedocs.io/en/stable/api/bson/index.html
#And also: https://leihao911358328.wordpress.com/2018/12/17/how-to-deal-with-bson-file-in-python/
#And also: https://pymongo.readthedocs.io/en/3.6.1/api/bson/index.html
#And Also: https://stackoverflow.com/questions/34320177/python-convert-bson-output-of-mongodump-to-array-of-json-objects-dictionaries

import bson
from bson.codec_options import CodecOptions
import collections

def collection_example_reactions_smilesonly():
    #db = client['reaction_examples']
    #collection = db['lowe_1976-2013_USPTOgrants']
    filename = "database/reaction_examples/lowe_1976-2013_USPTOgrants"
    filename += ".bson"
    options = CodecOptions(document_class=collections.OrderedDict)
    with open(filename, 'rb') as f:
      #Create a list of ordered dictionaries (i.e., a collection)
      collection = bson.decode_all(f.read(), options)
    return collection

def collection_example_reactions_details():
    #db = client['reaction_examples']
    #collection = db['lowe_1976-2013_USPTOgrants_reactions']
    filename = "database/reaction_examples/lowe_1976-2013_USPTOgrants_reactions"
    filename += ".bson"
    options = CodecOptions(document_class=collections.OrderedDict)
    with open(filename, 'rb') as f:
      #Create a list of ordered dictionaries (i.e., a collection)
      collection = bson.decode_all(f.read())
    return collection

def collection_templates():
    #db = client['askcos_transforms']
    #collection = db['lowe_refs_general_v3']
    filename = "database/askcos_transforms/lowe_refs_general_v3"
    filename += ".bson"
    options = CodecOptions(document_class=collections.OrderedDict)
    with open(filename, 'rb') as f:
      #Create a list of ordered dictionaries (i.e., a collection)
      collection = bson.decode_all(f.read(), options)
    return collection

def collection_candidates():
    #db = client['prediction']
    #collection = db['candidate_edits_8_9_16']
    filename = "database/prediction/candidate_edits_8_9_16"
    filename += ".bson"
    options = CodecOptions(document_class=collections.OrderedDict)
    with open(filename, 'rb') as f:
      #Create a list of ordered dictionaries (i.e., a collection)
      collection = bson.decode_all(f.read())
    return collection 
'''
Created on 18 nov. 2011

@author: JD219546
'''

from xml.etree import ElementTree as ET

class XML_tools(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        
        
    def get_xml_tree(self, xml_file):
        tree = ET.parse(xml_file)
        return tree
    
XML_tools = XML_tools()
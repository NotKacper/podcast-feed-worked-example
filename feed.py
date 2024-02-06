import yaml
import xml.etree.ElementTree as xml_tree

with open("feed.yaml",'r') as file:
    yaml_data = yaml.safe_load(file) #loads the .yaml file, ensuring it loads correctly.

rss_element = xml_tree.Element('rss', { # this creates an rss element - an element is a tag in the XML language (like an element in HTML)
'version':'2.0',
'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_element = xml_tree.SubElement(rss_element, 'channel') # creates a channel tag inside of the main rss element

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title'] # creates a title sub element inside the channel element.

output_tree = xml_tree.ElementTree(rss_element) # creates an XML tree representing the XML file.

output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True) # writes the XML tree to an XML file called podcast.xml
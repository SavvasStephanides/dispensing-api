import xml.etree.ElementTree as XML

class XmlDAO:
    def get_xml_as_tree(self, file_name_prefix):
        xml_file_tree = XML.parse("/uploads/" + file_name_prefix + ".xml")
        return xml_file_tree
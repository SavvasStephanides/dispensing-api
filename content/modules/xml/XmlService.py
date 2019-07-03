from modules.xml.XmlDAO import XmlDAO

class XmlService:
    def get_xml_as_tree(self, file_name_prefix):
        xmlDao = XmlDAO()
        tree = xmlDao.get_xml_as_tree(file_name_prefix)
        return tree


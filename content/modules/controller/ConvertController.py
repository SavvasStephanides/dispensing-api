from modules.xml.XmlService import XmlService
from modules.mapper.XmlToJsonMapper import XmlToJsonMapper
from modules.mapper.JsonToExcelMapper import JsonToExcelMapper

class ConvertController:
    def convert_xml_to_excel(self, file_name_prefix):
        xmlService = XmlService()

        xml_tree = xmlService.get_xml_as_tree(file_name_prefix)
        xml_to_json_mapper = XmlToJsonMapper(xml_tree)
        details = xml_to_json_mapper.map_xml_tree_to_mapper()

        json_to_excel_mapper = JsonToExcelMapper(details)
        json_to_excel_mapper.map_dispensation_details_to_excel_workbook(file_name_prefix)
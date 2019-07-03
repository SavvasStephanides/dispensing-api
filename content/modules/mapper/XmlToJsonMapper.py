class XmlToJsonMapper:

    def __init__(self, xml_tree):
        self.root = xml_tree.getroot()

    def map_xml_tree_to_mapper(self):
        timestamp = self.get_timestamp()
        dispensations = self.get_dispensations()

        details = {
            "timestamp": timestamp,
            "dispensations": dispensations
        }

        return details

    def get_timestamp(self):
        header = self.root.find("Header")
        timestamp = header.find("Timestamp").text
        return timestamp

    def get_dispensations(self):
        details = []

        drug_items = self.root.find("DrugItems")
        dispensations = drug_items.findall("Drug")

        for each_dispensation in dispensations:
            
            quantity_prescribed = each_dispensation.find("QtyPresc").text
            quantity_dispensed = each_dispensation.find("QtyDisp").text
            drug_name = each_dispensation.find("Description").text
            reimbursement = each_dispensation.find("HIOAmount").text
            copayment_amount = each_dispensation.find("BeneficiaryCopaymentAmount").text

            details.append(
                {
                    "quantity_prescribed": quantity_prescribed, 
                    "quantity_dispensed": quantity_dispensed, 
                    "drug": drug_name,
                    "reimbursement": reimbursement,
                    "copayment_amount": copayment_amount
                }
            )

        return details
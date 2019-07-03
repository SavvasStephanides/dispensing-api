import xlsxwriter

class JsonToExcelMapper:
    def __init__(self, dispensation_details):
        self.dispensation_details = dispensation_details

    def map_dispensation_details_to_excel_workbook(self, file_name_prefix):
        workbook = xlsxwriter.Workbook('/exceloutput/' + file_name_prefix + '.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write("A1", "Date")
        worksheet.write("B1", "Drug")
        worksheet.write("C1", "Quantity prescribed")
        worksheet.write("D1", "Quantity dispensed")
        worksheet.write("E1", "Beneficiary copayment amount")
        worksheet.write("F1", "HIO reimbursement")

        date = self.dispensation_details["timestamp"]

        for index, each_dispensation in enumerate(self.dispensation_details["dispensations"], start=2):
            quantity_prescribed = each_dispensation["quantity_prescribed"]
            quantity_dispensed = each_dispensation["quantity_dispensed"]
            drug = each_dispensation["drug"]
            reimbursement = each_dispensation["reimbursement"]
            copayment_amount = each_dispensation["copayment_amount"]

            worksheet.write("A" + str(index), date)
            worksheet.write("B" + str(index), drug)
            worksheet.write("C" + str(index), quantity_prescribed)
            worksheet.write("D" + str(index), quantity_dispensed)
            worksheet.write("E" + str(index), copayment_amount)
            worksheet.write("F" + str(index), reimbursement)
            
        workbook.close()
    
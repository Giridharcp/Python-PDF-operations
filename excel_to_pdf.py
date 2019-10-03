from win32com import client
from appJar import gui
from pathlib import Path

def Excel_to_pdf():
   def excel_to_pdf(input_file,output_file):
      xlApp = client.Dispatch("Excel.Application")
      books = xlApp.Workbooks.Open(input_file)
      ws = books.Worksheets[0]
      ws.Visible = 1
      out_file=str(output_file)# desktop\file.pptx
      out_file+=".pdf"
      ws.ExportAsFixedFormat(0,out_file )
      print("PPTX to PDF conversion sucessful and Saved")
      if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
           app.stop()


   def validate_inputs(src_file, dest_dir, out_file):

        errors = False
        error_msgs = []
        if Path(src_file).suffix.upper() != ".XLSX":
           errors = True
           error_msgs.append("Please select a .PPTX input file")
           
        if not(Path(dest_dir)).exists():
           errors = True
           error_msgs.append("Please Select a valid output directory")

       # Check for a file name
        if len(out_file) < 1:
           errors = True
           error_msgs.append("Please enter a file name")
           
        return(errors, error_msgs)


   def press(button):
       if button=="Process":
           src_file = app.getEntry("Input_File")
           dest_dir = app.getEntry("Output_Directory")
           out_file = app.getEntry("Output_name")
           errors, error_msg = validate_inputs(src_file, dest_dir, out_file)
           if errors:
               app.errorBox("Error", "\n".join(error_msg), parent=None)
           else:
              excel_to_pdf(src_file,Path(dest_dir,out_file))
       else:
           app.stop()


   app=gui("Excel to PDF Converter", useTtk=True)
   app.setTtkTheme('alt')
   app.setSize(500, 200)

   # Add the interactive components
   app.addLabel("Choose Source Excel File to convert ")
   app.addFileEntry("Input_File")


   app.addLabel("Select Output Directory")
   app.addDirectoryEntry("Output_Directory")

   app.addLabel("Output file name")
   app.addEntry("Output_name")

   app.addButtons(["Process", "Quit"],press)
   app.go()


Excel_to_pdf()

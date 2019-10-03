import sys
import os
import win32com.client
from appJar import gui
from pathlib import Path

wdFormatPDF = 17
def Word_to_pdf():   
   def word_to_pdf(input_file,output_file):
      in_file =input_file
      out_file = str(output_file)+'.pdf'
      
      word = win32com.client.Dispatch('Word.Application')
      doc = word.Documents.Open(in_file)
      doc.SaveAs(out_file, FileFormat=wdFormatPDF)
      doc.Close()
      word.Quit()
      print(".DOCX to PDF conversion sucessful and Saved")
      if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
           app.stop()


   def validate_inputs(src_file, dest_dir, out_file):

        errors = False
        error_msgs = []
        if Path(src_file).suffix.upper() != ".DOCX":
           errors = True
           error_msgs.append("Please select a .DOC or .DOCX   input file")
           
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
             word_to_pdf(src_file,Path(dest_dir,out_file))
       else:
           app.stop()


   app=gui("Word to PDF Converter", useTtk=True)
   app.setTtkTheme('alt')
   app.setSize(500, 200)

   # Add the interactive components
   app.addLabel("Choose Source Word File to convert ")
   app.addFileEntry("Input_File")


   app.addLabel("Select Output Directory")
   app.addDirectoryEntry("Output_Directory")

   app.addLabel("Output file name")
   app.addEntry("Output_name")

   app.addButtons(["Process", "Quit"],press)
   app.go()
Word_to_pdf()

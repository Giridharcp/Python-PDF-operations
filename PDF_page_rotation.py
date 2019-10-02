import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from appJar import gui
from pathlib import Path

def PDF_rotation():
   def rotation(input_file,output_file,rotate):
                 pdf_in = open(input_file, 'rb')
                 pdf_reader = PyPDF2.PdfFileReader(pdf_in)
                 pdf_writer = PyPDF2.PdfFileWriter()
   
                 for pagenum in range(pdf_reader.numPages):
                               page = pdf_reader.getPage(pagenum)
                               page.rotateClockwise(rotate)
                               pdf_writer.addPage(page)
   
                 pdf_out = open(output_file, 'wb')
                 pdf_writer.write(pdf_out)
                 pdf_out.close()
                 pdf_in.close()
                 if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
                         app.stop()
   def validate_inputs(src_file,rotate, dest_dir, out_file):
   
        errors = False
        error_msgs = []
        rotate_dir=0
        rotate_value=0
        if Path(src_file).suffix.upper() != ".PDF":
           errors = True
           error_msgs.append("Please select a PDF input file")
           
        test_list=["1", "2", "3", "LEFT", "RIGHT",'']
        for i in test_list: 
            if(i ==rotate) : 
                rotate_dir=i.upper()
        if rotate_dir==0:
             app.infoBox("Invalid Input","Enter a valid Direction to rotate")
        else:
             if (rotate_dir=="LEFT")or(rotate_dir=='1'):
                 rotate_value=90
             elif (rotate_dir=="REVERSE")or(rotate_dir=='2'):
                 rotate_value=180
             elif (rotate_dir=="RIGHT")or(rotate_dir=='3'):
                 rotate_value=270
        if rotate_value==0:
           errors = True
           
           error_msgs.append("Please Select a valid output directory")
        if not(Path(dest_dir)).exists():
           errors = True
           error_msgs.append("Please Select a valid output directory")
   
       # Check for a file name
        if len(out_file) <=0:
           errors = True
           error_msgs.append("Please enter a file name")
       
        return(errors, error_msgs,rotate_value)  
   
   
   def press(button):
       if button=="Process":
           input_file = app.getEntry("Input_File")
           rotate=app.getEntry("rotate_dir")
           output_dir = app.getEntry("Output_Directory")
           output_name = app.getEntry("Output_name")
           
           errors, error_msg,rotate_value = validate_inputs(input_file, rotate, output_dir, output_name)
           if errors:
               app.errorBox("Error", "\n".join(error_msg), parent=None)
           else:
              rotation(input_file,Path(output_dir,output_name),rotate_value)
       else:
           app.stop()
   
   app=gui("PDF Rotationi", useTtk=True)
   app.setTtkTheme('alt')
   app.setSize(500, 200)
   
   # Add the interactive components
   app.addLabel("Choose Source PDF File to Rotate")
   app.addFileEntry("Input_File")
   
   app.addLabel("Enter the numerical value of direction to Rotate 1-Left. 2-Reverse. 3-Right")
   app.addEntry("rotate_dir")
   
   app.addLabel("Select Output Directory")
   app.addDirectoryEntry("Output_Directory")
   
   app.addLabel("Output file name")
   app.addEntry("Output_name")
   
   app.addButtons(["Process", "Quit"],press)
   app.go()


PDF_rotation()

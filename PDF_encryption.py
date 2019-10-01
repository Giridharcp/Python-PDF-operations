import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from appJar import gui
from pathlib import Path

def PDF_encryption():
    def encrypt(input_file,password,out_file):
        output=PdfFileWriter()
        input_pdf=PdfFileReader(open(input_file,"rb"))
        output_file=open(out_file,"wb")

      
        # Create reader and writer object
        pdfReader = PyPDF2.PdfFileReader(input_file)
        pdfWriter = PyPDF2.PdfFileWriter()
        # Add all pages to writer (accepted answer results into blank pages)
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        # Encrypt with your password
        pdfWriter.encrypt(password)
        # Write it to an output file. (you can delete unencrypted version now)
        resultPdf = open(out_file, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
            app.stop()



    def validate_inputs(src_file, dest_dir,password, out_file):

         errors = False
         error_msgs = []
         if Path(src_file).suffix.upper() != ".PDF":
            errors = True
            error_msgs.append("Please select a PDF input file")
            
         if not(Path(dest_dir)).exists():
            errors = True
            error_msgs.append("Please Select a valid output directory")

        # Check for a file name
         if len(out_file) < 1:
            errors = True
            error_msgs.append("Please enter a file name")
            
         if len(password) < 1:
            errors = True
            error_msgs.append("Please enter the password")
        
         return(errors, error_msgs)  

    def press(button):
        if button=="Process":
            src_file = app.getEntry("Input_File")
            dest_dir = app.getEntry("Output_Directory")
            out_file = app.getEntry("Output_name")
            password = app.getEntry("password")
            errors, error_msg = validate_inputs(src_file, dest_dir,password, out_file)
            if errors:
                app.errorBox("Error", "\n".join(error_msg), parent=None)
            else:
               encrypt(src_file,password,Path(dest_dir,out_file))
        else:
            app.stop()




            
    app=gui("PDF Password Encryption", useTtk=True)
    app.setTtkTheme('alt')
    app.setSize(500, 200)

    # Add the interactive components
    app.addLabel("Choose Source PDF File to Encrypt")
    app.addFileEntry("Input_File")

    app.addLabel("Enter the Password:")
    app.addSecretEntry("password")


    app.addLabel("Select Output Directory")
    app.addDirectoryEntry("Output_Directory")

    app.addLabel("Output file name")
    app.addEntry("Output_name")

    app.addButtons(["Process", "Quit"],press)
    
    app.go()


PDF_encryption()

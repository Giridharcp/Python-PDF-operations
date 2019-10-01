# Decrypt password-protected PDF in Python.
# 
# Requirements:
# pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter
from appJar import gui
from pathlib import Path

def PDF_decryption():


  def decrypt_pdf(input_path,password, output_path):
    with open(input_path, 'rb') as input_file, \
      open(output_path, 'wb') as output_file:
      reader = PdfFileReader(input_file)
      reader.decrypt(password)

      writer = PdfFileWriter()

      for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))

      writer.write(output_file)
      if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
          app.stop()
  ##if __name__ == '__main__':
  ##  # example usage:
  ##  decrypt_pdf(r'C:\Users\Giridhar\Desktop\Python FCUK\Encrypted.pdf', 'decrypted.pdf', 'password')
  ##


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
             decrypt_pdf(src_file,password,Path(dest_dir,out_file))
      else:
          app.stop()

          
  app=gui("PDF Password Decryption", useTtk=True)
  app.setTtkTheme('alt')
  app.setSize(500, 200)

  # Add the interactive components
  app.addLabel("Choose Source PDF File to Decrypt")
  app.addFileEntry("Input_File")

  app.addLabel("Enter the Password:")
  app.addSecretEntry("password")


  app.addLabel("Select Output Directory")
  app.addDirectoryEntry("Output_Directory")

  app.addLabel("Output file name")
  app.addEntry("Output_name")

  app.addButtons(["Process", "Quit"],press)
  app.go()
PDF_decryption()

from appJar import gui
from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path


def PDF_delete():

    def delete_pages(input_file,page_range,out_file):
        page_ranges = (x.split("-") for x in page_range.split(","))
        range_list = [i for r in page_ranges for i in range(int(r[0]), int(r[-1]) + 1)]
    #pages_to_delete = [1-20] # page numbering starts from 0
        

        infile = PdfFileReader(input_file)
        output = PdfFileWriter()

        for i in range(infile.getNumPages()):
            try:
                if i not in range_list:
                    p = infile.getPage(i)
                    output.addPage(p)
            except IndexError:
                app.infoBox("Info", "Range exceeded number of pages in input.\nFile will still be saved.")
                    # Alert the user and stop adding pages
                break
        output_dest=str(out_file)
        with open(output_dest, 'wb') as f:
            output.write(f)
        if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
            app.stop()
    def validate_inputs(input_file, output_dir, range, file_name):
        errors = False
        error_msgs = []

        # Make sure a PDF is selected
        if Path(input_file).suffix.upper() != ".PDF":
            errors = True
            error_msgs.append("Please select a PDF input file")

        # Make sure a range is selected
        if len(range) < 1:
            errors = True
            error_msgs.append("Please enter a valid page range")

        # Check for a valid directory
        if not(Path(output_dir)).exists():
            errors = True
            error_msgs.append("Please Select a valid output directory")

        # Check for a file name
        if len(file_name) < 1:
            errors = True
            error_msgs.append("Please enter a file name")

        return(errors, error_msgs)


    def press(button):
     if button == "Process":
            src_file = app.getEntry("Input_File")
            dest_dir = app.getEntry("Output_Directory")
            page_range = app.getEntry("Page_Ranges")
            out_file = app.getEntry("Output_name")
            errors, error_msg = validate_inputs(src_file, dest_dir, page_range, out_file)
            if errors:
                app.errorBox("Error", "\n".join(error_msg), parent=None)
            else:
                delete_pages(src_file, page_range, Path(dest_dir, out_file))
     else:
         app.stop()





    app = gui("PDF Delete selected Pagese", useTtk=True)
    app.setTtkTheme("alt")
    app.setSize(500, 200)

    # Add the interactive components
    app.addLabel("Choose Source PDF File")
    app.addFileEntry("Input_File")

    app.addLabel("Select Output Directory")
    app.addDirectoryEntry("Output_Directory")

    app.addLabel("Output file name")
    app.addEntry("Output_name")

    app.addLabel("Page Ranges: 1,3,4-10")
    app.addEntry("Page_Ranges")

    # link the buttons to the function called press
    app.addButtons(["Process", "Quit"], press)

    # start the GUI
    app.go()
PDF_delete()

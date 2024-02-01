To make it work you need to have the imports in the beginning of your document. That will define the command to get a sertain column from your exel file. Use \getValue{Exelcolums name} with in the document to get it. The exel file must be in the same folder as the latex documents files. 

To build the document you have to do it using the usercommand or else the exelvalues would not be updated.
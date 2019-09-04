
# Publishing MARS Forms and IMSMA Field report GUID.
Once IMSMA NG published a form it assign a GUID value to that form to link the reports, with the correct version of form. Hence when connecting any reports to an IMSMA form you will need to include the GUID to identify the correct published form and link it to the reports. 

MARS uses the published form GUID when building the MaXML file to link the reports with the desired form in IMSMA NG. To accomplish this here are the recommended steps that MARS Organisation Administrators can follows.

## Export MaXML
IMSMA NG creates a new report following the preferred method. In this example I will use the Data Entry menu item as a way to create a new report. 
* On the Main Menu in IMSMA Click on `Date Entry` and select `Data Entry Forms`.
* Select `Add Data Entry Forms...` 
* IMSMA will show you a list of the data entry form templates.
* Select the desired template and click `Ok` or double click.
* The Data Entry Form Editor will open.
* Fill some data and click on `Save` 
* Close the Date Entry Form Editor and open `Workbench`
* In `Workbench` select the new form you just saved and click on `Export` icon

* In the `Export Options` make sure that the `XML Export` selected and click `Ok`
* Select the folder you want to save the file and fill the file name in `File Name` field.
* Click on `Save`
	![][image-1]
## Getting the IMSMA Field Report GUID
Once you have the `MaXML` file in your computer, open it using your favourite editor, here I will use the notepad++.
* From the main menu click on `File` and select `Open...`
* Find the folder that contain he `MaXML` file and select it.
* Click ok.
* Click on `'Ctrl'+'f'` to open the Find dialog.
* Type `reportGUID` and click `Find Next`
* The FieldReportInfo element has the following structure
		<FieldReportInfo 
			reportGUID="c0a8-016e-158248f3321-b08c2538-4-bc80," 
			reportID="DEF-1831" 
			fieldReportGUID="c0a8-8e7f-16cf2236466-35d67078-1-42bc"
		>
* What we are looking for is the `reportGUID` that contain the GUID of the report from IMSMA.
* Don’t be confused with the `fieldReportGUID` which is unique to each Report
*  Copy that part value between the double quote, in this example that will be `c0a8-016e-158248f3321-b08c2538-4-bc80`

## Linking the MARS Form with the IMSMA NG Form.
* In MARS open select `Forms`
* If you did not create a form, create one. 
* Fill `IMSMA Report GUID` using the value we got from the `reportGUID`. 
* In case you have the form already exists, open it and click on `properties`
* Fill the value we have it copied.
this will conclude this process, and if you have any issue contact GICHD for support.

[image-1]:	./images/ExportMaXML.png
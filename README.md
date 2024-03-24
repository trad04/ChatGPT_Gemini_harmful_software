# ChatGPT_Gemini_harmful_software

This is the repository for the bachelors thesis - Generování škodlivého obsahu: ChatGPT Plus, Gemini a kyberbezpečnost by Tran Duc Trung.

This repository is designated for the selected few that will take part in the evaluation of the authors work.

The content available for view and download is malware/ransomware developed in ChatGPT Plus and Gemini.

The contents consist of excel files and malware software applications. Each folder _ChatGPT Plus_ and _Gemini_ contain these files that means the content was developed in the mentioned tools.

## Disclaimer 

Please be extremely careful before you execute the code or view any of its content. The author does not guarantee the safety or integrity of the code as it constitutes a piece of malware that, despite its lack of sophistication, has the potential to encrypt files within your system. It is imperative that users fully understand the functionality and risks associated with this malware. Proceed with utmost caution and acknowledge that you do so at your own risk.

## Functionality

Excel file via VBA macro upon opening executes the malware python .exe application.

This .exe file searches for every PDF file in your system. 
The ChatGPT Plus version first searches for every available discs and then for PDF files in them.
Whereas Gemini version searches from root.

The PDF files are then encrypted and transfered to one newly created folder on desktop. 
Additionaly a ransom note in txt file is created in this folder.

The execution of the malware is not shown and the user should be able to know that it even was executed or being ran in the background.

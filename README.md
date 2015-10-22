# 521_FinalProject
lateral flow image processor

#Brainstorm 
Draft Title: Lateral Flow Assay Image Processor            
The purpose of our project is to develop an image processor that will provide automatic readings of lateral flow assays. Lateral flow assays are great for providing point-of-care diagnostics, but the results are traditionally determined by eye, which make them reader subjective. Creating a lateral flow assay image processor that could automatically read these assays will make the results more reliable, allow for better comparisons amongst tests, and overall increase the ease-of-use of lateral flow assays in clinical settings. We hope to achieve our goal by first making a device that can take an image of a lateral flow assay. In this case, we will be concentrating on analyzing a test specific for detecting mutant vs wild type HIV DNA. We will then work on using image processing filters to increase the contrast of the image. We will then use recognition software to locate the area of the assay we want to analyze and then see if a colored dot can be detected. The contrast enhanced image as well as the final result (“mutant positive,” “wild type positive,” or “negative”) will then be output to the screen. 

Further Development Possibilities 
- Create a user-friendly interface using icons that allow the program to be run with a push of a button 
- Telemedicine: Create a way for information to be transmitted wirelessly to a main computer as well as attach pertinent medical information to the image (Patient ID, date, locations, etc) 
- Further develop the code to not only recognize the presence of a dot but also be able to distinguish between relative intensities. For example, “positive” dots are usually darker if the person has a higher viral load. Being able to distinguish between low and high viral loads could then be used when deciding treatment. 

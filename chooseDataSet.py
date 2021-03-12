import pandas as pd

'''
Find benign samples that in some way correspond to malignant.
'''

def loadData(inputFile):
    data = pd.read_csv(inputFile, 
                        sep=",", 
                        header=1, 
                        low_memory=False,
                        names=[
                        "_id",
                        "name",
                        "meta_clinical_age_approx",
                        "meta_clinical_anatom_site_general",
                        "meta_clinical_benign_malignant",
                        "meta_clinical_clin_size_long_diam_mm",
                        "meta_clinical_diagnosis",
                        "meta_clinical_diagnosis_confirm_type",
                        "meta_clinical_family_hx_mm",
                        "meta_clinical_lesion_id",
                        "meta_clinical_mel_class",
                        "meta_clinical_mel_mitotic_index",
                        "meta_clinical_mel_thick_mm",
                        "meta_clinical_mel_type",
                        "meta_clinical_mel_ulcer",
                        "meta_clinical_melanocytic",
                        "meta_clinical_nevus_type",
                        "meta_clinical_patient_id",
                        "meta_clinical_personal_hx_mm",
                        "meta_clinical_sex",
                        "meta_acquisition_acquisition_day",
                        "meta_acquisition_blurry",
                        "meta_acquisition_color_tint",
                        "meta_acquisition_dermoscopic_type",
                        "meta_acquisition_hairy",
                        "meta_acquisition_image_type",
                        "meta_acquisition_marker_pen",
                        "meta_acquisition_pixelsX",
                        "meta_acquisition_pixelsY"
                        ])

    malignant = data.query("meta_clinical_benign_malignant == ['malignant']")
    benign = data.query("meta_clinical_benign_malignant == ['benign']")
    
    return data, benign, malignant

inputFile = "ISIC_metadata.csv"
outputFile = "melanoma_dataSet.csv"

data, benign, malignant = loadData(inputFile)
# Use all malignant samples
dataSet = malignant.copy()

# Run through possible values of the anatom_site column
for site in malignant['meta_clinical_anatom_site_general'].unique():
    if not isinstance(site, float):
        numberOfRowsToAdd = malignant.query(
            "meta_clinical_anatom_site_general == ['" + site + "']").count()[0]
        
        addedRows = 0
        sizeOfFrameStart = dataSet.shape[0]
        newSample = benign.query(
            "meta_clinical_anatom_site_general == ['" + site + "']").sample\
                (n=numberOfRowsToAdd, random_state=443)
        dataSet = dataSet.append(newSample)
        
        addedRows += (dataSet.shape[0] - sizeOfFrameStart)
        print(site, "# to add:", numberOfRowsToAdd, "# did add:",addedRows)
        if numberOfRowsToAdd != addedRows:
            print("Error, will exit")
            exit()
    else:
        # If "None", i.e. no value for this attribute
        numberOfRowsToAdd = malignant.query(
            "meta_clinical_anatom_site_general.isnull()").count()[0]
        addedRows = 0
    
        sizeOfFrameStart = dataSet.shape[0]
        newSample = benign.query(
            "meta_clinical_anatom_site_general.isnull()"
            ).sample(n=numberOfRowsToAdd, random_state=443)
        dataSet = dataSet.append(newSample)
        
        addedRows += (dataSet.shape[0] - sizeOfFrameStart)
        print(site, "# to add:", numberOfRowsToAdd, "# did add:",addedRows)
        if numberOfRowsToAdd != addedRows:
            print("Error, will exit")
            exit()
        
print("\n",dataSet.shape)

dataSet.to_csv(outputFile, sep=',', columns=["_id","name","meta_clinical_age_approx","meta_clinical_anatom_site_general","meta_clinical_benign_malignant","meta_clinical_lesion_id","meta_clinical_patient_id","meta_clinical_sex","meta_acquisition_pixelsX","meta_acquisition_pixelsY"], index=False)
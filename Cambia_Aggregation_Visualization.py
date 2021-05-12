# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:03:45 2021

@author: 15403
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read in FL vaccine hesitancy data retrieved from data.cdc.gov
vaccine_hesitancy_df = pd.read_csv('Florida_Vaccine_Hesitancy.csv')

vaccine_hesitancy_df.rename(columns={'Estimated hesitant': 'COVID vaccine hesitancy'}, inplace=True)

#read in FL infant death rate data by county retrieved from flhealthcharts.com; skipped title, combined state data, and Alachua county--data not available across all data sets for Alachua county
infant_deaths_df = pd.read_csv('InfantDeathViewer_FLGridData.csv', skiprows= [0, 2, 3], usecols = (0,3))

infant_deaths_df.rename(columns={'Rate': 'Infant death rate'}, inplace=True)

#read in FL 7th grade immunization compliance data by county retrieved from flhealthcharts.com; skipped title, combined state data, and Alachua county--data not available across all data sets for Alachua county
immunizations_7th_grade_counties = pd.read_csv('Immunizations7thGrade.csv', skiprows= [0, 2, 3], usecols = (0, 3))

immunizations_7th_grade_counties.rename(columns= {'Percent (%)': 'Immunization completion'}, inplace=True)

#read in FL varicella rates by county retrieved from flhealthcharts.com; skipped title, combined state data, and Alachua county--data not available across all data sets for Alachua county
varicella_rates_counties = pd.read_csv('Varicella_Rates_FL.csv', skiprows= [0, 2, 3], usecols = (0, 3))

varicella_rates_counties.rename(columns={'Rate': 'Rate of Varicella'}, inplace=True)

#create DataFrame of data to be used for correlations
searching_correlations = [varicella_rates_counties['Rate of Varicella'], immunizations_7th_grade_counties['Immunization completion'], vaccine_hesitancy_df['COVID vaccine hesitancy'], infant_deaths_df['Infant death rate']]

#create DataFrame for correlation matrix
cor= pd.DataFrame(searching_correlations)
cor_df = cor.T
corrMatrix = cor_df.corr()

#heatmap of correlations
sns.heatmap(corrMatrix, annot=True)
sns.color_palette('mako', as_cmap=True)
plt.title('Health Data Correlations', fontsize=20)
plt.show()






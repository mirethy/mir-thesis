# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy.stats as st
import pandas as pd
import statsmodels.formula.api as stat
import matplotlib.pyplot as plt
import pandas
from scipy.stats import mstats
from scipy import stats
import statistics
import scipy
from scipy.stats import ranksums
from scipy.stats import wilcoxon

#uploading data
data_proc_file=pd.read_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Data/procdata_treat.csv", delimiter=(";"))
data_list=pd.read_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Data_Input.csv", delimiter=(";"))
table_bis11=pd.read_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Data/table_BIS11.csv", delimiter=(";"))
negin_participants=pd.read_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Negin_Participants.csv", delimiter=(","))
participants_excell=pd.read_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Participants_Treatment_Calc.csv", delimiter=(";"))

#note in my dataset ip=treatment; submitted= choice in combined_dataset
negin_participants=negin_participants.drop_duplicates('subject')
negin_participants = negin_participants[negin_participants['ip'].notna()]
negin_participants.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/negin_participants.csv")

for i in range (1,19):
    dataname = "/Users/neginjavaheri/Desktop/UVA/Thesis/Data/" + str(i)+".csv"
    globals()[f'mytable{i}']=pd.read_csv(dataname, delimiter=(","))
    if i == 1:
        ALL_base = globals()[f'mytable{i}']
    else:
        ALL_base = ALL_base.append(globals()[f'mytable{i}'])


combined_table=data_proc_file.merge(data_list,how="left",left_on="subject", right_on="row_col")
unproc_data=ALL_base.merge(negin_participants,how="left",left_on="subject", right_on="subject")
unproc_data = unproc_data[unproc_data['time'] > 200]
unproc_data_subset = unproc_data[["name","ip_y","subject", "expname","choice","event","ip_x"]]
unproc_data_new= unproc_data_subset[unproc_data_subset["event"].isin(["mouseover", "btnClick"]) ]


#(group_percent[["submitted"]]).to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/sub_data.csv")

#
#creating regression for percentage , treatment groups and submitted answer

combined_table["percentage_new"]=combined_table["Percentage"].str.strip("%").astype(int)
combined_table["ip_new"]=combined_table["ip"].astype(str)


##first regressions
my_regression1=stat.ols(formula="submitted ~ ip_new ",data=combined_table).fit() 
print(my_regression1.summary())
my_regression=stat.ols(formula="submitted ~ percentage_new + ip_new ",data=combined_table).fit() 
print(my_regression.summary())
#average choices
mean_choice_total=statistics.mean(combined_table["submitted"])
print(mean_choice_total)

Ip0_total= combined_table[combined_table["ip_new"]=="0"]
Submittedip0_total = Ip0_total["submitted"]
mean_choice_ip0_total=statistics.mean(Ip0_total["submitted"])
print(mean_choice_ip0_total)

Ip1_total= combined_table[combined_table["ip_new"]=="1"]
Submittedip1_total = Ip1_total["submitted"]
mean_choice_ip1_total=statistics.mean(Ip1_total["submitted"])
print(mean_choice_ip1_total)

Ip2_total= combined_table[combined_table["ip_new"]=="2"]
Submittedip2_total = Ip2_total["submitted"]
mean_choice_ip2_total=statistics.mean(Ip2_total["submitted"])
print(mean_choice_ip2_total)

#calulated CI of 95% level
ci_all_ipo0=st.norm.interval(alpha=0.95, loc=np.mean(Submittedip0_total), scale=st.sem(Submittedip0_total))
print(ci_all_ipo0)
ci_all_ip1=st.norm.interval(alpha=0.95, loc=np.mean(Submittedip1_total), scale=st.sem(Submittedip1_total))
print(ci_all_ip1)
ci_all_ipo2=st.norm.interval(alpha=0.95, loc=np.mean(Submittedip2_total), scale=st.sem(Submittedip2_total))
print(ci_all_ipo2)

#calculate SD
sd_all_ipo0=statistics.stdev(Submittedip0_total)
print(sd_all_ipo0)

sd_all_ipo1=statistics.stdev(Submittedip1_total)
print(sd_all_ipo1)

sd_all_ipo2=statistics.stdev(Submittedip2_total)
print(sd_all_ipo2)

#KW-test on submitted choices total
H, pval =stats.kruskal(Submittedip0_total,Submittedip1_total,Submittedip2_total)

print("H-statistic:", H) ##h statistics is 2.9242634481209424
print("P-Value:", pval) ##p-value is 0.23174173837000625 when looking at 3 treatment groups. when comparing t1 with t2 p-value is 0.17410351997550277 (20-50% discounting).

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
    
##creating dataset with percentage difference of more than 10 percent in amount option

combined_table_subset = combined_table.loc[(combined_table['percentage_new'] >=15) & (combined_table['percentage_new'] <= 50)]

combined_table.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/combined_table.csv")
combined_table_subset.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/combined_table_subset.csv")
Ip0_total.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Ip0_total.csv")
Ip1_total.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Ip1_total.csv")
Ip2_total.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/Ip2_total.csv")


mean_choice=statistics.mean(combined_table_subset["submitted"])
print(mean_choice)



Ip0= combined_table_subset[combined_table_subset["ip_new"]=="0"]

Submittedip0 = Ip0["submitted"]

mean_choice_ip0=statistics.mean(Ip0["submitted"])
print(mean_choice_ip0)

Ip1= combined_table_subset[combined_table_subset["ip_new"]=="1"]

Submittedip1 = Ip1["submitted"]

mean_choice_ip1=statistics.mean(Ip1["submitted"])
print(mean_choice_ip1)

Ip2= combined_table_subset[combined_table_subset["ip_new"]=="2"]

Submittedip2 = Ip2["submitted"]

mean_choice_ip2=statistics.mean(Ip2["submitted"])
print(mean_choice_ip2)

#calculate SD
sd_sub_ipo0=statistics.stdev(Ip0["submitted"])
print(sd_sub_ipo0)

sd_sub_ipo1=statistics.stdev(Ip1["submitted"])
print(sd_sub_ipo1)

sd_sub_ipo2=statistics.stdev(Ip2["submitted"])
print(sd_sub_ipo2)

#calculate KW-test
H, pval =stats.kruskal(Submittedip0,Submittedip1,Submittedip2)

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")



## creating combined table with soon-time being today
combined_table_soon_time=combined_table[combined_table["Soon_Time"]=="0 weeks"]
combined_table_subset_soon_time=combined_table_subset[combined_table_subset["Soon_Time"]=="0 weeks"]
combined_table_later_time=combined_table[combined_table["Soon_Time"]=="2 weeks"]
combined_table_subset_later_time=combined_table_subset[combined_table_subset["Soon_Time"]=="2 weeks"]

combined_table_soon_time = combined_table_soon_time.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_soon_time = combined_table_subset_soon_time.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_later_time = combined_table_later_time.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_later_time = combined_table_subset_later_time.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)

my_regression_sub_time=stat.ols(formula="submitted ~ ip_new + percentage_new",data=combined_table_subset).fit() 
print(my_regression_sub_time.summary())

## in order to analyze a complete OLS for all choices and

##analyzing the different tables; looking at treatment effects

my_regression_soon_time=stat.ols(formula="submitted ~ Treatment + Percentage_Difference",data=combined_table_soon_time).fit() 
print(my_regression_soon_time.summary())

my_regression_soon_time_subset=stat.ols(formula="submitted ~  Treatment + Percentage_Difference",data=combined_table_subset_soon_time).fit() 
print(my_regression_soon_time_subset.summary())

my_regression_later_time=stat.ols(formula="submitted ~ Treatment + Percentage_Difference ",data=combined_table_later_time).fit() 
print(my_regression_later_time.summary())

my_regression_later_time_subset=stat.ols(formula="submitted ~ Treatment + Percentage_Difference ",data=combined_table_subset_later_time).fit() 
print(my_regression_later_time_subset.summary())

##combined_table_soon_time


combined_table_soon_time_all = combined_table_soon_time[["Treatment", "submitted"]]

combined_table_soon_time_ip0=combined_table_soon_time_all[combined_table_soon_time_all["Treatment"]=="0"]
combined_table_soon_time_ip1=combined_table_soon_time_all[combined_table_soon_time_all["Treatment"]=="1"]
combined_table_soon_time_ip2=combined_table_soon_time_all[combined_table_soon_time_all["Treatment"]=="2"]

combined_table_soon_time_sub_ip0=combined_table_soon_time_ip0['submitted']
combined_table_soon_time_sub_ip1=combined_table_soon_time_ip1['submitted']
combined_table_soon_time_sub_ip2=combined_table_soon_time_ip2['submitted']



H, pval =stats.kruskal(combined_table_soon_time_sub_ip0,combined_table_soon_time_sub_ip1,combined_table_soon_time_sub_ip2)

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(combined_table_soon_time_sub_ip0,combined_table_soon_time_sub_ip1)
ranksums(combined_table_soon_time_sub_ip1,combined_table_soon_time_sub_ip2)
ranksums(combined_table_soon_time_sub_ip0,combined_table_soon_time_sub_ip2)

#calculate mean  and SD of treatment

mean_choice_soon_ip0=statistics.mean(combined_table_soon_time_sub_ip0)
print(mean_choice_soon_ip0)


mean_choice_soon_ip1=statistics.mean(combined_table_soon_time_sub_ip1)
print(mean_choice_soon_ip1)


mean_choice_soon_ip2=statistics.mean(combined_table_soon_time_sub_ip2)
print(mean_choice_soon_ip2)

#calculate SD
sd_soon_ipo0=statistics.stdev(combined_table_soon_time_sub_ip0)
print(sd_soon_ipo0)

sd_soon_ipo1=statistics.stdev(combined_table_soon_time_sub_ip1)
print(sd_soon_ipo1)

sd_soon_ip2=statistics.stdev(combined_table_soon_time_sub_ip2)
print(sd_soon_ip2)

##combined_table_subset_soon_time

combined_table_subset_soon_time_all = combined_table_subset_soon_time[["Treatment", "submitted"]]

combined_table_subset_soon_time_ip0=combined_table_subset_soon_time_all[combined_table_subset_soon_time_all["Treatment"]=="0"]
combined_table_subset_soon_time_ip1=combined_table_subset_soon_time_all[combined_table_subset_soon_time_all["Treatment"]=="1"]
combined_table_subset_soon_time_ip2=combined_table_subset_soon_time_all[combined_table_subset_soon_time_all["Treatment"]=="2"]

combined_table_subset_soon_time_ip0=combined_table_subset_soon_time_ip0['submitted']
combined_table_subset_soon_time_ip1=combined_table_subset_soon_time_ip1['submitted']
combined_table_subset_soon_time_ip2=combined_table_subset_soon_time_ip2['submitted']

H, pval =stats.kruskal(combined_table_subset_soon_time_ip0,combined_table_subset_soon_time_ip1,combined_table_subset_soon_time_ip2)

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#calculate mean  and SD of treatment

mean_choice_sub_soon_ip0=statistics.mean(combined_table_subset_soon_time_ip0)
print(mean_choice_sub_soon_ip0)

mean_choice_sub_soon_ip1=statistics.mean(combined_table_subset_soon_time_ip1)
print(mean_choice_sub_soon_ip1)

mean_choice_sub_soon_ip2=statistics.mean(combined_table_subset_soon_time_ip2)
print(mean_choice_sub_soon_ip2)

#calculate SD
sd_sub_soon_ip0=statistics.stdev(combined_table_subset_soon_time_ip0)
print(sd_sub_soon_ip0)

sd_sub_soon_ip1=statistics.stdev(combined_table_subset_soon_time_ip1)
print(sd_sub_soon_ip1)

sd_sub_soon_ip2=statistics.stdev(combined_table_subset_soon_time_ip2)
print(sd_sub_soon_ip2)

##combined_table_later_time

combined_table_later_time_all = combined_table_later_time[["Treatment", "submitted"]]

combined_table_later_time_ip0=combined_table_later_time_all[combined_table_later_time_all["Treatment"]=="0"]
combined_table_later_time_ip1=combined_table_later_time_all[combined_table_later_time_all["Treatment"]=="1"]
combined_table_later_time_ip2=combined_table_later_time_all[combined_table_later_time_all["Treatment"]=="2"]

combined_table_later_time_ip0=combined_table_later_time_ip0['submitted']
combined_table_later_time_ip1=combined_table_later_time_ip1['submitted']
combined_table_later_time_ip2=combined_table_later_time_ip2['submitted']

H, pval =stats.kruskal(combined_table_later_time_ip0, combined_table_later_time_ip1, combined_table_later_time_ip2)

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


#calculate mean  and SD of treatment

mean_choice_late_ip0=statistics.mean(combined_table_later_time_ip0)
print(mean_choice_late_ip0)


mean_choice_late_ip1=statistics.mean(combined_table_later_time_ip1)
print(mean_choice_late_ip1)


mean_choice_late_ip2=statistics.mean(combined_table_later_time_ip2)
print(mean_choice_late_ip2)

#calculate SD
sd_late_ip0=statistics.stdev(combined_table_later_time_ip0)
print(sd_late_ip0)

sd_late_ip1=statistics.stdev(combined_table_later_time_ip1)
print(sd_late_ip1)

sd_late_ip2=statistics.stdev(combined_table_later_time_ip2)
print(sd_late_ip2)

##combined_table_subset_later_time


combined_table_subset_later_time_all = combined_table_subset_later_time[["Treatment", "submitted"]]

combined_table_subset_later_time_ip0=combined_table_subset_later_time_all[combined_table_subset_later_time_all["Treatment"]=="0"]
combined_table_subset_later_time_ip1=combined_table_subset_later_time_all[combined_table_subset_later_time_all["Treatment"]=="1"]
combined_table_subset_later_time_ip2=combined_table_subset_later_time_all[combined_table_subset_later_time_all["Treatment"]=="2"]

combined_table_subset_later_time_ip0=combined_table_subset_later_time_ip0['submitted']
combined_table_subset_later_time_ip1=combined_table_subset_later_time_ip1['submitted']
combined_table_subset_later_time_ip2=combined_table_subset_later_time_ip2['submitted']

H, pval =stats.kruskal(combined_table_subset_later_time_ip0,combined_table_subset_later_time_ip1,combined_table_subset_later_time_ip2)
print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#calculate mean  and SD of treatment

mean_choice_sub_late_ip0=statistics.mean(combined_table_subset_later_time_ip0)
print(mean_choice_sub_late_ip0)


mean_choice_sub_late_ip1=statistics.mean(combined_table_subset_later_time_ip1)
print(mean_choice_sub_late_ip1)


mean_choice_sub_late_ip2=statistics.mean(combined_table_subset_later_time_ip2)
print(mean_choice_sub_late_ip2)

#calculate SD
sd_sub_late_ip0=statistics.stdev(combined_table_subset_later_time_ip0)
print(sd_sub_late_ip0)

sd_sub_late_ip1=statistics.stdev(combined_table_subset_later_time_ip1)
print(sd_sub_late_ip1)

sd_sub_late_ip2=statistics.stdev(combined_table_subset_later_time_ip2)
print(sd_sub_late_ip2)


#creating option index
imm_opt = combined_table["t_box1"] + combined_table["t_box3"]
combined_table["imm_opt"] = imm_opt

imm_opt_mean = statistics.mean(imm_opt)
print(imm_opt_mean) 
 
del_opt = combined_table["t_box2"] + combined_table["t_box4"]
combined_table["del_opt"] = del_opt

del_opt_mean = statistics.mean(del_opt)
print(del_opt_mean) #

opt_index= (imm_opt - del_opt)/(imm_opt + del_opt)
combined_table["opt_index"]=opt_index
mean_opt_index=statistics.mean(opt_index)
print(mean_opt_index)
stdev_opt_index=statistics.stdev(opt_index)
print(stdev_opt_index)

opt_index_treatment = combined_table[["opt_index", "ip"]]

##creating the additional lists for the indexes
combined_table_subset_with_index = combined_table.loc[(combined_table['percentage_new'] >= 15) & (combined_table['percentage_new'] <= 50)]
combined_table_soon_time_index=combined_table[combined_table["Soon_Time"]=="0 weeks"]
combined_table_subset_soon_time_index=combined_table_subset_with_index[combined_table_subset_with_index["Soon_Time"]=="0 weeks"]
combined_table_later_time_index=combined_table[combined_table["Soon_Time"]=="2 weeks"]
combined_table_subset_later_time_index=combined_table_subset_with_index[combined_table_subset_with_index["Soon_Time"]=="2 weeks"]

combined_table_soon_time_index = combined_table_soon_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_soon_time_index = combined_table_subset_soon_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_later_time_index = combined_table_later_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_later_time_index = combined_table_subset_later_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)


combined_table_opt_ip0=opt_index_treatment[opt_index_treatment["ip"]==0]
combined_table_opt_ip1=opt_index_treatment[opt_index_treatment["ip"]==1]
combined_table_opt_ip2=opt_index_treatment[opt_index_treatment["ip"]==2]

opt_ip0=combined_table_opt_ip0["opt_index"]
opt_ip1=combined_table_opt_ip1["opt_index"]
opt_ip2=combined_table_opt_ip2["opt_index"]


##KW-Test
H, pval =stats.kruskal(combined_table_opt_ip0["opt_index"], combined_table_opt_ip1["opt_index"],combined_table_opt_ip2["opt_index"])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(combined_table_opt_ip0["opt_index"],combined_table_opt_ip1["opt_index"])
ranksums(combined_table_opt_ip1["opt_index"],combined_table_opt_ip2["opt_index"])
ranksums(combined_table_opt_ip0["opt_index"],combined_table_opt_ip2["opt_index"])
#Calculate Mean and SD
combined_table_opt_mean_ip0=statistics.mean(opt_ip0)
print(combined_table_opt_mean_ip0)
combined_table_opt_mean_ip1=statistics.mean(opt_ip1)
print(combined_table_opt_mean_ip1)
combined_table_opt_mean_ip2=statistics.mean(opt_ip2)
print(combined_table_opt_mean_ip2)

#calculate SD
combined_table_opt_sd_ip0=statistics.stdev(opt_ip0)
print(combined_table_opt_sd_ip0)

combined_table_opt_sd_ip1=statistics.stdev(opt_ip1)
print(combined_table_opt_sd_ip1)

combined_table_opt_sd_ip2=statistics.stdev(opt_ip2)
print(combined_table_opt_sd_ip2)

##krusal-test with subset of data

combined_table_subset_with_index = combined_table.loc[(combined_table['percentage_new'] >= 15) & (combined_table['percentage_new'] <= 50)]

opt_index_treatment_subset = combined_table_subset_with_index[["opt_index", "ip"]]

subset_table_opt_ip0=opt_index_treatment_subset[opt_index_treatment_subset["ip"]==0]
subset_table_opt_ip1=opt_index_treatment_subset[opt_index_treatment_subset["ip"]==1]
subset_table_opt_ip2=opt_index_treatment_subset[opt_index_treatment_subset["ip"]==2]

H, pval =stats.kruskal(subset_table_opt_ip0['opt_index'], subset_table_opt_ip1['opt_index'], 
                       subset_table_opt_ip2['opt_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#Calculate Mean and SD
opt_sub_ip0=subset_table_opt_ip0["opt_index"]
opt_sub_ip1=subset_table_opt_ip1["opt_index"]
opt_sub_ip2=subset_table_opt_ip2["opt_index"]

opt_sub_mean_ip0=statistics.mean(opt_sub_ip0)
print(opt_sub_mean_ip0)
opt_sub_mean_ip1=statistics.mean(opt_sub_ip1)
print(opt_sub_mean_ip1)
opt_sub_mean_ip2=statistics.mean(opt_sub_ip2)
print(opt_sub_mean_ip2)

#calculate SD
opt_sub_sd_ip0=statistics.stdev(opt_sub_ip0)
print(opt_sub_sd_ip0)

opt_sub_sd_ip1=statistics.stdev(opt_sub_ip1)
print(opt_sub_sd_ip1)

opt_sub_sd_ip2=statistics.stdev(opt_sub_ip2)
print(opt_sub_sd_ip2)

##Kruskal-test with subsets as well as time options

##combined_table_soon_time_index

opt_index_treatment_soon_time_index = combined_table_soon_time_index[["opt_index", "ip"]]

table_opt_ip0_soon_time=opt_index_treatment_soon_time_index[opt_index_treatment_soon_time_index["ip"]==0]
table_opt_ip1_soon_time=opt_index_treatment_soon_time_index[opt_index_treatment_soon_time_index["ip"]==1]
table_opt_ip2_soon_time=opt_index_treatment_soon_time_index[opt_index_treatment_soon_time_index["ip"]==2]

H, pval =stats.kruskal(table_opt_ip0_soon_time['opt_index'], table_opt_ip1_soon_time['opt_index'], 
                       table_opt_ip2_soon_time['opt_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(table_opt_ip0_soon_time["opt_index"],table_opt_ip1_soon_time["opt_index"])
ranksums(table_opt_ip1_soon_time["opt_index"],table_opt_ip2_soon_time["opt_index"])
ranksums(table_opt_ip0_soon_time["opt_index"],table_opt_ip2_soon_time["opt_index"])

#Calculate Mean and SD
opt_soon_time_ip0=table_opt_ip0_soon_time["opt_index"]
opt_soon_time_ip1=table_opt_ip1_soon_time["opt_index"]
opt_soon_time_ip2=table_opt_ip2_soon_time["opt_index"]

opt_soon_time_mean_ip0=statistics.mean(opt_soon_time_ip0)
print(opt_soon_time_mean_ip0)
opt_soon_time_mean_ip1=statistics.mean(opt_soon_time_ip1)
print(opt_soon_time_mean_ip1)
opt_soon_time_mean_ip2=statistics.mean(opt_soon_time_ip2)
print(opt_soon_time_mean_ip2)

#calculate SD
opt_soon_time_sd_ip0=statistics.stdev(opt_soon_time_ip0)
print(opt_soon_time_sd_ip0)

opt_soon_time_sd_ip1=statistics.stdev(opt_soon_time_ip1)
print(opt_soon_time_sd_ip1)

opt_soon_time_sd_ip2=statistics.stdev(opt_soon_time_ip2)
print(opt_soon_time_sd_ip2) 
   
##combined_table_subset_soon_time_index

opt_index_treatment_subset_soon_time_index = combined_table_subset_soon_time_index[["opt_index", "ip"]]

subset_table_opt_ip0_soon_time=opt_index_treatment_subset_soon_time_index[opt_index_treatment_subset_soon_time_index["ip"]==0]
subset_table_opt_ip1_soon_time=opt_index_treatment_subset_soon_time_index[opt_index_treatment_subset_soon_time_index["ip"]==1]
subset_table_opt_ip2_soon_time=opt_index_treatment_subset_soon_time_index[opt_index_treatment_subset_soon_time_index["ip"]==2]

H, pval =stats.kruskal(subset_table_opt_ip0_soon_time['opt_index'], subset_table_opt_ip1_soon_time['opt_index'], 
                       subset_table_opt_ip2_soon_time['opt_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
 

#Calculate Mean and SD
opt_sub_soon_time_ip0=subset_table_opt_ip0_soon_time["opt_index"]
opt_sub_soon_time_ip1=subset_table_opt_ip1_soon_time["opt_index"]
opt_sub_soon_time_ip2=subset_table_opt_ip2_soon_time["opt_index"]

opt_sub_soon_time_mean_ip0=statistics.mean(opt_sub_soon_time_ip0)
print(opt_sub_soon_time_mean_ip0)
opt_sub_soon_time_mean_ip1=statistics.mean(opt_sub_soon_time_ip1)
print(opt_sub_soon_time_mean_ip1)
opt_sub_soon_time_mean_ip2=statistics.mean(opt_sub_soon_time_ip2)
print(opt_sub_soon_time_mean_ip2)

#calculate SD
opt_sub_soon_time_sd_ip0=statistics.stdev(opt_sub_soon_time_ip0)
print(opt_sub_soon_time_sd_ip0)

opt_sub_soon_time_sd_ip1=statistics.stdev(opt_sub_soon_time_ip1)
print(opt_sub_soon_time_sd_ip1)

opt_sub_soon_time_sd_ip2=statistics.stdev(opt_sub_soon_time_ip2)
print(opt_sub_soon_time_sd_ip2) 
      
##combined_table_later_time_index


opt_index_treatment_later_index = combined_table_later_time_index[["opt_index", "ip"]]

table_opt_ip0_later_time=opt_index_treatment_later_index[opt_index_treatment_later_index["ip"]==0]
table_opt_ip1_later_time=opt_index_treatment_later_index[opt_index_treatment_later_index["ip"]==1]
table_optr_ip2_later_time=opt_index_treatment_later_index[opt_index_treatment_later_index["ip"]==2]

H, pval =stats.kruskal(table_opt_ip0_later_time['opt_index'], table_opt_ip1_later_time['opt_index'], 
                       table_optr_ip2_later_time['opt_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#Calculate Mean and SD
opt_later_time_ip0=table_opt_ip0_later_time["opt_index"]
opt_later_time_ip1=table_opt_ip1_later_time["opt_index"]
opt_later_time_ip2=table_optr_ip2_later_time["opt_index"]

opt_later_time_mean_ip0=statistics.mean(opt_later_time_ip0)
print(opt_later_time_mean_ip0)
opt_later_time_mean_ip1=statistics.mean(opt_later_time_ip1)
print(opt_later_time_mean_ip1)
opt_later_time_mean_ip2=statistics.mean(opt_later_time_ip2)
print(opt_later_time_mean_ip2)

#calculate SD
opt_later_time_sd_ip0=statistics.stdev(opt_later_time_ip0)
print(opt_later_time_sd_ip0)

opt_later_time_sd_ip1=statistics.stdev(opt_later_time_ip1)
print(opt_later_time_sd_ip1)

opt_later_time_sd_ip2=statistics.stdev(opt_later_time_ip2)
print(opt_later_time_sd_ip2) 



##combined_table_subset_later_time_index

opt_index_treatment_subset_later_time_index = combined_table_subset_later_time_index[["opt_index", "ip"]]

subset_table_opt_ip0_later_time=opt_index_treatment_subset_later_time_index[opt_index_treatment_subset_later_time_index["ip"]==0]
subset_table_opt_ip1_later_time=opt_index_treatment_subset_later_time_index[opt_index_treatment_subset_later_time_index["ip"]==1]
subset_table_opt_ip2_later_time=opt_index_treatment_subset_later_time_index[opt_index_treatment_subset_later_time_index["ip"]==2]

H, pval =stats.kruskal(subset_table_opt_ip0_later_time['opt_index'], subset_table_opt_ip1_later_time['opt_index'], 
                       subset_table_opt_ip2_later_time['opt_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


#Calculate Mean and SD
opt_sub_later_time_ip0=subset_table_opt_ip0_later_time["opt_index"]
opt_sub_later_time_ip1=subset_table_opt_ip1_later_time["opt_index"]
opt_sub_later_time_ip2=subset_table_opt_ip2_later_time["opt_index"]

opt_sub_later_time_mean_ip0=statistics.mean(opt_sub_later_time_ip0)
print(opt_sub_later_time_mean_ip0)
opt_sub_later_time_mean_ip1=statistics.mean(opt_sub_later_time_ip1)
print(opt_sub_later_time_mean_ip1)
opt_sub_later_time_mean_ip2=statistics.mean(opt_sub_later_time_ip2)
print(opt_sub_later_time_mean_ip2)

#calculate SD
opt_sub_later_time_sd_ip0=statistics.stdev(opt_sub_later_time_ip0)
print(opt_sub_later_time_sd_ip0)

opt_sub_later_time_sd_ip1=statistics.stdev(opt_sub_later_time_ip1)
print(opt_sub_later_time_sd_ip1)

opt_sub_later_time_sd_ip2=statistics.stdev(opt_sub_later_time_ip2)
print(opt_sub_later_time_sd_ip2) 
      

### finished option section

#creating attribute index
total_amount_points=combined_table["t_box1"] + combined_table["t_box2"]
combined_table["total_amount_points"] = total_amount_points   

total_amount_points_mean = statistics.mean(total_amount_points)
print(total_amount_points_mean) #7.913329676357653

total_time_points=combined_table["t_box3"] + combined_table["t_box4"]
combined_table["total_time_points"] = total_time_points 


total_time_points_mean = statistics.mean(total_time_points)
print(total_time_points_mean) #3.97970378496983

##kruskal-test with combined_table (all data_sets)
attr_index=(total_amount_points - total_time_points)/(total_amount_points + total_time_points)
combined_table["attr_index"] = attr_index

mean_attr_index=statistics.mean(attr_index)
print(mean_attr_index)
stdev_attr_index=statistics.stdev(attr_index)
print(stdev_attr_index)

attr_index_treatment = combined_table[["attr_index", "ip"]]

##creating the additional lists for the indexes
combined_table_subset_with_index = combined_table.loc[(combined_table['percentage_new'] >= 15) & (combined_table['percentage_new'] <= 50)]
combined_table_soon_time_index=combined_table[combined_table["Soon_Time"]=="0 weeks"]
combined_table_subset_soon_time_index=combined_table_subset_with_index[combined_table_subset_with_index["Soon_Time"]=="0 weeks"]
combined_table_later_time_index=combined_table[combined_table["Soon_Time"]=="2 weeks"]
combined_table_subset_later_time_index=combined_table_subset_with_index[combined_table_subset_with_index["Soon_Time"]=="2 weeks"]

combined_table_soon_time_index = combined_table_soon_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_soon_time_index = combined_table_subset_soon_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_later_time_index = combined_table_later_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)
combined_table_subset_later_time_index = combined_table_subset_later_time_index.rename(columns = {'ip_new': 'Treatment', 'percentage_new': 'Percentage_Difference'}, inplace = False)


combined_table_attr_ip0=attr_index_treatment[attr_index_treatment["ip"]==0]
combined_table_attr_ip1=attr_index_treatment[attr_index_treatment["ip"]==1]
combined_table_attr_ip2=attr_index_treatment[attr_index_treatment["ip"]==2]

H, pval =stats.kruskal(combined_table_attr_ip0['attr_index'], combined_table_attr_ip1['attr_index'], 
                       combined_table_attr_ip2['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
 
#Calculate Mean and SD
attr_ip0=combined_table_attr_ip0["attr_index"]
attr_ip1=combined_table_attr_ip1["attr_index"]
attr_ip2=combined_table_attr_ip2["attr_index"]

attr_mean_ip0=statistics.mean(attr_ip0)
print(attr_mean_ip0)
attr_mean_ip1=statistics.mean(attr_ip1)
print(attr_mean_ip1)
attr_mean_ip2=statistics.mean(attr_ip2)
print(attr_mean_ip2)

#calculate SD
attr_sd_ip0=statistics.stdev(attr_ip0)
print(attr_sd_ip0)

attr_sd_ip1=statistics.stdev(attr_ip1)
print(attr_sd_ip1)

attr_sd_ip2=statistics.stdev(attr_ip2)
print(attr_sd_ip2) 
      
   
##krusal-test with subset of data
##create subset of data
combined_table_subset_with_index = combined_table.loc[(combined_table['percentage_new'] >= 15) & (combined_table['percentage_new'] <= 50)]

attr_index_treatment_subset = combined_table_subset_with_index[["attr_index", "ip"]]

subset_table_attr_ip0=attr_index_treatment_subset[attr_index_treatment_subset["ip"]==0]
subset_table_attr_ip1=attr_index_treatment_subset[attr_index_treatment_subset["ip"]==1]
subset_table_attr_ip2=attr_index_treatment_subset[attr_index_treatment_subset["ip"]==2]

H, pval =stats.kruskal(subset_table_attr_ip0['attr_index'], subset_table_attr_ip1['attr_index'], 
                       subset_table_attr_ip2['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
  
#Calculate Mean and SD
attr_sub_ip0=subset_table_attr_ip0["attr_index"]
attr_sub_ip1=subset_table_attr_ip1["attr_index"]
attr_sub_ip2=subset_table_attr_ip2["attr_index"]

attr_sub_mean_ip0=statistics.mean(attr_sub_ip0)
print(attr_sub_mean_ip0)
attr_sub_mean_ip1=statistics.mean(attr_sub_ip1)
print(attr_sub_mean_ip1)
attr_sub_mean_ip2=statistics.mean(attr_sub_ip2)
print(attr_sub_mean_ip2)

#calculate SD
attr_sub_sd_ip0=statistics.stdev(attr_sub_ip0)
print(attr_sub_sd_ip0)

attr_sub_sd_ip1=statistics.stdev(attr_sub_ip1)
print(attr_sub_sd_ip1)

attr_sub_sd_ip2=statistics.stdev(attr_sub_ip2)
print(attr_sub_sd_ip2) 
      

##Kruskal-test with subsets as well as time options

##combined_table_soon_time_index

attr_index_treatment_soon_time_index = combined_table_soon_time_index[["attr_index", "ip"]]

table_attr_ip0_soon_time=attr_index_treatment_soon_time_index[attr_index_treatment_soon_time_index["ip"]==0]
table_attr_ip1_soon_time=attr_index_treatment_soon_time_index[attr_index_treatment_soon_time_index["ip"]==1]
table_attr_ip2_soon_time=attr_index_treatment_soon_time_index[attr_index_treatment_soon_time_index["ip"]==2]

H, pval =stats.kruskal(table_attr_ip0_soon_time['attr_index'], table_attr_ip1_soon_time['attr_index'], 
                       table_attr_ip2_soon_time['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
    
#Calculate Mean and SD
attr_soon_ip0=table_attr_ip0_soon_time["attr_index"]
attr_soon_ip1=table_attr_ip1_soon_time["attr_index"]
attr_soon_ip2=table_attr_ip2_soon_time["attr_index"]

attr_soon_mean_ip0=statistics.mean(attr_soon_ip0)
print(attr_soon_mean_ip0)
attr_soon_mean_ip1=statistics.mean(attr_soon_ip1)
print(attr_soon_mean_ip1)
attr_soon_mean_ip2=statistics.mean(attr_soon_ip2)
print(attr_soon_mean_ip2)

#calculate SD
attr_soon_sd_ip0=statistics.stdev(attr_soon_ip0)
print(attr_soon_sd_ip0)

attr_soon_sd_ip1=statistics.stdev(attr_soon_ip1)
print(attr_soon_sd_ip1)

attr_soon_sd_ip2=statistics.stdev(attr_soon_ip2)
print(attr_soon_sd_ip2) 
      
##combined_table_subset_soon_time_index

attr_index_treatment_subset_soon_time_index = combined_table_subset_soon_time_index[["attr_index", "ip"]]

subset_table_attr_ip0_soon_time=attr_index_treatment_subset_soon_time_index[attr_index_treatment_subset_soon_time_index["ip"]==0]
subset_table_attr_ip1_soon_time=attr_index_treatment_subset_soon_time_index[attr_index_treatment_subset_soon_time_index["ip"]==1]
subset_table_attr_ip2_soon_time=attr_index_treatment_subset_soon_time_index[attr_index_treatment_subset_soon_time_index["ip"]==2]

H, pval =stats.kruskal(subset_table_attr_ip0_soon_time['attr_index'], subset_table_attr_ip1_soon_time['attr_index'], 
                       subset_table_attr_ip2_soon_time['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#Calculate Mean and SD
attr_sub_soon_ip0=subset_table_attr_ip0_soon_time["attr_index"]
attr_sub_soon_ip1=subset_table_attr_ip1_soon_time["attr_index"]
attr_sub_soon_ip2=subset_table_attr_ip2_soon_time["attr_index"]

attr_sub_soon_mean_ip0=statistics.mean(attr_sub_soon_ip0)
print(attr_sub_soon_mean_ip0)
attr_sub_soon_mean_ip1=statistics.mean(attr_sub_soon_ip1)
print(attr_sub_soon_mean_ip1)
attr_sub_soon_mean_ip2=statistics.mean(attr_sub_soon_ip2)
print(attr_sub_soon_mean_ip2)

#calculate SD
attr_sub_soon_sd_ip0=statistics.stdev(attr_sub_soon_ip0)
print(attr_sub_soon_sd_ip0)

attr_sub_soon_sd_ip1=statistics.stdev(attr_sub_soon_ip1)
print(attr_sub_soon_sd_ip1)

attr_sub_soon_sd_ip2=statistics.stdev(attr_sub_soon_ip2)
print(attr_sub_soon_sd_ip2)   
 
##combined_table_later_time_index


attr_index_treatment_later_index = combined_table_later_time_index[["attr_index", "ip"]]

table_attr_ip0_later_time=attr_index_treatment_later_index[attr_index_treatment_later_index["ip"]==0]
table_attr_ip1_later_time=attr_index_treatment_later_index[attr_index_treatment_later_index["ip"]==1]
table_attr_ip2_later_time=attr_index_treatment_later_index[attr_index_treatment_later_index["ip"]==2]

H, pval =stats.kruskal(table_attr_ip0_later_time['attr_index'], table_attr_ip1_later_time['attr_index'], 
                       table_attr_ip2_later_time['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#Calculate Mean and SD
attr_later_ip0=table_attr_ip0_later_time["attr_index"]
attr_later_ip1=table_attr_ip1_later_time["attr_index"]
attr_later_ip2=table_attr_ip2_later_time["attr_index"]

attr_later_mean_ip0=statistics.mean(attr_later_ip0)
print(attr_later_mean_ip0)
attr_later_mean_ip1=statistics.mean(attr_later_ip1)
print(attr_later_mean_ip1)
attr_later_mean_ip2=statistics.mean(attr_later_ip2)
print(attr_later_mean_ip2)

#calculate SD
attr_later_sd_ip0=statistics.stdev(attr_later_ip0)
print(attr_later_sd_ip0)

attr_later_sd_ip1=statistics.stdev(attr_later_ip1)
print(attr_later_sd_ip1)

attr_later_sd_ip2=statistics.stdev(attr_later_ip2)
print(attr_later_sd_ip2)   
 

##combined_table_subset_later_time_index


attr_index_treatment_subset_later_time_index = combined_table_subset_later_time_index[["attr_index", "ip"]]

subset_table_attr_ip0_later_time=attr_index_treatment_subset_later_time_index[attr_index_treatment_subset_later_time_index["ip"]==0]
subset_table_attr_ip1_later_time=attr_index_treatment_subset_later_time_index[attr_index_treatment_subset_later_time_index["ip"]==1]
subset_table_attr_ip2_later_time=attr_index_treatment_subset_later_time_index[attr_index_treatment_subset_later_time_index["ip"]==2]

H, pval =stats.kruskal(subset_table_attr_ip0_later_time['attr_index'], subset_table_attr_ip1_later_time['attr_index'], 
                       subset_table_attr_ip2_later_time['attr_index'])

print("H-statistic:", H) 
print("P-Value:", pval) 

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#Calculate Mean and SD
attr_sub_later_ip0=subset_table_attr_ip0_later_time["attr_index"]
attr_sub_later_ip1=subset_table_attr_ip1_later_time["attr_index"]
attr_sub_later_ip2=subset_table_attr_ip2_later_time["attr_index"]

attr_sub_later_mean_ip0=statistics.mean(attr_sub_later_ip0)
print(attr_sub_later_mean_ip0)
attr_sub_later_mean_ip1=statistics.mean(attr_sub_later_ip1)
print(attr_sub_later_mean_ip1)
attr_sub_later_mean_ip2=statistics.mean(attr_sub_later_ip2)
print(attr_sub_later_mean_ip2)

#calculate SD
attr_sub_later_sd_ip0=statistics.stdev(attr_sub_later_ip0)
print(attr_sub_later_sd_ip0)

attr_sub_later_sd_ip1=statistics.stdev(attr_sub_later_ip1)
print(attr_sub_later_sd_ip1)

attr_sub_later_sd_ip2=statistics.stdev(attr_sub_later_ip2)
print(attr_sub_later_sd_ip2)   
 


### finished attribute section


my_regression_with_index=stat.ols(formula="submitted ~ attr_index + percentage_new +ip_new  + opt_index",data=combined_table).fit()
print(my_regression_with_index.summary())

  #what Reeck et al did,  indicating both contributed to search behavior during the task.
my_regression_attr_corr_discount=stat.ols(formula="submitted ~ percentage_new +ip_new + attr_index",data=combined_table).fit()
print(my_regression_attr_corr_discount.summary())
my_regression_opt_corr_discount=stat.ols(formula="submitted ~ percentage_new +ip_new + opt_index",data=combined_table).fit()
print(my_regression_opt_corr_discount.summary())


#look for individual search effects
my_regression_individual_attr=stat.ols(formula="submitted ~attr_index",data=combined_table).fit()
print(my_regression_individual_attr.summary())

my_regression_individual_opt=stat.ols(formula="submitted ~ opt_index",data=combined_table).fit()
print(my_regression_individual_opt.summary())


combined_table.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/combined_table.csv")
combined_table_subset.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/combined_table_subset.csv")


##start of payne-index analysis
temp123 = ""
Prev_row = ""
for index, row in unproc_data_new.iterrows():
    if row["name"]=="box1" and Prev_row=="box2":
        temp123 = "attr_trans"
    elif row["name"]=="box2" and Prev_row=="box1":
        temp123 = "attr_trans"
    elif row["name"]=="box1" and Prev_row=="box3":
        temp123 = "notrans"
    elif row["name"]=="box3" and Prev_row=="box1":
        temp123 = "notrans"
    elif row["name"]=="box1" and Prev_row=="box4":
        temp123 = "notrans" 
    elif  row["name"]=="box4" and Prev_row=="box1":
        temp123 = "notrans"
    elif row["name"]=="box2" and Prev_row=="box3":
        temp123 = "opt_trans"
    elif row["name"]=="box3" and Prev_row=="box2":
        temp123 = "opt_trans"
    elif row["name"]=="box2" and Prev_row=="box4":
        temp123 = "opt_trans"
    elif row["name"]=="box4" and Prev_row=="box2":
        temp123 = "opt_trans"
    elif row["name"]=="box3" and Prev_row=="box4":
        temp123 = "attr_trans"
    elif row["name"]=="box4" and Prev_row=="box3":
        temp123 = "attr_trans"
    else:
        temp123 = "notrans"
        
    unproc_data_new.at[index,'transition'] = temp123
    Prev_row = row["name"]
    
unproc_data = unproc_data[unproc_data['time'] > 200]
unproc_data_grouped=unproc_data_new.groupby(by=["expname","ip_y","subject","transition","choice","ip_x"]).size().reset_index(name='transition_counts')


#group_percent=combined_table.groupby(by=["Percentage","ip"]).mean()

unproc_data_grouped_new= unproc_data_grouped[unproc_data_grouped["transition"].isin(["attr_trans","opt_trans"]) ]

unproc_data_with_transition = unproc_data_grouped_new.pivot_table('transition_counts', ['expname', 'ip_y', 'subject','choice','ip_x'], 'transition')
  #index to columns
unproc_data_with_transition = unproc_data_with_transition.reset_index()

unproc_data_with_transition["choice"].replace({"A": "0", "B": "1"}, inplace=True)
unproc_data_with_transition["choice"]=unproc_data_with_transition["choice"].astype(int)


#creating payne-index
payne_index = (unproc_data_with_transition["opt_trans"] - unproc_data_with_transition["attr_trans"])/(unproc_data_with_transition["attr_trans"] + unproc_data_with_transition["opt_trans"])
unproc_data_with_transition["payne_index"] = payne_index

#now dropping all data with nan
unproc_data_with_payne = unproc_data_with_transition[unproc_data_with_transition['payne_index'].notna()]

#creating datasets for the subsets
unproc_data_with_payne_subset= unproc_data_with_payne[unproc_data_with_payne["expname"].isin([1,2,4,8,9,10,12,13,17,18]) ]
unproc_data_with_payne_subset_soon= unproc_data_with_payne[unproc_data_with_payne["expname"].isin([1,2,4,8,9]) ]
unproc_data_with_payne_subset_later= unproc_data_with_payne[unproc_data_with_payne["expname"].isin([10,12,13,17,18]) ]
unproc_data_with_payne_soon= unproc_data_with_payne[unproc_data_with_payne["expname"].isin([1,2,3,4,5,6,7,8,9]) ]
unproc_data_with_payne_late= unproc_data_with_payne[unproc_data_with_payne["expname"].isin([10,11,12,13,14,15,16,17,18]) ]


unproc_data_with_payne_ip0=unproc_data_with_payne[unproc_data_with_payne["ip_y"]==0]
unproc_data_with_payne_ip1=unproc_data_with_payne[unproc_data_with_payne["ip_y"]==1]
unproc_data_with_payne_ip2=unproc_data_with_payne[unproc_data_with_payne["ip_y"]==2]

mean_payne_index=statistics.mean(unproc_data_with_payne["payne_index"])
print(mean_payne_index)
stdev_payne_index=statistics.stdev(unproc_data_with_payne["payne_index"])
print(stdev_payne_index)


H, pval =stats.kruskal(unproc_data_with_payne_ip0["payne_index"],unproc_data_with_payne_ip1["payne_index"],unproc_data_with_payne_ip2["payne_index"])


print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


ranksums(unproc_data_with_payne_ip0["payne_index"],unproc_data_with_payne_ip1["payne_index"])
ranksums(unproc_data_with_payne_ip1["payne_index"],unproc_data_with_payne_ip2["payne_index"])
ranksums(unproc_data_with_payne_ip0["payne_index"],unproc_data_with_payne_ip2["payne_index"])

#Calculate Mean and SD
payne_ip0=unproc_data_with_payne_ip0["payne_index"]
payne_ip1=unproc_data_with_payne_ip1["payne_index"]
payne_ip2=unproc_data_with_payne_ip2["payne_index"]

mean_payne_ip0=statistics.mean(payne_ip0)
print(mean_payne_ip0)
mean_payne_ip1=statistics.mean(payne_ip1)
print(mean_payne_ip1)
mean_payne_ip2=statistics.mean(payne_ip2)
print(mean_payne_ip2)

#calculate SD
sd_payne_ip0=statistics.stdev(payne_ip0)
print(sd_payne_ip0)

sd_payne_ip1=statistics.stdev(payne_ip1)
print(sd_payne_ip1)

sd_payne_ip2=statistics.stdev(payne_ip2)
print(sd_payne_ip2)   
 
#kruskal.wallis test for subset unproc_data_with_payne_subset
unproc_data_with_payne_subset_ip0=unproc_data_with_payne_subset[unproc_data_with_payne_subset["ip_y"]==0]
unproc_data_with_payne_subset_ip1=unproc_data_with_payne_subset[unproc_data_with_payne_subset["ip_y"]==1]
unproc_data_with_payne_subset_ip2=unproc_data_with_payne_subset[unproc_data_with_payne_subset["ip_y"]==2]


H, pval =stats.kruskal(unproc_data_with_payne_subset_ip0["payne_index"],unproc_data_with_payne_subset_ip1["payne_index"],unproc_data_with_payne_subset_ip2["payne_index"])

print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(unproc_data_with_payne_subset_ip0["payne_index"],unproc_data_with_payne_subset_ip1["payne_index"])
ranksums(unproc_data_with_payne_subset_ip1["payne_index"],unproc_data_with_payne_subset_ip2["payne_index"])
ranksums(unproc_data_with_payne_subset_ip0["payne_index"],unproc_data_with_payne_subset_ip2["payne_index"])


#Calculate Mean and SD
payne_sub_ip0=unproc_data_with_payne_subset_ip0["payne_index"]
payne_sub_ip1=unproc_data_with_payne_subset_ip1["payne_index"]
payne_sub_ip2=unproc_data_with_payne_subset_ip2["payne_index"]

mean_payne_sub_ip0=statistics.mean(payne_sub_ip0)
print(mean_payne_sub_ip0)
mean_payne_sub_ip1=statistics.mean(payne_sub_ip1)
print(mean_payne_sub_ip1)
mean_payne_sub_ip2=statistics.mean(payne_sub_ip2)
print(mean_payne_sub_ip2)

#calculate SD
sd_payne_sub_ip0=statistics.stdev(payne_sub_ip0)
print(sd_payne_sub_ip0)

sd_payne_sub_ip1=statistics.stdev(payne_sub_ip1)
print(sd_payne_sub_ip1)

sd_payne_sub_ip2=statistics.stdev(payne_sub_ip2)
print(sd_payne_sub_ip2)   
 
#kruskal.wallis test for subset unproc_data_with_payne_subset_soon
unproc_data_with_payne_subset_soon_ip0=unproc_data_with_payne_subset_soon[unproc_data_with_payne_subset_soon["ip_y"]==0]
unproc_data_with_payne_subset_soon_ip1=unproc_data_with_payne_subset_soon[unproc_data_with_payne_subset_soon["ip_y"]==1]
unproc_data_with_payne_subset_soon_ip2=unproc_data_with_payne_subset_soon[unproc_data_with_payne_subset_soon["ip_y"]==2]


H, pval =stats.kruskal(unproc_data_with_payne_subset_soon_ip0["payne_index"],unproc_data_with_payne_subset_soon_ip1["payne_index"],unproc_data_with_payne_subset_soon_ip2["payne_index"])

print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


ranksums(unproc_data_with_payne_subset_soon_ip0["payne_index"],unproc_data_with_payne_subset_soon_ip1["payne_index"])
ranksums(unproc_data_with_payne_subset_soon_ip1["payne_index"],unproc_data_with_payne_subset_soon_ip2["payne_index"])
ranksums(unproc_data_with_payne_subset_soon_ip0["payne_index"],unproc_data_with_payne_subset_soon_ip2["payne_index"])

#Calculate Mean and SD
payne_sub_soon_ip0=unproc_data_with_payne_subset_soon_ip0["payne_index"]
payne_sub_soon_ip1=unproc_data_with_payne_subset_soon_ip1["payne_index"]
payne_sub_soon_ip2=unproc_data_with_payne_subset_soon_ip2["payne_index"]

mean_payne_soon_sub_ip0=statistics.mean(payne_sub_soon_ip0)
print(mean_payne_soon_sub_ip0)
mean_payne_soon_sub_ip1=statistics.mean(payne_sub_soon_ip1)
print(mean_payne_soon_sub_ip1)
mean_payne_soon_sub_ip2=statistics.mean(payne_sub_soon_ip2)
print(mean_payne_soon_sub_ip1)

#calculate SD
sd_payne_soon_sub_ip0=statistics.stdev(payne_sub_soon_ip0)
print(sd_payne_soon_sub_ip0)

sd_payne_soon_sub_ip1=statistics.stdev(payne_sub_soon_ip1)
print(sd_payne_soon_sub_ip1)

sd_payne_soon_sub_ip2=statistics.stdev(payne_sub_soon_ip2)
print(sd_payne_soon_sub_ip2)

#kruskal.wallis test for subset unproc_data_with_payne_subset_later
unproc_data_with_payne_subset_later_ip0=unproc_data_with_payne_subset_later[unproc_data_with_payne_subset_later["ip_y"]==0]
unproc_data_with_payne_subset_later_ip1=unproc_data_with_payne_subset_later[unproc_data_with_payne_subset_later["ip_y"]==1]
unproc_data_with_payne_subset_later_ip2=unproc_data_with_payne_subset_later[unproc_data_with_payne_subset_later["ip_y"]==2]


H, pval =stats.kruskal(unproc_data_with_payne_subset_later_ip0["payne_index"],unproc_data_with_payne_subset_later_ip1["payne_index"],unproc_data_with_payne_subset_later_ip2["payne_index"])

print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(unproc_data_with_payne_subset_later_ip0["payne_index"],unproc_data_with_payne_subset_later_ip1["payne_index"])
ranksums(unproc_data_with_payne_subset_later_ip1["payne_index"],unproc_data_with_payne_subset_later_ip2["payne_index"])
ranksums(unproc_data_with_payne_subset_later_ip0["payne_index"],unproc_data_with_payne_subset_later_ip2["payne_index"])


#Calculate Mean and SD
payne_sub_later_ip0=unproc_data_with_payne_subset_later_ip0["payne_index"]
payne_sub_later_ip1=unproc_data_with_payne_subset_later_ip1["payne_index"]
payne_sub_later_ip2=unproc_data_with_payne_subset_later_ip2["payne_index"]

mean_payne_later_sub_ip0=statistics.mean(payne_sub_later_ip0)
print(mean_payne_later_sub_ip0)
mean_payne_later_sub_ip1=statistics.mean(payne_sub_later_ip1)
print(mean_payne_later_sub_ip1)
mean_payne_later_sub_ip2=statistics.mean(payne_sub_later_ip2)
print(mean_payne_later_sub_ip2)

#calculate SD
sd_payne_later_sub_ip0=statistics.stdev(payne_sub_later_ip0)
print(sd_payne_later_sub_ip0)

sd_payne_later_sub_ip1=statistics.stdev(payne_sub_later_ip1)
print(sd_payne_later_sub_ip1)

sd_payne_later_sub_ip2=statistics.stdev(payne_sub_later_ip2)
print(sd_payne_later_sub_ip2)


##kruskal.wallis test for subset unproc_data_with_payne_soon
unproc_data_with_payne_soon_ip0=unproc_data_with_payne_soon[unproc_data_with_payne_soon["ip_y"]==0]
unproc_data_with_payne_soon_ip1=unproc_data_with_payne_soon[unproc_data_with_payne_soon["ip_y"]==1]
unproc_data_with_payne_soon_ip2=unproc_data_with_payne_soon[unproc_data_with_payne_soon["ip_y"]==2]


H, pval =stats.kruskal(unproc_data_with_payne_soon_ip0["payne_index"],unproc_data_with_payne_soon_ip1["payne_index"],unproc_data_with_payne_soon_ip2["payne_index"])

print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

ranksums(unproc_data_with_payne_soon_ip0["payne_index"],unproc_data_with_payne_soon_ip1["payne_index"])
ranksums(unproc_data_with_payne_soon_ip1["payne_index"],unproc_data_with_payne_soon_ip2["payne_index"])
ranksums(unproc_data_with_payne_soon_ip0["payne_index"],unproc_data_with_payne_soon_ip2["payne_index"])

#Calculate Mean and SD
payne_soon_ip0=unproc_data_with_payne_soon_ip0["payne_index"]
payne_soon_ip1=unproc_data_with_payne_soon_ip1["payne_index"]
payne_soon_ip2=unproc_data_with_payne_soon_ip2["payne_index"]

mean_payne_soon_ip0=statistics.mean(payne_soon_ip0)
print(mean_payne_later_sub_ip0)
mean_payne_soon_ip1=statistics.mean(payne_soon_ip1)
print(mean_payne_later_sub_ip1)
mean_payne_soon_ip2=statistics.mean(payne_soon_ip2)
print(mean_payne_later_sub_ip2)

#calculate SD
sd_payne_soon_ip0=statistics.stdev(payne_soon_ip0)
print(sd_payne_soon_ip0)

sd_payne_soon_ip1=statistics.stdev(payne_soon_ip1)
print(sd_payne_soon_ip1)

sd_payne_soon_ip2=statistics.stdev(payne_soon_ip2)
print(sd_payne_soon_ip2)

##kruskal.wallis test for unproc_data_with_payne_late
unproc_data_with_payne_later_ip0=unproc_data_with_payne_late[unproc_data_with_payne_late["ip_y"]==0]
unproc_data_with_payne_later_ip1=unproc_data_with_payne_late[unproc_data_with_payne_late["ip_y"]==1]
unproc_data_with_payne_later_ip2=unproc_data_with_payne_late[unproc_data_with_payne_late["ip_y"]==2]


H, pval =stats.kruskal(unproc_data_with_payne_later_ip0["payne_index"],unproc_data_with_payne_later_ip1["payne_index"],unproc_data_with_payne_later_ip2["payne_index"])

print("H-statistic:", H)
print("P-Value:", pval)
# 
if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


ranksums(unproc_data_with_payne_later_ip0["payne_index"],unproc_data_with_payne_later_ip1["payne_index"])
ranksums(unproc_data_with_payne_later_ip1["payne_index"],unproc_data_with_payne_later_ip2["payne_index"])
ranksums(unproc_data_with_payne_later_ip0["payne_index"],unproc_data_with_payne_later_ip2["payne_index"])

#Calculate Mean and SD
payne_later_ip0=unproc_data_with_payne_later_ip0["payne_index"]
payne_later_ip1=unproc_data_with_payne_later_ip1["payne_index"]
payne_later_ip2=unproc_data_with_payne_later_ip2["payne_index"]

mean_payne_later_ip0=statistics.mean(payne_later_ip0)
print(mean_payne_later_ip0)
mean_payne_later_ip1=statistics.mean(payne_later_ip1)
print(mean_payne_later_ip1)
mean_payne_later_ip2=statistics.mean(payne_later_ip2)
print(mean_payne_later_ip2)

#calculate SD
sd_payne_later_ip0=statistics.stdev(payne_later_ip0)
print(sd_payne_later_ip0)

sd_payne_later_ip1=statistics.stdev(payne_later_ip1)
print(sd_payne_later_ip1)

sd_payne_later_ip2=statistics.stdev(payne_later_ip2)
print(sd_payne_later_ip2)



unproc_data_with_payne["ip_y"].replace({0:"0", 1:"1",2: "2"}, inplace=True)


unproc_data_with_payne["expname"].replace({1:15, 2:50,3:1,4:35,5:3,6:10,7:5,8:25,9:20,10:20,11:1,12:35,13:25,14:3,15:10,16:5,17:15,18:50}, inplace=True)


my_regression_only_payne=stat.ols(formula="choice ~ payne_index",data=unproc_data_with_payne).fit()
print(my_regression_only_payne.summary())  


my_regression_payne=stat.ols(formula="choice ~ payne_index  + ip_y + expname",data=unproc_data_with_payne).fit()
print(my_regression_payne.summary())

my_regression_with_all_index=stat.ols(formula="submitted ~ attr_index + percentage_new +ip_new + opt_index",data=combined_table).fit()
print(my_regression_with_index.summary())

##analysis of BIS-11 data

table_bis11["ip"]=combined_table["ip"].astype(str)

attention_bis_attention= table_bis11[table_bis11["question"].isin(["q5", "q9","q11","q20", "q28"]) ]
attention_bis_cog_instability= table_bis11[table_bis11["question"].isin(["q6", "q24","q26"]) ]
motor_bis_motor= table_bis11[table_bis11["question"].isin(["q2","q3","q4","q17", "q19", "q22", "q25"]) ]
motor_bis_preseverance= table_bis11[table_bis11["question"].isin(["q16", "q21","q23","q30"]) ]
nonplanning_bis_selfcontrol= table_bis11[table_bis11["question"].isin(["q1","q7","q8","q12", "q13", "q14"]) ]
nonplanning_bis_cogcomplex= table_bis11[table_bis11["question"].isin(["q10", "q15","q18","q27", "q29"]) ]
attention_bis=table_bis11[table_bis11["question"].isin(["q5", "q9","q11","q20", "q28","q6", "q24","q26"]) ]
motor_bis=table_bis11[table_bis11["question"].isin(["q2","q3","q4","q17", "q19", "q22", "q25","q16", "q21","q23","q30"]) ]
non_planning=table_bis11[table_bis11["question"].isin(["q1","q7","q8","q12", "q13", "q14","q10", "q15","q18","q27", "q29"]) ]

#analyzing bis11-total
Ip0_bis= table_bis11[table_bis11["ip"]=="0"]

answer_ip0 = Ip0_bis["answer"]

Ip1_bis= table_bis11[table_bis11["ip"]=="1"]

answer_ip1 = Ip1_bis["answer"]

Ip2_bis= table_bis11[table_bis11["ip"]=="2"]

answer_ip2 = Ip2_bis["answer"]

answer_ip0_mean = statistics.mean(answer_ip0)
print(answer_ip0_mean)
answer_ip1_mean = statistics.mean(answer_ip1)
print(answer_ip1_mean)
answer_ip2_mean = statistics.mean(answer_ip2)
print(answer_ip2_mean)

answer_ip0_std = statistics.stdev(answer_ip0)
print(answer_ip0_std)
answer_ip1_std = statistics.stdev(answer_ip1)
print(answer_ip1_std)
answer_ip2_std = statistics.stdev(answer_ip2)
print(answer_ip2_std)

ave_ip0bis=sum(Ip0_bis["answer"])/30
print(ave_ip0bis)
ave_ip1bis=sum(Ip1_bis["answer"])/30
print(ave_ip1bis)
ave_ip2bis=sum(Ip2_bis["answer"])/30
print(ave_ip2bis)


H, pval =stats.kruskal(answer_ip0,answer_ip1,answer_ip2)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#analyzing attention bis-11
Ip0_attention_bis= attention_bis[attention_bis["ip"]=="0"]

answer_ip0_attention_bis = Ip0_attention_bis["answer"]


Ip1_attention_bis= attention_bis[attention_bis["ip"]=="1"]

answer_ip1_attention_bis = Ip1_attention_bis["answer"]


Ip2_attention_bis= attention_bis[attention_bis["ip"]=="2"]

answer_ip2_attention_bis = Ip2_attention_bis["answer"]


H, pval =stats.kruskal(answer_ip0_attention_bis,answer_ip1_attention_bis,answer_ip2_attention_bis)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
#Calculate Mean and SD


answer_ip0_attention_bis_mean=statistics.mean(answer_ip0_attention_bis)
print(answer_ip0_attention_bis_mean)
answer_ip1_attention_bis_mean=statistics.mean(answer_ip1_attention_bis)
print(answer_ip1_attention_bis_mean)
answer_ip2_attention_bis_mean=statistics.mean(answer_ip2_attention_bis)
print(answer_ip2_attention_bis_mean)

#calculate SD
answer_ip0_attention_bis_sd=statistics.stdev(answer_ip0_attention_bis)
print(answer_ip0_attention_bis_sd)

answer_ip1_attention_bis_mean=statistics.stdev(answer_ip1_attention_bis)
print(answer_ip1_attention_bis_mean)

answer_ip2_attention_bis_mean=statistics.stdev(answer_ip2_attention_bis)
print(answer_ip2_attention_bis_mean)


#analyzing  motor bis
Ip0_motor_bis= motor_bis[motor_bis["ip"]=="0"]

answer_ip0_motor_bis = Ip0_motor_bis["answer"]


Ip1_motor_bis= motor_bis[motor_bis["ip"]=="1"]

answer_ip1_motor_bis = Ip1_motor_bis["answer"]


Ip2_motor_bis= motor_bis[motor_bis["ip"]=="2"]

answer_ip2_motor_bis = Ip2_motor_bis["answer"]


H, pval =stats.kruskal(answer_ip0_motor_bis,answer_ip1_motor_bis,answer_ip2_motor_bis)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
#calculate mean
motor_mean_bis_ip0=statistics.mean(answer_ip0_motor_bis)
print(motor_mean_bis_ip0)
motor_mean_bis_ip1=statistics.mean(answer_ip1_motor_bis)
print(motor_mean_bis_ip1)
motor_mean_bis_ip2=statistics.mean(answer_ip2_motor_bis)
print(motor_mean_bis_ip2)

#calculate SD
motor_mean_sd_ip0=statistics.stdev(answer_ip0_motor_bis)
print(motor_mean_sd_ip0)

motor_mean_sd_ip1=statistics.stdev(answer_ip1_motor_bis)
print(motor_mean_sd_ip1)

motor_mean_sd_ip2=statistics.stdev(answer_ip2_motor_bis)
print(motor_mean_sd_ip2)
# analyzing bis-11 nonplanning

Ip0_nonplan_bis= non_planning[non_planning["ip"]=="0"]

answer_ip0_nonplan_bis = Ip0_nonplan_bis["answer"]


Ip1_nonplan_bis= non_planning[non_planning["ip"]=="1"]

answer_ip1nonplan_bis = Ip1_nonplan_bis["answer"]


Ip2_nonplan_bis= non_planning[non_planning["ip"]=="2"]

answer_ip2_nonplan_bis = Ip2_nonplan_bis["answer"]


H, pval =stats.kruskal(answer_ip0_nonplan_bis,answer_ip1nonplan_bis,answer_ip2_nonplan_bis)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

nonplan_mean_bis_ip0=statistics.mean(answer_ip0_nonplan_bis)
print(nonplan_mean_bis_ip0)
nonplan_mean_bis_ip1=statistics.mean(answer_ip1nonplan_bis)
print(nonplan_mean_bis_ip1)
nonplan_mean_bis_ip2=statistics.mean(answer_ip2_nonplan_bis)
print(nonplan_mean_bis_ip2)

#calculate SD
nonplan_mean_sd_ip0=statistics.stdev(answer_ip0_nonplan_bis)
print(nonplan_mean_sd_ip0)

nonplan_mean_sd_ip1=statistics.stdev(answer_ip1nonplan_bis)
print(nonplan_mean_sd_ip1)

nonplan_mean_sd_ip2=statistics.stdev(answer_ip2_nonplan_bis)
print(nonplan_mean_sd_ip2)
#analyzing bis-11 attention_bis_attention


Ip0_attention_bis_attention= attention_bis_attention[attention_bis_attention["ip"]=="0"]

answer_ip0_attention_attention = Ip0_attention_bis_attention["answer"]

Ip1_attention_bis_attention= attention_bis_attention[attention_bis_attention["ip"]=="1"]

answer_ip1_attention_attention = Ip1_attention_bis_attention["answer"]

Ip2_attention_bis_attention= attention_bis_attention[attention_bis_attention["ip"]=="2"]

answer_ip2_attention_attention = Ip2_attention_bis_attention["answer"]

answer_mean_ip0_attention_attention = statistics.mean(answer_ip0_attention_attention)
print(answer_mean_ip0_attention_attention)
answer_mean_ip1_attention_attention = statistics.mean(answer_ip1_attention_attention)
print(answer_mean_ip1_attention_attention)
answer_mean_ip2_attention_attention = statistics.mean(answer_ip2_attention_attention)
print(answer_mean_ip2_attention_attention)


answer_sd_ip0_attention_attention = statistics.stdev(answer_ip0_attention_attention)
print(answer_sd_ip0_attention_attention)

answer_sd_ip1_attention_attention = statistics.stdev(answer_ip1_attention_attention)
print(answer_sd_ip1_attention_attention)

answer_sd_ip2_attention_attention = statistics.stdev(answer_ip2_attention_attention)
print(answer_sd_ip2_attention_attention)

ave_ip0_attention_attention=sum(Ip0_attention_bis_attention["answer"])/30
print(ave_ip0_attention_attention)
ave_ip1_attention_attention=sum(Ip1_attention_bis_attention["answer"])/30
print(ave_ip1_attention_attention)
ave_ip2_attention_attention=sum(Ip2_attention_bis_attention["answer"])/30
print(ave_ip2_attention_attention)


H, pval =stats.kruskal(answer_ip0_attention_attention,answer_ip1_attention_attention,answer_ip2_attention_attention)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#analyzing bis-11 attention_bis_cog_instability


Ip0_attention_bis_cog_instability= attention_bis_cog_instability[attention_bis_cog_instability["ip"]=="0"]

answer_ip0_attention_bis_cog_instability = Ip0_attention_bis_cog_instability["answer"]


Ip1_attention_bis_cog_instability= attention_bis_cog_instability[attention_bis_cog_instability["ip"]=="1"]

answer_ip1_attention_bis_cog_instability = Ip1_attention_bis_cog_instability["answer"]


Ip2_attention_bis_cog_instability= attention_bis_cog_instability[attention_bis_cog_instability["ip"]=="2"]

answer_ip2_attention_bis_cog_instability = Ip2_attention_bis_cog_instability["answer"]


H, pval =stats.kruskal(answer_ip0_attention_bis_cog_instability,answer_ip1_attention_bis_cog_instability,answer_ip2_attention_bis_cog_instability)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")


attcog_mean_bis_ip0=statistics.mean(answer_ip0_attention_bis_cog_instability)
print(attcog_mean_bis_ip0)
attcog_mean_bis_ip1=statistics.mean(answer_ip1_attention_bis_cog_instability)
print(attcog_mean_bis_ip1)
attcog_mean_bis_ip2=statistics.mean(answer_ip2_attention_bis_cog_instability)
print(attcog_mean_bis_ip2)

#calculate SD
attcog_sd_ip0=statistics.stdev(answer_ip0_attention_bis_cog_instability)
print(attcog_sd_ip0)

attcog_sd_ip1=statistics.stdev(answer_ip1_attention_bis_cog_instability)
print(attcog_sd_ip1)

attcog_sd_ip2=statistics.stdev(answer_ip2_attention_bis_cog_instability)
print(attcog_sd_ip2)
#analyzing bis-11 motor_bis_motor

Ip0_motor_bis_motor= motor_bis_motor[motor_bis_motor["ip"]=="0"]

answer_ip0_motor_bis_motor = Ip0_motor_bis_motor["answer"]


Ip1_motor_bis_motor= motor_bis_motor[motor_bis_motor["ip"]=="1"]

answer_ip1_motor_bis_motor = Ip1_motor_bis_motor["answer"]


Ip2_motor_bis_motor= motor_bis_motor[motor_bis_motor["ip"]=="2"]

answer_ip2_motor_bis_motor = Ip2_motor_bis_motor["answer"]


H, pval =stats.kruskal(answer_ip0_motor_bis_motor,answer_ip1_motor_bis_motor,answer_ip2_motor_bis_motor)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
    
motmot_mean_bis_ip0=statistics.mean(answer_ip0_motor_bis_motor)
print(motmot_mean_bis_ip0)
motmot_mean_bis_ip1=statistics.mean(answer_ip1_motor_bis_motor)
print(motmot_mean_bis_ip1)
motmot_mean_bis_ip2=statistics.mean(answer_ip2_motor_bis_motor)
print(motmot_mean_bis_ip2)

#calculate SD
motmot_sd_ip0=statistics.stdev(answer_ip0_attention_bis_cog_instability)
print(motmot_sd_ip0)

motmot_sd_ip1=statistics.stdev(answer_ip1_attention_bis_cog_instability)
print(motmot_sd_ip1)

motmot_sd_ip2=statistics.stdev(answer_ip2_attention_bis_cog_instability)
print(motmot_sd_ip2)

#analyzing bis-11 motor_bis_preseverance

Ip0_motor_bis_preseverance= motor_bis_preseverance[motor_bis_preseverance["ip"]=="0"]

answer_ip0_motor_bis_preseverance = Ip0_motor_bis_preseverance["answer"]


Ip1_motor_bis_preseverance= motor_bis_preseverance[motor_bis_preseverance["ip"]=="1"]

answer_ip1_motor_bis_preseverance = Ip1_motor_bis_preseverance["answer"]


Ip2_motor_bis_preseverance= motor_bis_preseverance[motor_bis_preseverance["ip"]=="2"]

answer_ip2_motor_bis_preseverance = Ip2_motor_bis_preseverance["answer"]


H, pval =stats.kruskal(answer_ip0_motor_bis_preseverance,answer_ip1_motor_bis_preseverance,answer_ip2_motor_bis_preseverance)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

#calc mean and sd
premot_mean_bis_ip0=statistics.mean(answer_ip0_motor_bis_preseverance)
print(premot_mean_bis_ip0)
premot_mean_bis_ip1=statistics.mean(answer_ip1_motor_bis_preseverance)
print(premot_mean_bis_ip1)
premot_mean_bis_ip2=statistics.mean(answer_ip2_motor_bis_preseverance)
print(premot_mean_bis_ip2)

#calculate SD
premot_sd_ip0=statistics.stdev(answer_ip0_motor_bis_preseverance)
print(premot_sd_ip0)

premot_sd_ip1=statistics.stdev(answer_ip1_motor_bis_preseverance)
print(premot_sd_ip1)

premot_sd_ip2=statistics.stdev(answer_ip2_motor_bis_preseverance)
print(premot_sd_ip2)   
    
#anlayzing bis-11 nonplanning_bis_selfcontrol

Ip0_nonplanning_bis_selfcontrol= nonplanning_bis_selfcontrol[nonplanning_bis_selfcontrol["ip"]=="0"]

answer_ip0_nonplanning_bis_selfcontrol = Ip0_nonplanning_bis_selfcontrol["answer"]


Ip1_nonplanning_bis_selfcontrol= nonplanning_bis_selfcontrol[nonplanning_bis_selfcontrol["ip"]=="1"]

answer_ip1_nonplanning_bis_selfcontrole = Ip1_nonplanning_bis_selfcontrol["answer"]


Ip2_nonplanning_bis_selfcontrol= nonplanning_bis_selfcontrol[nonplanning_bis_selfcontrol["ip"]=="2"]

answer_ip2_nonplanning_bis_selfcontrol = Ip2_nonplanning_bis_selfcontrol["answer"]


H, pval =stats.kruskal(answer_ip0_nonplanning_bis_selfcontrol,answer_ip1_nonplanning_bis_selfcontrole,answer_ip2_nonplanning_bis_selfcontrol)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
#calc mean and sd
nonself_mean_bis_ip0=statistics.mean(answer_ip0_nonplanning_bis_selfcontrol)
print(nonself_mean_bis_ip0)
nonself_mean_bis_ip1=statistics.mean(answer_ip1_nonplanning_bis_selfcontrole)
print(nonself_mean_bis_ip1)
nonself_mean_bis_ip2=statistics.mean(answer_ip2_nonplanning_bis_selfcontrol)
print(nonself_mean_bis_ip2)

#calculate SD
nonself_sd_bis_ip0=statistics.stdev(answer_ip0_nonplanning_bis_selfcontrol)
print(nonself_sd_bis_ip0)

nonself_sd_bis_ip1=statistics.stdev(answer_ip1_nonplanning_bis_selfcontrole)
print(nonself_sd_bis_ip1)

nonself_sd_bis_ip2=statistics.stdev(answer_ip2_nonplanning_bis_selfcontrol)
print(nonself_sd_bis_ip2)  

#analyzing bis-11 nonplanning_bis_cogcomplex

Ip0_nonplanning_bis_cogcomplex= nonplanning_bis_cogcomplex[nonplanning_bis_cogcomplex["ip"]=="0"]

answer_ip0_nonplanning_bis_cogcomplex = Ip0_nonplanning_bis_cogcomplex["answer"]


Ip1_nnonplanning_bis_cogcomplex= nonplanning_bis_cogcomplex[nonplanning_bis_cogcomplex["ip"]=="1"]

answer_ip1_nonplanning_bis_cogcomplexx = Ip1_nnonplanning_bis_cogcomplex["answer"]


Ip2_nonplanning_bis_cogcomplex= nonplanning_bis_cogcomplex[nonplanning_bis_cogcomplex["ip"]=="2"]

answer_ip2_nonplanning_bis_cogcomplex = Ip2_nonplanning_bis_cogcomplex["answer"]


H, pval =stats.kruskal(answer_ip0_nonplanning_bis_cogcomplex,answer_ip1_nonplanning_bis_cogcomplexx,answer_ip2_nonplanning_bis_cogcomplex)

print("H-statistic:", H)
print("P-Value:", pval)

if pval < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")

cogself_mean_bis_ip0=statistics.mean(answer_ip0_nonplanning_bis_cogcomplex)
print(cogself_mean_bis_ip0)
cogself_mean_bis_ip1=statistics.mean(answer_ip1_nonplanning_bis_cogcomplexx)
print(cogself_mean_bis_ip1)
cogself_mean_bis_ip2=statistics.mean(answer_ip2_nonplanning_bis_cogcomplex)
print(cogself_mean_bis_ip2)

#calculate SD
cogself_sd_bis_ip0=statistics.stdev(answer_ip0_nonplanning_bis_cogcomplex)
print(cogself_sd_bis_ip0)

cogself_sd_bis_ip1=statistics.stdev(answer_ip1_nonplanning_bis_cogcomplexx)
print(cogself_sd_bis_ip1)

cogself_sd_bis_ip2=statistics.stdev(answer_ip2_nonplanning_bis_cogcomplex)
print(cogself_sd_bis_ip2) 

table_bis11.to_csv("/Users/neginjavaheri/Desktop/UVA/Thesis/bis_11_table.csv")


## calculating demographic means

mean_age=statistics.mean(negin_participants["Age"])
print(mean_age)
mean_children=statistics.mean(negin_participants["Children"])
print(mean_children)

negin_participants["Smokes"]=negin_participants["Smokes"].astype(int)
mean_smokes=statistics.mean(negin_participants["Smokes"])
print(mean_smokes)
negin_participants["Drinks"]=negin_participants["Drinks"].astype(int)
mean_drinks=statistics.mean(negin_participants["Drinks"])
print(mean_drinks)

countparticipantsip=negin_participants['ip'].value_counts()
print(countparticipantsip)

countparticipants_ethnicity=negin_participants['Ethnicity'].value_counts()
print(countparticipants_ethnicity)

countparticipants_eductaion=negin_participants['Education'].value_counts()
print(countparticipants_eductaion)


## creating the graphs
#average_choice_treatment = sns.violinplot(x="ip", y="submitted", data=combined_table)




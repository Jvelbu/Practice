#1 Importing and Cleaning Data set
Smart_Home <- read.csv("/Users/jayantvelichety/Desktop/Harrisburg University/PhD HU/Anal 715/DataSet/Smart_Home_Electricity_Usage_Dataset.csv")
colnames(Smart_Home)
#Checking missing values
sum(is.na(Smart_Home))
missing_values <- sapply(Smart_Home, anyNA)
missing_values
# Counting missing values in columns
missing_count <- colSums(is.na(Smart_Home))
missing_count
#Imputing missing values with median values
install.packages("dplyr")
library(dplyr)
Smart_Home_Energy <- Smart_Home %>% mutate(across(c(Electricity_Usage_kWh,Temperature_F,Humidity_Percent,Smart_Device_Usage_kWh), ~ifelse(is.na(.),median(., na.rm = TRUE), .)))
Smart_Home_Energy
sum(is.na(Smart_Home_Energy))
#2) Pick one categorical variable (with at least 3 categories and no more than 6 levels/categories; you can subset your data is needed) as your IV and one continuous/numeric variable as your DV. 
colnames(Smart_Home_Energy)
#Checking distinct categories in Season
unique(Smart_Home_Energy$Season)
#Check the summary of continious variable
summary(Smart_Home_Energy$Electricity_Usage_kWh)
#3Performing a simple analysis on the IV(Season) and DV (Season)
anova_result <- aov(Electricity_Usage_kWh ~ Season, data = Smart_Home_Energy)
summary(anova_result)
# Extract residuals from the model
residuals_anova <- residuals(anova_result)

# Shapiro-Wilk test for normality
shapiro_test <- shapiro.test(residuals_anova)
shapiro_test

# Q-Q plot for visual inspection of normality
qqnorm(residuals_anova)
qqline(residuals_anova, col = "red")

# Install car package if not already installed
 install.packages("car")

library(car)

# Levene's test for homogeneity of variances
levene_test <- leveneTest(Electricity_Usage_kWh ~ Season, data = Smart_Home_Energy)
levene_test
#4 Summary of the ANOVA result
summary(anova_result)
#ON this Anonva observation season doesnt have that much of an impact on the electricity usage
#5) Post hoc Compariosns
# Perform Tukey's HSD test (post-hoc comparisons)
tukey_test <- TukeyHSD(anova_result)
print(tukey_test)
#Overall interpration is no pairwise compariosn have shown any statstical differences since p values are all above 0,05, The Confidence intervial is 0 which says that there is no meaningful relationship with electricty and season
#6) Graph results 

 install.packages("ggplot2")

library(ggplot2)

# Create a boxplot to visualize differences in electricity usage across seasons
ggplot(Smart_Home_Energy, aes(x = Season, y = Electricity_Usage_kWh)) +
  geom_boxplot() +
  labs(title = "Electricity Usage by Season",
       x = "Season",
       y = "Electricity Usage (kWh)") +
  theme_minimal()
#Inteperation Boxplot will show the spread and median electricty usage for each season.
#7 Report and Interpret 
" " "
ANOVA Model:  Used electricity usage (kWh) as the DV and season as the IV in an ANOVA.
Result: There is no discernible variation in electricity use across seasons, as indicated by the p-value of 0.561.
Interpretation: The null hypothesis cannot be rejected because the p-value is higher than 0.05. There is no proof that the season has a major impact on electricity use.
Comparisons after the fact (optional): Tukey's HSD test can reveal particular pairwise comparisons between seasons if post-hoc testing are conducted in spite of the non-significant ANOVA result. However, it is doubtful that there will be significant changes between pairings of seasons because the overall ANOVA was not significant.
Results Graph: To see the distribution of electricity use by season, you can make a boxplot. This makes the dispersion and possible outliers easier to see.
Presenting the Findings:
Levene's Test: The assumption of homogeneity of variances was satisfied since the variances between the groups were homogeneous (p = 0.8697).
ANOVA: There was no discernible variation in electricity consumption by season (p = 0.561).
Post-Hoc (not required): When the ANOVA result is not significant, Tukey's HSD is usually not required, but it may shed light on particular group comparisons.
" " "

Renewable_Power_EU <-read.csv("/Users/jayantvelichety/Desktop/DataSets/opsd-renewable_power_plants-2020-08-25/renewable_power_plants_EU.csv")
Renewable_Power_EU
sum(is.na(Renewable_Power_EU))
colnames(Renewable_Power_EU)
missing_value <- sapply(Renewable_Power_EU, anyNA)
missing_value
missing_count <- colSums(is.na(Renewable_Power_EU))
missing_count
#Imputing with median and null values
install.packages("dplyr")
library(dplyr)
Renewable_Power_EU_Clean <- Renewable_Power_EU %>% mutate(across(c(lon, lat, as_of_year), ~ ifelse(is.na(.), median(., na.rm = TRUE), .)))
Renewable_Power_EU_Clean
colnames(Renewable_Power_EU_Clean)
sum(is.na(Renewable_Power_EU_Clean))
names(Renewable_Power_EU_Clean)
head(Renewable_Power_EU_Clean)
model <- lm(electrical_capacity ~ lon + lat, data = Renewable_Power_EU_Clean)
model

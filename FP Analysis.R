# Load packages
library(tidyverse)
library(data.table)
library(rstatix)
library(stringr)

#load data 
fp_data = read.csv('FP_Raw_Data.csv')

#Select which columns are wanted 
fp_data = fp_data %>%
  select(participant, mouse.time, mouse.clicked_name, 
         face_file, corr_resp_face, body_file, corr_resp_body)

#Remove NA variables 
fp_data = fp_data %>%
  na.omit()

#Rename variables for clarity
fp_data = fp_data %>%
  rename(rt = mouse.time,
         acc = mouse.clicked_name,
         corr_face = corr_resp_face,
         corr_body = corr_resp_body)

# Convert RTs from seconds to milliseconds
fp_data = fp_data %>%
  mutate(rt = rt*1000)

#Filter out RTs longer than 3,000 ms
fp_data = fp_data %>%
  filter(rt < 3000) 

#Good up to here 
## need to condense from here 

results <- aov(acc ~ corr_face*corr_body + Error(participant/(corr_face*corr_body)))








#Convert characters to variables 
resp_angry = as.numeric(1)
resp_happy = as.numeric(2)
resp_neutral = as.numeric(3)

#Create vectors
vector1 = resp_angry
vector2 = resp_happy
vector3 = resp_neutral

summarize(vector1 = mean(vector1),
          vecor2 = mean(vector2))
mutate(acc = )

str_split_fixed( sample_string, separator_pattern, n)

# Split name column into emotions 
df[c('angry', 'happy', 'neutral')] <- str_split_fixed(df$acc, 'resp', 3)

# Rearrange columns and remove original name column
df <- df[c('angry', 'happy', 'neutral')]

print(" Data frame after splitting: ")
df

# Aggregate accuracy and RT by participant and congruency
fp_data = fp_data %>%
  group_by(participant, corr_face, corr_body) %>%
  summarize(rt = mean(rt),
            acc = mean(acc))

# Aggregate accuracy and RT by participant and subset
fp_condense = fp_data %>%
  group_by(participant, corr_face, corr_body, acc) %>%
  summarize(rt = mean(rt), acc = mean())
          

# Aggregate acc by emotion
flanker_rt_congruency = flanker_congruency_id %>%
  group_by(congruency) %>%
  summarize(mean_rt = mean(rt),
            se_rt = sd(rt)/sqrt(n()))

#Try running a plot to see how it looks 
ggplot(data = fp_naming, 
       aes(x = congruency, 
           y = mean_rt,
           ymin = mean_rt - se_rt,
           ymax = mean_rt + se_rt,
           fill = congruency)) +
geom_bar(stat = 'identity',
         width = .5,
         position = position_dodge()) +
  geom_errorbar(width = .2,
                position = position_dodge(.2))

#Run the analysis
#Run a repeated measures ANOVA on the data 
anova_test(data = fp_data,
           within = c(acc, corr_face, corr_body),
           wid = participant,
           dv = rt)
anova_test(data = reward_data,
           within = c(reward, difficulty),
           wid = id,
           dv = rt)
  
  

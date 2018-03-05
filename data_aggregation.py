# aggregate candidate,vote and political party data into one file for 2002,2008,2013

import os
import pandas as pd
cwd = os.getcwd()

#aggregate candidate file

df_2002=pd.read_csv(cwd+'/2002'+'/NA'+'/candidate_2002.csv')
df_2008=pd.read_csv(cwd+'/2008'+'/NA'+'/canidate_2008.csv')
df_2013=pd.read_csv(cwd+'/2013'+'/NA'+'/candidate_2013.csv')


# aggregate vote file
votes_df_2002=pd.read_csv(cwd+'/2002'+'/NA'+'/votes_2002.csv')
votes_df_2008=pd.read_csv(cwd+'/2008'+'/NA'+'/votes_2008.csv')
votes_df_2013=pd.read_csv(cwd+'/2013'+'/NA'+'/votes_2013.csv')


# aggregate party file
party_df_2002=pd.read_csv(cwd+'/2002'+'/NA'+'/party_2002.csv')
party_df_2008=pd.read_csv(cwd+'/2008'+'/NA'+'/party_2008.csv')
party_df_2013=pd.read_csv(cwd+'/2013'+'/NA'+'/party_2013.csv')

cand = pd.concat([df_2002, df_2008,df_2013], ignore_index=True)
#cand.to_csv('candidate.csv',index=False)

votes = pd.concat([votes_df_2002, votes_df_2008,votes_df_2013], ignore_index=True)
#votes.to_csv('votes.csv',index=False)

party = pd.concat([party_df_2002, party_df_2008,party_df_2013], ignore_index=True)
#party.to_csv('political_party.csv',index=False)
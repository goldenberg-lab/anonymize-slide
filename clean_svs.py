# Clean all SVS files

# Load modules
import os
import numpy as np
import pandas as pd
from funs_support import find_dir_GI

dir_GI = find_dir_GI()
dir_data = os.path.join(dir_GI, 'data')
dir_svs = os.path.join(dir_data, 'svs')
assert os.path.exists(dir_svs)


###########################
# ---- (1) LOAD DATA ---- #

# (i) Get the list of svs files
batch_svs = os.listdir(dir_svs)
holder = []
for batch in batch_svs:
    for mag in ['20X','40X']:
        (batch, mag)
        path_mag = os.path.join(dir_svs, batch, mag)
        fn_mag = pd.Series(os.listdir(path_mag))
        tmp_df = pd.DataFrame({'batch':batch, 'mag':mag, 'fn':fn_mag})
        holder.append(tmp_df)
df_svs = pd.concat(holder).reset_index(drop=True)
df_svs['idt'] = df_svs['fn'].str.split('\\s',1,True)[0]
assert np.all(df_svs.groupby(['mag','idt']).size() == 1)

# Patients to igore
idt_drop = ['S15-981', 'S16-3714', 'S17-1100', 'S17-1545']
df_svs = df_svs[~df_svs['idt'].isin(idt_drop)]

# (ii) Compare to svs file
df_jazz = pd.read_csv(os.path.join(dir_data,'UC_TO_ED_MRN_files.csv'))
idt_keep = df_jazz['Accession_No'].dropna().unique()
u_idt = df_svs['idt'].unique()
assert len(np.setdiff1d(idt_keep,u_idt)) == 0
df_svs = df_svs[df_svs['idt'].isin(idt_keep)]
df_svs.reset_index(drop=True, inplace=True)


#################################
# ---- (2) LOOP OVER FILES ---- #

for ii, rr in df_svs.iterrows():
    batch, fn, mag, idt = rr['batch'], rr['fn'], rr['mag'], rr['idt']
    print('File: %s (iteration %i of %i)' % (fn, ii+1, len(df_svs)))
    break
import psrc_urbansim.models
import orca
orca.run([
    "repm_simulate",              # REPM
    #"nrh_simulate",              # non-residential rent hedonic

    #"households_relocation",     # households relocation model
    #"hlcm_simulate",            # households location choice
    #"households_transition",     # households transition

    #"jobs_relocation",           # jobs relocation model
    #"elcm_simulate",             # employment location choice
    #"jobs_transition",           # jobs transition

    #"feasibility",               # compute development feasibility
    #"residential_developer",     # build residential buildings
    #"non_residential_developer", # build non-residential buildings
], iter_vars=[2015, 2016], data_out="simresult.h5")
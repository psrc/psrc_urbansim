import psrc_urbansim.models
import orca
import logging
import psrc_urbansim.vars.variables_interactions
import psrc_urbansim.vars.variables_generic

logging.basicConfig(level=logging.INFO)

orca.run([
#    "repmres_simulate",           # residential REPM
#    "repmnr_simulate",            # non-residential REPM

    "households_transition",     # households transition
    "households_relocation",     # households relocation model
    #"hlcm_simulate",              # households location choice

    "jobs_transition",           # jobs transition
    "jobs_relocation",           # jobs relocation model
#    "elcm_simulate",             # employment location choice
    "governmental_jobs_scaling"

], iter_vars=[2015], data_out="simresult.h5")

logging.info('Simulation finished')
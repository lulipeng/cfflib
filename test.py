from cfflib import *

a = load_from_cff('/home/stephan/Dev/PyWorkspace/cfflib/datasets/ds1/c.cff')

w=a.get_all()[0]
w.load()
w.save() 

save('test.cff', a)


#a = load_from_cff('datasets/meta.cff')
#a = load_from_metaxml('datasets/meta.xml')

#myvol = a.get_by_name('T1-weighted single subject')[0]
#myvol.load()
#print myvol.content

#mynetwork = a.get_by_name('Network Lausanne83')[0]
#mynetwork.load()
#print mynetwork.content

#surf = a.get_by_name('Individual surfaces')[0]
#surf.load()
#print surf.content

#trk = a.get_by_name('Tractography')[0]
#trk.load()

#hdf = a.get_by_name('Generated timeseries data')[0]
#hdf.load()

#dat = a.get_by_name('Arbitrary data file')[0]
#dat.load()

#scr = a.get_by_name('Analysis Script MMXXXIV')[0]
#scr.load()

#stk = a.get_by_name('Planar anatomical segmentation')[0]
#stk.load()
#print stk.content

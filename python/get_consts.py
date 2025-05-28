from pathlib import Path
import h5py

data_dir = '../data/sim_data/aspenexg/viz/'
h5f = h5py.File(data_dir / Path('comms_out.h5'),'r')
out_alpha = h5f['out_alpha'][...]
Nr = h5f['Nr'][()]
Nt = h5f['Nt'][()]
diff = h5f['diff'][()]
h5f.close()

#get some sim constants (floats) from sim_consts
h5f = h5py.File(data_dir / Path('sim_consts.h5'),'r')
Ts = h5f['Ts'][()]
c = h5f['c'][()]
Tc = h5f['Tc'][()]
rh = h5f['rh'][()]

print(f"out_alpha: {out_alpha}")
print(f"Nr: {Nr}")
print(f"Nt: {Nt}")
print(f"diff: {diff}")

print(f"Ts: {Ts}")
print(f"c: {c}")
print(f"Tc: {Tc}")
print(f"rh: {rh}")

h5f.close()

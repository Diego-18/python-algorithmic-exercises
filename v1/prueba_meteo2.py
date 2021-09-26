from meteo import Meteo, mostrar_meteo

cs = Meteo(estacion='CS1', temp=[20.2, 19.1, 27.2, 24.8], lluvia=[0, 0, 0, 0])
vr = Meteo(estacion='VR1', temp=cs.temp[:], lluvia=cs.lluvia[:])
mostrar_meteo(cs)
mostrar_meteo(vr)

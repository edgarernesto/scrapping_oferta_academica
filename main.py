from oferta import Oferta

inco = Oferta()
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
inco.carrera = 'INCO'
inco.scrapping(url)
inco.to_json()

inni = Oferta()
url= 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
inni.carrera = 'INNI'
inni.scrapping(url)
inni.to_json()

inro = Oferta()
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
inro.carrera = 'INRO'
inro.scrapping(url)
inro.to_json()

ince = Oferta()
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
ince.carrera = 'INCE'
ince.scrapping(url)
ince.to_json()

inbi = Oferta()
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
inbi.carrera = 'INBI'
inbi.scrapping(url)
inbi.to_json()

igfo = Oferta()
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
igfo.carrera = 'IGFO'
igfo.scrapping(url)
igfo.to_json()
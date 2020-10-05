from os import path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager,SwapTransition
from kivy.config import Config
import engine
import datetime 

Config.set('graphics', 'resizable', '0')
kvdir=path.join('Kv')

Builder.load_file(path.join(kvdir,"main.kv"))
class inicio(Screen):
    def ir(self):
        self.parent.current='registro'
    def info(self):
        self.parent.current='update'
    def moni(self):
        self.parent.current='monitoreo'
class registro(Screen):
    def salvar(self): 
        fecha=f"{self.year.text}-{self.mes.text}-{self.dia.text}"
        nombre = self.nombre.text.upper()
        altura = self.altura.text
        sexo = self.sexo.text.upper()
        peso = self.peso.text
        if (self.nombre.text!=' ' or self.nombre.text!=' ' or self.altura.text!=' ' or self.sexo.text!=' ' or self.peso.text!=' ' or fecha=="--"):

            engine.datos(nombre,fecha,sexo,peso,altura)
            self.parent.current='inicio'
            self.mes.text=''
            self.dia.text=''
            self.year.text=''
            self.nombre.text=''
            self.sexo.text=''
            self.altura.text=''
            self.peso.text=''

        else:
            self.parent.current='inicio'
            self.mes.text=''
            self.dia.text=''
            self.year.text=''
            self.nombre.text=''
            self.sexo.text=''
            self.altura.text=''
            self.peso.text=''


class update(Screen):
    def actualiza(self):
        masa= self.masa.text
        wrist=self.wrist.text
        nombre=self.nombre.text.upper()
        knee=self.knee.text
        if masa!=' ' or wrist!=' ' or nombre!=' ' or knee!=' ':
            info=engine.get_data([nombre])
            fdn=info[1].split("-")
            if info[2]=="M":
                knee=float(knee)/100
                wrist=float(wrist)/100
                MR=float(masa)*.241
                MO=3.02* pow( (
                    pow((float(info[3])/100),2) 
                    * (float(wrist)) * (float(knee)) *400),.712)
                
                # MO=3.02*pow( pow( (float(info[3]))/100),2)*(float(wrist)/100)* (float(knee)/100) *400 ),.712))
                imc=int(masa)/pow((float(info[3])/100),2)

                fdn = datetime.date(int(fdn[0]), int(fdn[1]),int(fdn[2]) )
                year=datetime.date.today()-fdn
                year=year.days/365.5
                MG=(1.2*imc)+(.23*year)-16.7
                MM=int(masa)-(MO+MR+MG)
            else:
                MR=float(masa)*.209
                MO=3.02* pow( (
                    pow((float(info[3])/100),2) 
                    * (float(wrist)) * (float(knee)) *400),.712)
                    
                imc=int(masa)/pow((float(info[3])/100),2)
                fdn = datetime.date(int(fdn[0]), int(fdn[1]),int(fdn[2]) )
                year=datetime.date.today()-fdn
                year=year.days/365.5
                MG=(1.2*imc)+(.23*year)-5.4
                MM=int(masa)-(MO+MR+MG)

            data=[datetime.datetime.today(),MO,MM,MG,masa,info[0]]
            engine.week(data)

            self.parent.current='inicio'
            self.wrist.text=''
            self.masa.text=''
            self.nombre.text=''
            self.knee.text=''
        else :
            self.parent.current='inicio'
            self.wrist.text=''
            self.masa.text=''
            self.nombre.text=''
            self.knee.text=''

class monitoreo(Screen):
    def atras(self):
        self.parent.current='inicio'
        self.nombre.text=''
        self.monito.text=''
    def my_data(self):
        if len(self.nombre.text)>5:
            nombre=self.nombre.text.upper()
            data = engine.data(nombre)
            # if data:
            #     self.monito.text=data
            # except:
            #     self.parent.current='inicio'
            #     self.nombre.text=''
            #     self.monito.text=''
        else:
            self.parent.current='inicio'
            self.nombre.text=''
            self.monito.text=''


manager = ScreenManager(transition=SwapTransition())

manager.add_widget(inicio(name='inicio'))
manager.add_widget(registro(name='registro'))
manager.add_widget(update(name='update'))
manager.add_widget(monitoreo(name='monitoreo'))
class Palfa(App):
    def build(self):
        return manager

if __name__ == "__main__":
    Palfa().run()
    
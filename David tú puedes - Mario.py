from tkinter import *
ventana = Tk()


## La función iniciar2 tendra en su interior los diferentes botones que aparacen en la ventana inicial y
## además estan definidas las barras donde se ingresan los nombres de los jugadores. 5
def iniciar2 ():
    global Bot,Bot2,txtmario,txtluigi,entrada,entradal
    Bot.destroy ()
    Bot2.destroy ()
    Botlvl1= Button(ventana,image=lvl1,command=iniciar)
    Botlvl1.place(x=350,y=430)
    Botlvl2= Button(ventana,image=lvl2,command=iniciar3)
    Botlvl2.place(x=450,y=430)
    Botlvl3= Button(ventana,image=lvl3,command=iniciar4)
    Botlvl3.place(x=550,y=430)
    Botlvl4= Button(ventana,image=lvl4,command=iniciar5)
    Botlvl4.place(x=650,y=430)
    Botlvl5= Button(ventana,image=lvl5,command=iniciar6)
    Botlvl5.place(x=750,y=430)
    Botpar=Button(ventana,image=guardar,command=guardar_puntajes)
    Botpar.place(x=950,y=500)
    entrada=StringVar()
    entradal=StringVar()
    entrada.set("MARIO")
    entradal.set("LUIGI")
    txtmario=Entry(ventana,textvariable=entrada).place(x=400,y=600)
    txtluigi=Entry(ventana,textvariable=entradal).place(x=700,y=650)
    LblLuigi=Label(text="MARIO",font=("Super Mario Bros.",20),bg="saddle brown",fg="black").place(x=550,y=600)
    LblMario=Label(text="LUIGI",font=("Super Mario Bros.",20),bg="green",fg="black").place(x=850,y=650)
    Lblnueva=Label(text="MARIO DEBES SALVAR A LUIGI DE LLEGAR A -250 PUNTOS",font=("Super Mario Bros.",20),bg="Indian Red",fg="black").place(x=200,y=15)
## La funcion iniciar da el inicio al juego siendo ejecutada por medio de un boton en la pantalla inicial.
## Esta funcion crea el canvas donde el juego tendra sus diferentes interacciones.
def iniciar():
    global c,mario2,luigi,Bot,Bot2,el,muerte,vidam2,muertel,bo
    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel,puntosl,puntl
    puntosm=0
    puntosl=0
    vel=17
    muerte=5
    muertel=5
    ventan2=Toplevel()
    ventan2.title("Mario & Luigi")
    ventan2.geometry("1280x720")
    c=Canvas(ventan2, height=720,width=1280)
    mapa=PhotoImage(file="mapa.gif") ## Imagen del mapa donde se ejecuará el juego.
    c.create_image(0,0, anchor=NW, image=mapa)
    vidam2=c.create_image(250,60,image=vidam)
    vidal2=c.create_image(1050,60,image=vidal)
    fantasm=c.create_image(1212,301,image=fantasma)
    planta=c.create_image(85,340,image=pl)
    pl3=c.create_image(1135,500,image=pl2)
    pl4=c.create_image(1150,500,image=pl2)
    pl5=c.create_image(1165,500,image=pl2)
    pl6=c.create_image(1180,500,image=pl2)
    pl7=c.create_image(1195,500,image=pl2)
    pl8=c.create_image(1210,500,image=pl2)
    pl9=c.create_image(1225,500,image=pl2)
    pl10=c.create_image(1240,500,image=pl2)
    torre=c.create_image(250,475,image=tor)
    ## Se crearán labels con el fin de poner los nombres de los jugadores, la imagen que define la vida y el puntaje que el jugador lleve.
    labelmario= Label(ventan2,text=entrada.get(),height=3,width=10,bg="black",fg="saddle brown",font=("Super Mario Bros.",20)).place (x=350,y=10)
    puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
    puntma.place (x=50,y=10)
    puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
    puntl.place (x=1100,y=10)
    labelluigi= Label(ventan2,text=entradal.get(),height=3,width=10,bg="black",fg="green",font=("Super Mario Bros.",20)).place (x=800,y=10)
    ## Se ingresan las diferentes formas y/o figuras que se verán en el juego.
    mario2=c.create_image(260,640, image=mariodere)  
    luigi=c.create_image(900,640, image=luigiizq)
    enemigo1=c.create_image(1018,190,image=enemigo)
    enemigo2=c.create_image(300,190,image=enemigorojo)
    torgran1=c.create_image(800,360,image=torgran)
    mosca1=c.create_image(1020,190,image=mosca)
    muerto=c.create_image(3000,3000,image=capver)
    muertor=c.create_image(3000,3000,image=caprojo)
    el=c.create_image(400,360,image=elmat)
    bo=c.create_image(600,360,image=bom)
    c.focus_set()
    ## Al canvas se le definen algunas letras en especifico para que por medio de ellas, las
    ## funciones se pongan en acción.
    c.bind("<A>",movimiento)
    c.bind("<a>",movimiento)
    c.bind("<d>",movimiento)
    c.bind("<D>",movimiento)
    c.bind("<w>",movimiento)
    c.bind("<W>",movimiento)
    c.bind("<Key>",movimientoluigi)
    c.pack()
    ## La creación de coordenadas para paltaformas facilita la manera en que la fisica
    ## se ve reflejada en los objetos que van a sufrir de choques o cambios durante el juego.
    ## Los numeros dentro de las listas indican la coordenada que se toma, en este caso:
    ## 0 : x1
    ## 1 : y1
    ## 2 : x2
    ## 3 : y2
    movimientotortuga ()
    movimientotortuga2 ()
    movimientotorgran ()
    movimientodelraro ()
    movimientobomba ()
    fin ()
    c.mainloop()
def iniciar3():
    global c,mario2,luigi,Bot,Bot2,el,muerte,muertel,bo
    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel,puntosl,puntl
    puntosm=0
    puntosl=0
    vel=15
    muerte=5
    muertel=5
    ventan2=Toplevel()
    ventan2.title("Mario & Luigi")
    ventan2.geometry("1280x720")
    c=Canvas(ventan2, height=720,width=1280)
    mapa=PhotoImage(file="mapa.gif") ## Imagen del mapa donde se ejecuará el juego.
    c.create_image(0,0, anchor=NW, image=mapa)
    vidam2=c.create_image(250,60,image=vidam)
    vidal2=c.create_image(1050,60,image=vidal)
    fantasm=c.create_image(1212,301,image=fantasma)
    planta=c.create_image(85,340,image=pl)
    pl3=c.create_image(1135,500,image=pl2)
    pl4=c.create_image(1150,500,image=pl2)
    pl5=c.create_image(1165,500,image=pl2)
    pl6=c.create_image(1180,500,image=pl2)
    pl7=c.create_image(1195,500,image=pl2)
    pl8=c.create_image(1210,500,image=pl2)
    pl9=c.create_image(1225,500,image=pl2)
    pl10=c.create_image(1240,500,image=pl2)
    torre=c.create_image(250,475,image=tor)
    ## Se crearán labels con el fin de poner los nombres de los jugadores, la imagen que define la vida y el puntaje que el jugador lleve.
    labelmario= Label(ventan2,text=entrada.get(),height=3,width=10,bg="black",fg="saddle brown",font=("Super Mario Bros.",20)).place (x=350,y=10)
    puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
    puntma.place (x=50,y=10)
    puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
    puntl.place (x=1100,y=10)
    labelluigi= Label(ventan2,text=entradal.get(),height=3,width=10,bg="black",fg="green",font=("Super Mario Bros.",20)).place (x=800,y=10)
    ## Se ingresan las diferentes formas y/o figuras que se verán en el juego.
    mario2=c.create_image(260,640, image=mariodere)  
    luigi=c.create_image(900,640, image=luigiizq)
    enemigo1=c.create_image(1018,190,image=enemigo)
    enemigo2=c.create_image(300,190,image=enemigorojo)
    torgran1=c.create_image(800,360,image=torgran)
    mosca1=c.create_image(1020,190,image=mosca)
    muerto=c.create_image(3000,3000,image=capver)
    muertor=c.create_image(3000,3000,image=caprojo)
    el=c.create_image(400,360,image=elmat)
    bo=c.create_image(600,360,image=bom)
    c.focus_set()
    ## Al canvas se le definen algunas letras en especifico para que por medio de ellas, las
    ## funciones se pongan en acción.
    c.bind("<A>",movimiento)
    c.bind("<a>",movimiento)
    c.bind("<d>",movimiento)
    c.bind("<D>",movimiento)
    c.bind("<w>",movimiento)
    c.bind("<W>",movimiento)
    c.bind("<Key>",movimientoluigi)
    c.pack()
    ## La creación de coordenadas para paltaformas facilita la manera en que la fisica
    ## se ve reflejada en los objetos que van a sufrir de choques o cambios durante el juego.
    ## Los numeros dentro de las listas indican la coordenada que se toma, en este caso:
    ## 0 : x1
    ## 1 : y1
    ## 2 : x2
    ## 3 : y2
    movimientotortuga ()
    movimientotortuga2 ()
    movimientotorgran ()
    movimientodelraro ()
    movimientobomba ()
    fin ()
    c.mainloop()

def iniciar4():
    global c,mario2,luigi,Bot,Bot2,el,muerte,muertel,bo
    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel,puntosl,puntl
    puntosm=0
    puntosl=0
    vel=10
    muerte=5
    muertel=5
    ventan2=Toplevel()
    ventan2.title("Mario & Luigi")
    ventan2.geometry("1280x720")
    c=Canvas(ventan2, height=720,width=1280)
    mapa=PhotoImage(file="mapa.gif") ## Imagen del mapa donde se ejecuará el juego.
    c.create_image(0,0, anchor=NW, image=mapa)
    vidam2=c.create_image(250,60,image=vidam)
    vidal2=c.create_image(1050,60,image=vidal)
    fantasm=c.create_image(1212,301,image=fantasma)
    planta=c.create_image(85,340,image=pl)
    pl3=c.create_image(1135,500,image=pl2)
    pl4=c.create_image(1150,500,image=pl2)
    pl5=c.create_image(1165,500,image=pl2)
    pl6=c.create_image(1180,500,image=pl2)
    pl7=c.create_image(1195,500,image=pl2)
    pl8=c.create_image(1210,500,image=pl2)
    pl9=c.create_image(1225,500,image=pl2)
    pl10=c.create_image(1240,500,image=pl2)
    torre=c.create_image(250,475,image=tor)
    ## Se crearán labels con el fin de poner los nombres de los jugadores, la imagen que define la vida y el puntaje que el jugador lleve.
    labelmario= Label(ventan2,text=entrada.get(),height=3,width=10,bg="black",fg="saddle brown",font=("Super Mario Bros.",20)).place (x=350,y=10)
    puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
    puntma.place (x=50,y=10)
    puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
    puntl.place (x=1100,y=10)
    labelluigi= Label(ventan2,text=entradal.get(),height=3,width=10,bg="black",fg="green",font=("Super Mario Bros.",20)).place (x=800,y=10)
    ## Se ingresan las diferentes formas y/o figuras que se verán en el juego.
    mario2=c.create_image(260,640, image=mariodere)  
    luigi=c.create_image(900,640, image=luigiizq)
    enemigo1=c.create_image(1018,190,image=enemigo)
    enemigo2=c.create_image(300,190,image=enemigorojo)
    torgran1=c.create_image(800,360,image=torgran)
    mosca1=c.create_image(1020,190,image=mosca)
    muerto=c.create_image(3000,3000,image=capver)
    muertor=c.create_image(3000,3000,image=caprojo)
    el=c.create_image(400,360,image=elmat)
    bo=c.create_image(600,360,image=bom)
    c.focus_set()
    ## Al canvas se le definen algunas letras en especifico para que por medio de ellas, las
    ## funciones se pongan en acción.
    c.bind("<A>",movimiento)
    c.bind("<a>",movimiento)
    c.bind("<d>",movimiento)
    c.bind("<D>",movimiento)
    c.bind("<w>",movimiento)
    c.bind("<W>",movimiento)
    c.bind("<Key>",movimientoluigi)
    c.pack()
    ## La creación de coordenadas para paltaformas facilita la manera en que la fisica
    ## se ve reflejada en los objetos que van a sufrir de choques o cambios durante el juego.
    ## Los numeros dentro de las listas indican la coordenada que se toma, en este caso:
    ## 0 : x1
    ## 1 : y1
    ## 2 : x2
    ## 3 : y2
    movimientotortuga ()
    movimientotortuga2 ()
    movimientotorgran ()
    movimientodelraro ()
    movimientobomba ()
    c.mainloop()

def iniciar5():
    global c,mario2,luigi,Bot,Bot2,el,muerte,muertel,bo
    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel,puntosl,puntl
    puntosm=0
    puntosl=0
    vel=7
    muerte=5
    muertel=5
    ventan2=Toplevel()
    ventan2.title("Mario & Luigi")
    ventan2.geometry("1280x720")
    c=Canvas(ventan2, height=720,width=1280)
    mapa=PhotoImage(file="mapa.gif") ## Imagen del mapa donde se ejecuará el juego.
    c.create_image(0,0, anchor=NW, image=mapa)
    vidam2=c.create_image(250,60,image=vidam)
    vidal2=c.create_image(1050,60,image=vidal)
    fantasm=c.create_image(1212,301,image=fantasma)
    planta=c.create_image(85,340,image=pl)
    pl3=c.create_image(1135,500,image=pl2)
    pl4=c.create_image(1150,500,image=pl2)
    pl5=c.create_image(1165,500,image=pl2)
    pl6=c.create_image(1180,500,image=pl2)
    pl7=c.create_image(1195,500,image=pl2)
    pl8=c.create_image(1210,500,image=pl2)
    pl9=c.create_image(1225,500,image=pl2)
    pl10=c.create_image(1240,500,image=pl2)
    torre=c.create_image(250,475,image=tor)
    ## Se crearán labels con el fin de poner los nombres de los jugadores, la imagen que define la vida y el puntaje que el jugador lleve.
    labelmario= Label(ventan2,text=entrada.get(),height=3,width=10,bg="black",fg="saddle brown",font=("Super Mario Bros.",20)).place (x=350,y=10)
    puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
    puntma.place (x=50,y=10)
    puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
    puntl.place (x=1100,y=10)
    labelluigi= Label(ventan2,text=entradal.get(),height=3,width=10,bg="black",fg="green",font=("Super Mario Bros.",20)).place (x=800,y=10)
    ## Se ingresan las diferentes formas y/o figuras que se verán en el juego.
    mario2=c.create_image(260,640, image=mariodere)  
    luigi=c.create_image(900,640, image=luigiizq)
    enemigo1=c.create_image(1018,190,image=enemigo)
    enemigo2=c.create_image(300,190,image=enemigorojo)
    torgran1=c.create_image(800,360,image=torgran)
    mosca1=c.create_image(1020,190,image=mosca)
    muerto=c.create_image(3000,3000,image=capver)
    muertor=c.create_image(3000,3000,image=caprojo)
    el=c.create_image(400,360,image=elmat)
    bo=c.create_image(600,360,image=bom)
    c.focus_set()
    ## Al canvas se le definen algunas letras en especifico para que por medio de ellas, las
    ## funciones se pongan en acción.
    c.bind("<A>",movimiento)
    c.bind("<a>",movimiento)
    c.bind("<d>",movimiento)
    c.bind("<D>",movimiento)
    c.bind("<w>",movimiento)
    c.bind("<W>",movimiento)
    c.bind("<Key>",movimientoluigi)
    c.pack()
    ## La creación de coordenadas para paltaformas facilita la manera en que la fisica
    ## se ve reflejada en los objetos que van a sufrir de choques o cambios durante el juego.
    ## Los numeros dentro de las listas indican la coordenada que se toma, en este caso:
    ## 0 : x1
    ## 1 : y1
    ## 2 : x2
    ## 3 : y2
    movimientotortuga ()
    movimientotortuga2 ()
    movimientotorgran ()
    movimientobomba ()
    fin ()
    c.mainloop()
def iniciar6():
    global c,mario2,luigi,Bot,Bot2,el,muerte,muertel,bo
    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel,puntosl,puntl
    puntosm=0
    puntosl=0
    vel=5
    muerte=5
    muertel=5
    ventan2=Toplevel()
    ventan2.title("Mario & Luigi")
    ventan2.geometry("1280x720")
    c=Canvas(ventan2, height=720,width=1280)
    mapa=PhotoImage(file="mapa.gif") ## Imagen del mapa donde se ejecuará el juego.
    c.create_image(0,0, anchor=NW, image=mapa)
    vidam2=c.create_image(250,60,image=vidam)
    vidal2=c.create_image(1050,60,image=vidal)
    fantasm=c.create_image(1212,301,image=fantasma)
    planta=c.create_image(85,340,image=pl)
    pl3=c.create_image(1135,500,image=pl2)
    pl4=c.create_image(1150,500,image=pl2)
    pl5=c.create_image(1165,500,image=pl2)
    pl6=c.create_image(1180,500,image=pl2)
    pl7=c.create_image(1195,500,image=pl2)
    pl8=c.create_image(1210,500,image=pl2)
    pl9=c.create_image(1225,500,image=pl2)
    pl10=c.create_image(1240,500,image=pl2)
    torre=c.create_image(250,475,image=tor)
    ## Se crearán labels con el fin de poner los nombres de los jugadores, la imagen que define la vida y el puntaje que el jugador lleve.
    labelmario= Label(ventan2,text=entrada.get(),height=3,width=10,bg="black",fg="saddle brown",font=("Super Mario Bros.",20)).place (x=350,y=10)
    puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
    puntma.place (x=50,y=10)
    puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
    puntl.place (x=1100,y=10)
    labelluigi= Label(ventan2,text=entradal.get(),height=3,width=10,bg="black",fg="green",font=("Super Mario Bros.",20)).place (x=800,y=10)
    ## Se ingresan las diferentes formas y/o figuras que se verán en el juego.
    mario2=c.create_image(260,640, image=mariodere)  
    luigi=c.create_image(900,640, image=luigiizq)
    enemigo1=c.create_image(1018,190,image=enemigo)
    enemigo2=c.create_image(300,190,image=enemigorojo)
    torgran1=c.create_image(800,360,image=torgran)
    mosca1=c.create_image(1020,190,image=mosca)
    muerto=c.create_image(3000,3000,image=capver)
    muertor=c.create_image(3000,3000,image=caprojo)
    el=c.create_image(400,360,image=elmat)
    bo=c.create_image(600,360,image=bom)
    c.focus_set()
    ## Al canvas se le definen algunas letras en especifico para que por medio de ellas, las
    ## funciones se pongan en acción.
    c.bind("<A>",movimiento)
    c.bind("<a>",movimiento)
    c.bind("<d>",movimiento)
    c.bind("<D>",movimiento)
    c.bind("<w>",movimiento)
    c.bind("<W>",movimiento)
    c.bind("<Key>",movimientoluigi)
    c.pack()
    ## La creación de coordenadas para paltaformas facilita la manera en que la fisica
    ## se ve reflejada en los objetos que van a sufrir de choques o cambios durante el juego.
    ## Los numeros dentro de las listas indican la coordenada que se toma, en este caso:
    ## 0 : x1
    ## 1 : y1
    ## 2 : x2
    ## 3 : y2
    movimientotortuga ()
    movimientotortuga2 ()
    movimientotorgran ()
    movimientodelraro ()
    movimientobomba ()
    fin ()
    c.mainloop()

## En la función movimiento lo que se hará es definir los estados que va a tener el mario, este puede
## tomar un estado hacia el lado derecho o hacia el lado izquierdo. Esto depende de la tecla que se le oprima.
## Para ello, "event" proporciona la capacidad de poder tomar la tecla que se le este siendo oprimida y la use para generar
## una serie de acciones y condiciones dependiendo de la ubicación del jugador.
def movimiento (event):
    global c,mario2,estadomario,tec,boo,enemigo1
    x=int(c.coords(mario2)[0])
    y=int(c.coords(mario2)[1])
    tec = repr(event.char)
    ## Al oprimir "d" o "D", el estado de mario será hacia el lado derecho.
    if(tec=="'d'") or (tec=="'D'"):
            p1=c.coords(mario2)
            c.delete(mario2)
            mario2=c.create_image(x,y, image=mariodere)
            estadomario="derecha"
            c.move(mario2,10,0)
            if (c.coords(mario2)[0]>1280):
                c.coords(mario2,10,int(c.coords(mario2)[1]))
            if (c.coords(mario2)[1]==490)and (c.coords(mario2)[0]>=480 and c.coords(mario2)[0]<=799):
                caida ()
            if (c.coords(mario2)[1]==360)and (c.coords(mario2)[0]>=160 and c.coords(mario2)[0]<=320):
                caida ()
            if (c.coords(mario2)[1]==360)and (c.coords(mario2)[0]>=963 and c.coords(mario2)[0]<=1120):
                caida ()
            if (c.coords(mario2)[1]==180)and (c.coords(mario2)[0]>=561 and c.coords(mario2)[0]<=720):
                caida ()
            if(max(c.coords(mario2)[0],c.coords(enemigo1)[0])-min(c.coords(mario2)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(mario2)[1],c.coords(enemigo1)[1])-min(c.coords(mario2)[1],c.coords(enemigo1)[1])<=20):
                c.delete(mario2)
                respawn ()
    ## Al oprimir "a" o "A", el estado de mario será hacia el lado izquierdo.
    if(tec=="'a'") or (tec=="'A'"):
            p1=c.coords(mario2)
            c.delete(mario2)
            mario2=c.create_image(x,y, image=marioizq)
            estadomario="izquierda"
            c.move(mario2,-10,0)
            if (c.coords(mario2)[0]<0):
                c.coords(mario2,1270,int(c.coords(mario2)[1]))
            if (c.coords(mario2)[1]==490)and (c.coords(mario2)[0]>=480 and c.coords(mario2)[0]<=799):
                caida ()
            if (c.coords(mario2)[1]==360)and (c.coords(mario2)[0]>=160 and c.coords(mario2)[0]<=320):
                caida ()
            if (c.coords(mario2)[1]==360)and (c.coords(mario2)[0]>=963 and c.coords(mario2)[0]<=1120):
                caida ()
            if (c.coords(mario2)[1]==180)and (c.coords(mario2)[0]>=561 and c.coords(mario2)[0]<=720):
                caida ()
            if(max(c.coords(mario2)[0],c.coords(enemigo1)[0])-min(c.coords(mario2)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(mario2)[1],c.coords(enemigo1)[1])-min(c.coords(mario2)[1],c.coords(enemigo1)[1])<=20):
                c.delete(mario2)
                respawn ()
    ## Al oprimir la tecla "w" o "W" un valor booleano tomará un diferente valor y se llamará a la función
    ## para lograr que mario salte.
    if ((tec=="'w'") or (tec=="'W'")) and (boo==False):
            boo=True
            saltar()


## En esta instancia del codigo, la funcion saltar resivirá dor valores que serán definidos fuera de
## ella, estos son:      
lim=-1
boo=False
## Con el lim se difinirá la distancia que podrá saltar el mario en funcion del eje "y".
## Con boo se logrará que al dejar oprimida la tecla "w" o "W" el mario no tenga un error y se salga 
## del mapa consiguiendo que el juego colapse.
def saltar ():
    global c,mario2,estadomario,lim,ventan2,boo,vel
    lim=0
    ## En este punto lo que se hará es crear dos condicionales base para que el salto
    ## de mario se logre limpio y con la imagen correspondiente a su estado.
    ## Cuando el estado de mario es hacia el lado derecho, se creará una imagen de salto mirando hacia el lado derecho.
    if estadomario=="derecha":
    	## Ya dentro de la condición se darán dos ciclos, en mi caso decidi hacerlos con while 
    	## y un contador que ya estaba definido, llamado lim.
    	## El primer ciclo moverá y creará la imagen de mario de salto hacia la derecha para que se 
    	## vea el salto limpio.
        while lim <=65:
            x=int(c.coords(mario2)[0])
            y=int(c.coords(mario2)[1])
            c.delete(mario2)
            mario2=c.create_image(x,y, image=mariosaltoder)
            c.move(mario2,0,-10)
            c.update ()
            ventan2.after (20)
            ## Las siguientes condiciones haran que el ciclo se acabe.
            ## Esto sucede cuando el mario está debajo de una plataforma el ciclo se acabe y se genere el ciclo de caida.
            if (y==560) and not(x>=480 and x<799):
                break
            elif (y==420) and (x>=0 and x<160):
                break
            elif (y==420) and (x>=320 and x<963):
                break
            elif (y==420) and (x>=1120 and x<1280):
                break
            elif (y==260) and (x>=0 and x<561):
                break
            elif (y==260) and (x>=720 and x<1280):
                break
            elif (y==140):
                break
            elif (y==600) and (x>=600 and x<680):
                break
                vel=17
            lim+=1
        lim=0
        ## El segundo ciclo moverá y creara la imagen de mario de caida hacia la derecha para que se 
    	## vea que al llegar al suelo cae parado y no con una imagen de salto.
        while lim <=65:
            x=int(c.coords(mario2)[0])
            y=int(c.coords(mario2)[1])
            c.delete(mario2)
            mario2=c.create_image(x,y, image=mariodere)
            c.move(mario2,0,10)
            c.update ()
            ventan2.after (20)
            ## Las siguientes condiciones provocarán que el mario cuando esta saltando, 
            ## y no se encuentre debajo de una plataforma pueda llegar hasta el suelo sin
            ## que se quede volando.
            if (y==630)or (y==480)and not(x>=480 and x<799):
                break
            elif (y==350) and (x>=0 and x<160):
                break
            elif (y==350) and (x>=320 and x<963):
                break
            elif (y==350) and (x>=1120 and x<1280):
                break
            elif (y==170) and (x>=0 and x<561):
                break
            elif (y==170) and (x>=720 and x<1280):
                break
            elif (y==480)and (x>=600 and x<680):
                break
            lim+=1
    ## Cuando el estado de mario es hacia el lado izquierdo, se creará una imagen de salto mirando hacia el lado izquierdo.
    elif estadomario=="izquierda":
    	## El primer ciclo moverá y creará la imagen de mario de salto hacia la izquierda para que se 
    	## vea el salto limpio.
        while lim <=65:
            x=int(c.coords(mario2)[0])
            y=int(c.coords(mario2)[1])
            c.delete(mario2)
            mario2=c.create_image(x,y, image=mariosaltoizq)
            c.move(mario2,0,-10)
            c.update ()
            ventan2.after (20)
            ## Las siguientes condiciones haran que el ciclo se acabe.
            ## Esto sucede cuando el mario está debajo de una plataforma el ciclo se acabe y se genere el ciclo de caida.
            if (y==560)and not(x>=480 and x<799):
                break
            elif (y==420) and (x>=0 and x<160):
                break
            elif (y==420) and (x>=320 and x<963):
                break
            elif (y==420) and (x>=1120 and x<1280):
                break
            elif (y==260) and (x>=0 and x<561):
                break
            elif (y==260) and (x>=720 and x<1280):
                break
            elif (y==140):
                break
            elif (y==600)and (x>=600 and x<680):
                break
                vel=17
            lim+=1
        lim=0
        ## El segundo ciclo moverá y creara la imagen de mario de caida hacia la izquierda para que se 
    	## vea que al llegar al suelo cae parado y no con una imagen de salto.
        while lim <=65:
            x=int(c.coords(mario2)[0])
            y=int(c.coords(mario2)[1])
            c.delete(mario2)
            mario2=c.create_image(x,y, image=marioizq)
            c.move(mario2,0,10)
            c.update ()
            ventan2.after (20)
            ## Las siguientes condiciones provocarán que el mario cuando esta saltando, 
            ## y no se encuentre debajo de una plataforma pueda llegar hasta el suelo sin
            ## que se quede volando.
            if (y==630) or (y==480)and not(x>480 and x<799):
                break
            elif (y==350) and (x>=0 and x<160):
                break
            elif (y==350) and (x>=320 and x<963):
                break
            elif (y==350) and (x>=1120 and x<1280):
                break
            elif (y==170) and (x>=0 and x<561):
                break
            elif (y==170) and (x>=720 and x<1280):
                break
            elif (y==480)and (x>=600 and x<680):
                break
            lim+=1
    lim-=1
    boo=False

## En la siguientes función se logrará que el mario cuando este sobre una plataforma y desee bajar 
## al piso inferior pueda lograrlo sin dificultad alguna.
def caida ():
    global c,mario2,estadomario,lim,ventan2
    ## Al igual que en la función de salto, se hará uso de dos condicionales segun el estado de mario.
    ## Dentro de cada condicion se hará un ciclo donde la imagen de mario se movera hacia bajo, debido
    ## a la gravedad que en el juego también se cumple.
    if estadomario=="derecha" :
        lim=0
        while lim <=65:
            xm=int(c.coords(mario2)[0])
            ym=int(c.coords(mario2)[1])
            c.move(mario2,1,10)
            c.update ()
            if (ym==630):
                  break
            elif (ym==480):
                  break
            elif (ym==350):
                  break
            elif (ym==170):
                  break
            ventan2.after(15)
            lim+=2
    elif estadomario=="izquierda" :
        lim=0
        while lim <=65:
            xm=int(c.coords(mario2)[0])
            ym=int(c.coords(mario2)[1])
            c.move(mario2,-1,10)
            c.update ()
            if (ym==630):
                  break
            elif (ym==480):
                  break
            elif (ym==350):
                  break
            elif (ym==170):
                  break
            ventan2.after(15)
            lim+=2
            
## En la función movimiento lo que se hará es definir los estados que va a tener luigi, este puede
## tomar un estado hacia el lado derecho o hacia el lado izquierdo. Esto depende de la tecla que se le oprima.
## Para ello, "event" proporciona la capacidad de poder tomar la tecla que se le este siendo oprimida y la use para generar
## una serie de acciones y condiciones dependiendo de la ubicación del jugador.
def movimientoluigi (event):
    global c,luigi,estadoluigi,va,booli
    tecla = repr(event.char)
    if(tecla=="'l'"):
            p2=c.coords(luigi)
            c.delete(luigi)
            luigi=c.create_image(int(p2[0]),int(p2[1]), image=luigidere)
            estadoluigi="izquierda"
            c.move(luigi,10,0)
            if (c.coords(luigi)[0]>1280):
                c.coords(luigi,10,int(c.coords(luigi)[1]))
    if(tecla=="'j'"):
            p2=c.coords(luigi)
            c.delete(luigi)
            luigi=c.create_image(int(p2[0]),int(p2[1]), image=luigiizq)
            estadoluigi="derecha"
            c.move(luigi,-10,0)
            if (c.coords(luigi)[0]<0):
                c.coords(luigi,1270,int(c.coords(luigi)[1]))
  
## Los enemigos tendrán cada uno, una función que los caracterizará ya que esta solo consta de condicionales que activan 
## un valor booleano llamado varene que al ser True, ejecutará un ciclo.                
varene=False
r=False
def movimientotortuga ():
    global enemigo1,varene,mario2,enemigomuerto,puntosm,r,muerto,puntma,enemigo2,vel,luigi,puntosl,puntl,muerte,muertel
    xt=int(c.coords(enemigo1)[0])
    yt=int(c.coords(enemigo1)[1])
    c.move(enemigo1,-2,0)
    ## Las siguientes condiciones dan paso a una variable con valor booleano que activará el ciclo de caida:
    if (c.coords(enemigo1)[1]==490)and (c.coords(enemigo1)[0]>=480 and c.coords(enemigo1)[0]<=799):
        varene=True
    if (c.coords(enemigo1)[1]==360)and (c.coords(enemigo1)[0]>=160 and c.coords(enemigo1)[0]<=320):
        varene=True
    if (c.coords(enemigo1)[1]==360)and (c.coords(enemigo1)[0]>=963 and c.coords(enemigo1)[0]<=1120):
        varene=True
    if (c.coords(enemigo1)[1]==190)and (c.coords(enemigo1)[0]>=561 and c.coords(enemigo1)[0]<=720):
        varene=True
    if (c.coords(enemigo1)[0]<0):
        c.coords(enemigo1,1270,int(c.coords(enemigo1)[1]))
    if (c.coords(enemigo1)[0]==160) and (c.coords(enemigo1)[1]==640):
        c.delete(enemigo1)
        enemigo1=c.create_image(1018,190,image=enemigo)
        enemigo2=c.create_image(300,190,image=enemigorojo)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if (c.coords(mario2)[1]-60==c.coords(enemigo1)[1])and (c.coords(mario2)[0]-c.coords(enemigo1)[0]<20)and(c.coords(mario2)[0]-c.coords(enemigo1)[0]>-20):
        c.delete(enemigo1)
        muerto=c.create_image(xt,yt,image=capver)
        enemigo1=c.create_image(1018,190,image=enemigo)
        puntosm+=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
##    elif(c.coords(mario2)[0]==c.coords(muerto)[0])and (c.coords(mario2)[0]==c.coords(muerto)[1]):
##        c.delete (muerto)
##        enemigo1=c.create_image(1018,190,image=enemigo)
##        puntosm+=50       
    elif(max(c.coords(mario2)[0],c.coords(enemigo1)[0])-min(c.coords(mario2)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(mario2)[1],c.coords(enemigo1)[1])-min(c.coords(mario2)[1],c.coords(enemigo1)[1])<=20):
        c.delete(mario2)
        muerte-=1
        respawn ()
    elif(max(c.coords(luigi)[0],c.coords(enemigo1)[0])-min(c.coords(luigi)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(luigi)[1],c.coords(enemigo1)[1])-min(c.coords(luigi)[1],c.coords(enemigo1)[1])<=20):
        c.delete (luigi)
        muertel-=1
        respawnl ()
        
    ## Esta condicion al ser cierta, generará el ciclo de caida de la tortuga o enemigo que este en ese momento en pantalla. Para ello la funcion 
    ## .move tendra como coordenada en y 10 pixeles del canvas, asi logrando una caida exacta en la plataformas justamente inferior. 
    if varene==True :
        lim=0
        while lim <=100:
            xm=int(c.coords(enemigo1)[0])
            ym=int(c.coords(enemigo1)[1])
            c.move(enemigo1,-1,10)
            c.update ()
            if (ym==630):
                break
            elif (ym==480):
                break
            elif (ym==350):
                break
            ventan2.after(1)
            lim+=2
        varene=False
    ventan2.after(10+vel,movimientotortuga)


varen=False
def movimientotortuga2 ():
    global enemigo2,varen,mario2,enemigomuerto,muertor,puntosm,vel,puntosl,puntl,muerte,muertel
    xt=int(c.coords(enemigo2)[0])
    yt=int(c.coords(enemigo2)[1])
    c.move(enemigo2,2,0)
    ## Las siguientes condiciones dan paso a una variable con valor booleano que activará el ciclo de caida:
    if (c.coords(enemigo2)[1]==490)and (c.coords(enemigo2)[0]>=480 and c.coords(enemigo2)[0]<=799):
        varen=True
    if (c.coords(enemigo2)[1]==360)and (c.coords(enemigo2)[0]>=160 and c.coords(enemigo2)[0]<=320):
        varen=True
    if (c.coords(enemigo2)[1]==360)and (c.coords(enemigo2)[0]>=963 and c.coords(enemigo2)[0]<=1120):
        varen=True
    if (c.coords(enemigo2)[1]==190)and (c.coords(enemigo2)[0]>=561 and c.coords(enemigo2)[0]<=720):
        varen=True
    if (c.coords(enemigo2)[0]>1280):
        c.coords(enemigo2,10,int(c.coords(enemigo2)[1]))
    if (c.coords(enemigo2)[0]==1120) and (c.coords(enemigo2)[1]==640):
        c.delete(enemigo2)
        enemigo2=c.create_image(300,190,image=enemigorojo)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    elif (c.coords(mario2)[1]-60==c.coords(enemigo2)[1])and (c.coords(mario2)[0]-c.coords(enemigo2)[0]<20)and(c.coords(mario2)[0]-c.coords(enemigo2)[0]>-20):
        c.delete(enemigo2)
        muertor=c.create_image(xt,yt,image=caprojo)
        enemigo2=c.create_image(300,190,image=enemigorojo)
        puntosm+=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    elif(max(c.coords(mario2)[0],c.coords(enemigo2)[0])-min(c.coords(mario2)[0],c.coords(enemigo2)[0])<=20) and (max(c.coords(mario2)[1],c.coords(enemigo2)[1])-min(c.coords(mario2)[1],c.coords(enemigo2)[1])<=20):
        c.delete(mario2)
        muerte-=1
        respawn ()
    elif(max(c.coords(luigi)[0],c.coords(enemigo1)[0])-min(c.coords(luigi)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(luigi)[1],c.coords(enemigo1)[1])-min(c.coords(luigi)[1],c.coords(enemigo1)[1])<=20):
        c.delete (luigi)
        muertel-=1
        respawnl ()
        
## Esta condicion al ser cierta, generará el ciclo de caida de la tortuga o enemigo que este en ese momento en pantalla. Para ello la funcion 
## .move tendra como coordenada en y 10 pixeles del canvas, asi logrando una caida exacta en la plataformas justamente inferior. 
    if varen==True :
        lim=0
        while lim <=100:
            xm=int(c.coords(enemigo2)[0])
            ym=int(c.coords(enemigo2)[1])
            c.move(enemigo2,-1,10)
            c.update ()
            if (ym==630):
                break
            elif (ym==480):
                break
            elif (ym==350):
                break
            ventan2.after(1)
            lim+=2
        varen=False
    ventan2.after (10+vel,movimientotortuga2)
        
varo=False
vare=False
def movimientotorgran ():
    global torgran1,vare,mario2,puntosm,ventan2,vel,varo,puntosl,puntl,muerte,muertel
    xt=int(c.coords(torgran1)[0])
    yt=int(c.coords(torgran1)[1])
    c.move(torgran1,2,0)
    if (c.coords(torgran1)[1]==490)and (c.coords(torgran1)[0]>=480 and c.coords(torgran1)[0]<=799):
        vare=True
    if (c.coords(torgran1)[1]==360)and (c.coords(torgran1)[0]>=160 and c.coords(torgran1)[0]<=320):
        vare=True
    if (c.coords(torgran1)[1]==360)and (c.coords(torgran1)[0]>=963 and c.coords(torgran1)[0]<=1120):
        vare=True
    if (c.coords(torgran1)[1]==190)and (c.coords(torgran1)[0]>=561 and c.coords(torgran1)[0]<=720):
        vare=True
    if (c.coords(torgran1)[0]>1280):
        c.coords(torgran1,10,int(c.coords(torgran1)[1]))
    if (c.coords(torgran1)[0]==1120) and (c.coords(torgran1)[1]==640):
        c.delete(torgran1)
        torgran1=c.create_image(300,190,image=torgran)
    elif (c.coords(mario2)[1]-60==c.coords(torgran1)[1])and (c.coords(mario2)[0]-c.coords(torgran1)[0]<20)and(c.coords(mario2)[0]-c.coords(torgran1)[0]>-20):
        c.delete(torgran1)
        torgran1=c.create_image(300,190,image=torgran)
        puntosm+=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    elif(max(c.coords(mario2)[0],c.coords(torgran1)[0])-min(c.coords(mario2)[0],c.coords(torgran1)[0])<=20) and (max(c.coords(mario2)[1],c.coords(torgran1)[1])-min(c.coords(mario2)[1],c.coords(torgran1)[1])<=20):
        c.delete(mario2)
        muerte-=1
        respawn ()
    elif(max(c.coords(luigi)[0],c.coords(enemigo1)[0])-min(c.coords(luigi)[0],c.coords(enemigo1)[0])<=20) and (max(c.coords(luigi)[1],c.coords(enemigo1)[1])-min(c.coords(luigi)[1],c.coords(enemigo1)[1])<=20):
        c.delete (luigi)
        muertel-=1
        respawnl ()
        
## Esta condicion al ser cierta, generará el ciclo de caida de la tortuga o enemigo que este en ese momento en pantalla. Para ello la funcion 
## .move tendra como coordenada en y 10 pixeles del canvas, asi logrando una caida exacta en la plataformas justamente inferior. 
    if vare==True :
        lim=0
        while lim <=100:
            ym=int(c.coords(torgran1)[1])
            c.move(torgran1,-1,10)
            c.update ()
            if (ym==630):
                break
            elif (ym==480):
                break
            elif (ym==350):
                break
            ventan2.after(1)
            lim+=2
        vare=False
    ventan2.after (10+vel,movimientotorgran)

va=False
def movimientodelraro ():
    global el,va,mario2,enemigomuerto,puntosm,muerto,puntma,enemigo2,vel,luigi,puntosl,puntl,muerte,muertel
    xt=int(c.coords(el)[0])
    yt=int(c.coords(el)[1])
    c.move(el,-2,0)
    ## Las siguientes condiciones dan paso a una variable con valor booleano que activará el ciclo de caida:
    if (c.coords(el)[1]==490)and (c.coords(el)[0]>=480 and c.coords(el)[0]<=799):
        va=True
    if (c.coords(el)[1]==360)and (c.coords(el)[0]>=160 and c.coords(el)[0]<=320):
        va=True
    if (c.coords(el)[1]==360)and (c.coords(el)[0]>=963 and c.coords(el)[0]<=1120):
        va=True
    if (c.coords(el)[1]==190)and (c.coords(el)[0]>=561 and c.coords(el)[0]<=720):
        va=True
    if (c.coords(el)[0]<0):
        c.coords(el,1270,int(c.coords(el)[1]))
    if (c.coords(el)[0]==160) and (c.coords(el)[1]==640):
        c.delete(el)
        el=c.create_image(1018,190,image=elmat)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if (c.coords(mario2)[1]-60==c.coords(el)[1])and (c.coords(mario2)[0]-c.coords(el)[0]<20)and(c.coords(mario2)[0]-c.coords(el)[0]>-20):
        c.delete(el)
        el=c.create_image(1018,190,image=elmat)
        puntosm+=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)     
    elif(max(c.coords(mario2)[0],c.coords(el)[0])-min(c.coords(mario2)[0],c.coords(el)[0])<=20) and (max(c.coords(mario2)[1],c.coords(el)[1])-min(c.coords(mario2)[1],c.coords(el)[1])<=20):
        c.delete(mario2)
        muerte-=1
        respawn ()
    elif(max(c.coords(luigi)[0],c.coords(el)[0])-min(c.coords(luigi)[0],c.coords(el)[0])<=20) and (max(c.coords(luigi)[1],c.coords(el)[1])-min(c.coords(luigi)[1],c.coords(el)[1])<=20):
        c.delete (luigi)
        muertel-=1
        respawnl ()
     
    ## Esta condicion al ser cierta, generará el ciclo de caida de la tortuga o enemigo que este en ese momento en pantalla. Para ello la funcion 
    ## .move tendra como coordenada en y 10 pixeles del canvas, asi logrando una caida exacta en la plataformas justamente inferior. 
    if va==True :
        lim=0
        while lim <=100:
            xm=int(c.coords(el)[0])
            ym=int(c.coords(el)[1])
            c.move(el,-1,10)
            c.update ()
            if (ym==630):
                break
            elif (ym==480):
                break
            elif (ym==350):
                break
            ventan2.after(1)
            lim+=2
        va=False
    ventan2.after(10+vel,movimientodelraro)


van=False
def movimientobomba ():
    global bo,van,mario2,puntosm,muerto,puntma,vel,luigi,puntosl,puntl,muerte,muertel,bmuerta
    xt=int(c.coords(bo)[0])
    yt=int(c.coords(bo)[1])
    c.move(bo,-2,0)
    ## Las siguientes condiciones dan paso a una variable con valor booleano que activará el ciclo de caida:
    if (c.coords(bo)[1]==490)and (c.coords(bo)[0]>=480 and c.coords(bo)[0]<=799):
        van=True
    if (c.coords(bo)[1]==360)and (c.coords(bo)[0]>=160 and c.coords(bo)[0]<=320):
        van=True
    if (c.coords(bo)[1]==360)and (c.coords(bo)[0]>=963 and c.coords(bo)[0]<=1120):
        van=True
    if (c.coords(bo)[1]==190)and (c.coords(bo)[0]>=561 and c.coords(bo)[0]<=720):
        van=True
    if (c.coords(bo)[0]<0):
        c.coords(bo,1270,int(c.coords(bo)[1]))
    if (c.coords(bo)[0]==160) and (c.coords(bo)[1]==640):
        c.delete(bo)
        bo=c.create_image(1050,190,image=bom)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if (c.coords(mario2)[1]-60==c.coords(bo)[1])and (c.coords(mario2)[0]-c.coords(bo)[0]<20)and(c.coords(mario2)[0]-c.coords(bo)[0]>-20):
        c.delete(bo)
        bmuerta=c.create_image(xt,yt,image=bomuer)
        bo=c.create_image(1050,190,image=bom)
        puntosm+=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)     
    elif(max(c.coords(mario2)[0],c.coords(bo)[0])-min(c.coords(mario2)[0],c.coords(bo)[0])<=20) and (max(c.coords(mario2)[1],c.coords(bo)[1])-min(c.coords(mario2)[1],c.coords(bo)[1])<=20):
        c.delete(mario2)
        muerte-=1
        respawn ()
    elif(max(c.coords(luigi)[0],c.coords(bo)[0])-min(c.coords(luigi)[0],c.coords(bo)[0])<=20) and (max(c.coords(luigi)[1],c.coords(bo)[1])-min(c.coords(luigi)[1],c.coords(bo)[1])<=20):
        c.delete (luigi)
        muertel-=1
        respawnl ()
     
    ## Esta condicion al ser cierta, generará el ciclo de caida de la tortuga o enemigo que este en ese momento en pantalla. Para ello la funcion 
    ## .move tendra como coordenada en y 10 pixeles del canvas, asi logrando una caida exacta en la plataformas justamente inferior. 
    if van==True :
        lim=0
        while lim <=100:
            ym=int(c.coords(bo)[1])
            c.move(bo,-1,10)
            c.update ()
            if (ym==630):
                break
            elif (ym==480):
                break
            elif (ym==350):
                break
            ventan2.after(1)
            lim+=2
        van=False
    ventan2.after(10+vel,movimientobomba)


## La función respawn prooverá la imagen de mario despues de haber sido matado por un enemigo y asi mismo, se le restará
## 50 puntos al puntaje que lleve el jugador.
def respawn ():
    global c,mario2,estadomario,lim,ventan2,vidam2,puntosm,puntma,luigi
    mario2=c.create_image(260,640, image=mariodere)
    if muerte ==4:
        vidam2=c.create_image(250,60,image=vidam20)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if muerte==3:
        vidam2=c.create_image(250,60,image=vidam30)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if muerte==2:
        vidam2=c.create_image(250,60,image=vidam40)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if muerte==1:
        vidam2=c.create_image(250,60,image=vidam40)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
    if muerte==0:
        vidam2=c.create_image(250,60,image=mu)
        c.create_image(640,330,image=go)
        puntosm-=50
        puntma=Label(ventan2,text=puntosm,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="saddle brown")
        puntma.place (x=50,y=10)
        c.delete(mario2)
        c.delete(luigi)
        
def respawnl ():
    global c,luigi,estadomario,lim,ventan2,vidal2,puntosl,puntl,mario2,muertel
    luigi=c.create_image(900,640, image=luigidere)
    if muertel==4:
        vidal2=c.create_image(1050,60,image=vidal20)
        puntosl-=50
        puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
        puntl.place (x=1100,y=10)   
    if muertel==3:
        vidal2=c.create_image(1050,60,image=vidal30)
        puntosl-=50
        puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
        puntl.place (x=1100,y=10)   
    if muertel==2:
        vidal2=c.create_image(1050,60,image=vidal40)
        puntosl-=50
        puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
        puntl.place (x=1100,y=10)   
    if muertel==1:
        vidal2=c.create_image(1050,60,image=vidal40)
        puntosl-=50
        puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
        puntl.place (x=1100,y=10)   
    if muertel==0:
        vidal2=c.create_image(1050,60,image=mu)
        c.create_image(640,330,image=go)
        puntosl-=50
        puntl=Label(ventan2,text=puntosl,height=2,width=9,font=("Super Mario Bros.",20),bg="black",fg="green")
        puntl.place (x=1100,y=10)   
        c.delete(mario2)
        c.delete (luigi)
        
        
    
def guardar_puntajes():
    global puntosm,puntosl
    archivo=open("proyecto.txt","w")
    archivo.write (entrada)
    archivo.write (entradal)
    archivo.write (puntosm)
    archivo.write (puntosl)
    archivo.close ()

def fin ():
    global puntosl
    if puntosl<(-100):
        ventan2.destroy ()
        ve=Tk ()
        ve.geometry ("1000x750")
        wid=Label(ve,image=go).pack()

##def juegoperdido ():
##    global ventan2,estadomario,enemigo1,enemigo2,txtmario,txtluigi,entrada,entradal,puntosm,vidam2,vidal2,vidam,vidal,muerto,muertor,puntma,torgran1,vel
##    if puntosl==(-2000):
##        
    
##def recuperar_puntajes():

   
    
    
## Fuera de todas las funciones se le asignan variables a las diferentes imagenes que se verán
## involucradas durante el juego y aparte de esto, se crea la imagen principal con sus respectivos botones.           
ventana.geometry("1280x960")
ventana.title("Mario & Luigi")
img = PhotoImage(file="inicio.gif")
widget = Label(ventana, image=img).pack()
imgboton=PhotoImage(file="botonini.gif")
go=PhotoImage(file="gameover.png")
mu=PhotoImage(file="muerte.png")
imgboton2=PhotoImage(file="botoncargarpartida.gif")
lvl1=PhotoImage(file="lvl1.gif")
lvl2=PhotoImage(file="lvl2.gif")
lvl3=PhotoImage(file="lvl3.gif")
lvl4=PhotoImage(file="lvl4.gif")
lvl5=PhotoImage(file="lvl5.gif")
guardar=PhotoImage(file="guadar.gif")
enemigo=PhotoImage(file="tortugaverde.png")
torgran=PhotoImage(file="torgran.png")
capver=PhotoImage(file="capverde.png")
caprojo=PhotoImage(file="caprojo.png")
enemigorojo=PhotoImage(file="tortugaroja1.png")
mosca=PhotoImage(file="mosca.png")
fantasma=PhotoImage(file="fantasma.png")
pl=PhotoImage(file="planta.png")
pl2=PhotoImage(file="pl.png")
tor=PhotoImage(file="torre.png")
elmat=PhotoImage(file="elma.png")
bomuer=PhotoImage(file="bombamuerta.png")
bom=PhotoImage(file="bomb.png")
mariodere=PhotoImage(file="marioder2.png")
marioizq=PhotoImage(file="marioizq2.png")
marioderecor=PhotoImage(file="correrder.png")
mariosaltoder=PhotoImage(file="saltoder2.png")
mariosaltoizq=PhotoImage(file="saltoizq2.png")
luigidere=PhotoImage(file="luigider.png")
luigiizq=PhotoImage(file="luigiizq.png")
luigisal=PhotoImage(file="lusalto.png")
vidam=PhotoImage(file="vidam.png")
vidal=PhotoImage(file="vidal.png")
vidal20=PhotoImage(file="vidal2.png")
vidal30=PhotoImage(file="vidal3.png")
vidal40=PhotoImage(file="vidal4.png")
vidam20=PhotoImage(file="vidam2.png")
vidam30=PhotoImage(file="vidam3.png")
vidam40=PhotoImage(file="vidam4.png")
estadomario="derecha"
estadoluigi="derecha"

## Los botones iniciales se encuentra en las siguientes variables que despues serán usadas para eliminarse y crear nuevos botones.
Bot= Button(ventana,image=imgboton,
              command=iniciar2)
Bot.place(x=200,y=430)
Bot2=Button(ventana,image=imgboton2,command=iniciar2)
Bot2.place(x=650,y=530)







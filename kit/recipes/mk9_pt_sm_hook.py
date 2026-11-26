import json
def S(img,t,f,z,**k): d={"img":img,"t":t,"focus":list(f),"zoom":list(z)}; d.update(k); return d
C=lambda s,e,text,y=.40: {"type":"card","start":s,"end":e,"text":text,"y":y}
W=(1.0,1.06)
def R(n,out,title,end,scenes,ov,sfx,music="music_comedy1.mp3",vol=0.35):
    d={"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":[],"full":True,"caps":"big","title_y":230,
       "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]}
    if music: d.update(music=music,music_vol=vol)
    json.dump(d,open(n+".json","w"),indent=1)
P="pt1T_"
R("pt2","public_transport_pt1",["Every Type of Person","on Public Transport"],31.7,[
 S(P+"close",0,(.5,.45),(1.0,1.45),punch=1,shake=1.2),
 S(P+"doors",1.4,(.5,.45),(1.15,1.35),punch=1), S(P+"map",2.4,(.5,.3),(1.1,1.35),punch=1),
 S(P+"close",3.9,(.5,.4),(1.3,1.7),punch=1,shake=0.8),
 S(P+"doors",6.0,(.5,.5),W), S(P+"doors",7.36,(.3,.5),(1.3,1.4)),
 S(P+"close",9.28,(.5,.5),(1.1,1.2)), S(P+"lean",10.56,(.7,.5),(1.35,1.45)),
 S(P+"squeeze",13.0,(.5,.5),W), S(P+"backpack",14.8,(.65,.45),(1.3,1.4),punch=1,shake=0.8), S(P+"stroller",16.0,(.55,.65),(1.25,1.35)),
 S(P+"close",18.3,(.5,.65),(1.4,1.5)),
 S(P+"map",20.9,(.5,.45),W), S(P+"squash",21.9,(.5,.5),(1.1,1.2)),
 S(P+"map",23.0,(.5,.35),(1.2,1.3)), S(P+"squash",24.0,(.5,.45),(1.35,1.45)),
 S(P+"empty",25.4,(.5,.5),W), S(P+"empty",26.5,(.5,.4),(1.35,1.45)),
 S(P+"reverse",27.8,(.5,.5),W), S(P+"reverse",28.9,(.5,.4),(1.0,1.45),punch=1),
],[
 C(-0.2,5.7,"8 STOPS. NOT GETTING OFF.",.30),
 C(10.7,12.9,"HE LIKES THE DOOR."),
 C(14.9,15.9,"*BONK*"), C(16.4,18.0,"*crunch*"),
 C(20.9,21.8,"NEXT STOP"), C(21.9,22.9,"SAME THING."),
 C(23.0,23.9,"NEXT STOP"), C(24.0,25.3,"SAME THING."),
],[(0.0,"boom"),(1.4,"ding"),(3.95,"boom"),(6.0,"ding"),(14.9,"crunch"),(16.4,"pop"),(20.9,"ding"),(23.0,"ding"),(28.9,"boom")])
Q="sm1T_"
R("sm2","supermarket_pt1",["Every Type of Person","at the Supermarket"],35.6,[
 S(Q+"aisle",0,(.45,.6),(1.0,1.4),punch=1,shake=1.2),
 S(Q+"read",1.3,(.5,.4),(1.1,1.35),punch=1),
 S(Q+"aisle",2.3,(.45,.62),(1.15,1.35),punch=1,shake=0.6),
 S(Q+"start",4.6,(.5,.5),W), S(Q+"start",6.2,(.5,.35),(1.6,1.7)),
 S(Q+"aisle",7.1,(.5,.5),W), S(Q+"aisle",8.9,(.45,.6),(1.25,1.35)), S(Q+"aisle",11.3,(.45,.42),(1.7,1.8)),
 S(Q+"read",12.3,(.5,.5),W), S(Q+"read",13.0,(.65,.35),(1.4,1.5)),
 S(Q+"polite",14.6,(.6,.6),(1.1,1.15)), S(Q+"read",16.6,(.5,.35),(1.1,1.15)),
 S(Q+"louder",17.5,(.6,.7),(1.15,1.25)), S(Q+"louder",19.0,(.5,.35),(1.7,1.8)),
 S(Q+"bump",22.3,(.5,.5),W), S(Q+"bump",24.0,(.55,.6),(1.35,1.45),punch=1,shake=0.8),
 S(Q+"glare",25.8,(.5,.4),(1.0,1.3),punch=1), S(Q+"glare",26.9,(.5,.35),(1.3,1.4)),
 S(Q+"wheels",28.4,(.45,.72),(1.6,1.7)), S(Q+"wheels",29.6,(.4,.78),(2.0,2.1)),
 S(Q+"fridge",30.8,(.5,.55),W), S(Q+"fridge",32.7,(.72,.5),(1.0,1.4),punch=1),
],[
 C(-0.2,4.4,"SHE'S NOT EVEN USING IT.",.30),
 C(6.3,7.0,"MILK."),
 C(9.0,11.2,"SIDEWAYS."),
 C(16.6,17.4,"NOTHING."),
 C(21.2,22.2,"*to compare*"),
 C(25.8,28.3,"HOW DARE YOU.",.30),
 C(29.6,30.7,"ONE. INCH."),
],[(0.0,"boom"),(2.3,"crunch"),(6.3,"pop"),(9.0,"boom"),(16.6,"sad"),(21.2,"pop"),(24.0,"crunch"),(25.8,"boom"),(29.6,"ding"),(32.8,"sad")])
print("ok")

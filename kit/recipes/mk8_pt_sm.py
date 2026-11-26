import json
S=lambda img,t,f,z: {"img":img,"t":t,"focus":list(f),"zoom":list(z)}
C=lambda s,e,text,y=.40: {"type":"card","start":s,"end":e,"text":text,"y":y}
W=(1.0,1.06)
def R(n,out,title,end,scenes,ov,sfx,music="music_comedy1.mp3",vol=0.35):
    d={"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":[],"full":True,"caps":"big","title_y":230,
       "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]}
    if music: d.update(music=music,music_vol=vol)
    json.dump(d,open(n+".json","w"),indent=1)
P="pt1T_"
R("pt","public_transport_pt1",["Every Type of Person","on Public Transport"],30.0,[
 S(P+"doors",0,(.5,.5),W), S(P+"doors",1.6,(.3,.5),(1.3,1.4)), S(P+"doors",3.3,(.5,.45),(1.5,1.6)),
 S(P+"close",4.8,(.5,.55),W), S(P+"close",6.0,(.5,.6),(1.2,1.3)), S(P+"close",7.4,(.5,.45),(1.45,1.55)),
 S(P+"lean",9.0,(.7,.5),(1.35,1.45)),
 S(P+"squeeze",11.5,(.5,.5),W), S(P+"backpack",13.2,(.65,.45),(1.3,1.4)), S(P+"stroller",14.2,(.55,.65),(1.25,1.35)),
 S(P+"close",16.4,(.5,.65),(1.4,1.5)),
 S(P+"map",18.7,(.5,.45),W), S(P+"squash",19.7,(.5,.5),(1.1,1.2)),
 S(P+"map",20.8,(.5,.35),(1.2,1.3)), S(P+"squash",21.8,(.5,.45),(1.35,1.45)),
 S(P+"empty",23.0,(.5,.5),W), S(P+"empty",24.4,(.5,.4),(1.35,1.45)),
 S(P+"reverse",26.1,(.5,.5),W), S(P+"reverse",27.1,(.5,.4),(1.4,1.5)),
],[
 C(9.3,11.3,"HE LIKES THE DOOR."),
 C(13.3,14.1,"*BONK*"), C(14.5,16.2,"*crunch*"),
 C(18.8,19.7,"NEXT STOP"), C(19.8,20.7,"SAME THING."),
 C(20.9,21.8,"NEXT STOP"), C(21.9,22.9,"SAME THING."),
 C(23.1,25.9,"8 STOPS LATER"),
],[(0.2,"ding"),(4.9,"boom"),(13.4,"crunch"),(14.6,"pop"),(18.8,"ding"),(20.9,"ding"),(23.1,"ding"),(27.2,"boom")])
Q="sm1T_"
R("sm","supermarket_pt1",["Every Type of Person","at the Supermarket"],32.7,[
 S(Q+"start",0,(.5,.5),W), S(Q+"start",1.8,(.5,.35),(1.6,1.7)),
 S(Q+"aisle",2.8,(.5,.5),W), S(Q+"aisle",4.6,(.45,.6),(1.25,1.35)), S(Q+"aisle",7.0,(.45,.42),(1.7,1.8)),
 S(Q+"read",8.5,(.5,.5),W), S(Q+"read",10.0,(.65,.35),(1.4,1.5)),
 S(Q+"polite",11.8,(.6,.6),(1.1,1.15)), S(Q+"read",13.8,(.5,.35),(1.1,1.15)),
 S(Q+"louder",14.8,(.6,.7),(1.15,1.25)), S(Q+"louder",16.2,(.5,.35),(1.7,1.8)),
 S(Q+"bump",19.7,(.5,.5),W), S(Q+"bump",21.6,(.55,.6),(1.35,1.45)),
 S(Q+"glare",23.0,(.5,.4),(1.0,1.1)), S(Q+"glare",24.1,(.5,.35),(1.3,1.4)),
 S(Q+"wheels",25.6,(.45,.72),(1.6,1.7)), S(Q+"wheels",26.8,(.4,.78),(2.0,2.1)),
 S(Q+"fridge",28.0,(.5,.55),W), S(Q+"fridge",30.1,(.72,.5),(1.3,1.4)),
],[
 C(1.9,2.7,"MILK."),
 C(4.7,6.9,"SIDEWAYS."),
 C(13.9,14.7,"NOTHING."),
 C(18.6,19.6,"*to compare*"),
 C(23.1,25.5,"HOW DARE YOU.",.30),
 C(26.8,27.9,"ONE. INCH."),
],[(1.9,"pop"),(4.7,"boom"),(13.9,"sad"),(18.6,"pop"),(21.7,"crunch"),(23.1,"boom"),(26.8,"ding"),(30.2,"sad")])
print("ok")

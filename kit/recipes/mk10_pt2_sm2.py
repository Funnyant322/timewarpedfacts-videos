import json
def S(img,t,f,z,**k): d={"img":img,"t":t,"focus":list(f),"zoom":list(z)}; d.update(k); return d
C=lambda s,e,text,y=.40: {"type":"card","start":s,"end":e,"text":text,"y":y}
W=(1.0,1.06)
def R(n,out,title,end,scenes,ov,sfx,music="sneaky_tense.mp3",vol=0.55):
    d={"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":[],"full":True,"caps":"big","title_y":230,
       "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]}
    if music: d.update(music=music,music_vol=vol)
    json.dump(d,open(n+".json","w"),indent=1)
P="pt2T_"
R("pt3","public_transport_pt2",["Every Type of Person","on Public Transport"],25.5,[
 S(P+"close",0,(.5,.4),(1.0,1.35),punch=1,shake=1.2), S(P+"start",1.6,(.5,.45),(1.1,1.3),punch=1),
 S(P+"close",2.5,(.5,.35),(1.3,1.7),punch=1,shake=0.8),
 S(P+"waves",3.3,(.5,.5),W), S(P+"waves",5.0,(.4,.5),(1.2,1.35),punch=1), S(P+"waves",5.9,(.4,.5),(1.35,1.6),punch=1,shake=1.0),
 S(P+"listen",7.1,(.5,.5),W), S(P+"listen",8.9,(.75,.6),(1.2,1.3)),
 S(P+"rash",10.5,(.5,.4),(1.1,1.45),punch=1,shake=0.6),
 S(P+"far",11.7,(.5,.5),W), S(P+"far",12.8,(.5,.17),(1.3,2.6),punch=1),
 S(P+"tunnel",15.4,(.5,.5),W), S(P+"tunnel",16.6,(.45,.4),(1.25,1.35)),
 S(P+"shout",17.5,(.5,.45),(1.0,1.2),punch=1,shake=1.2), S(P+"shout",19.1,(.5,.35),(1.3,1.6),punch=1,shake=1.0),
 S(P+"start",20.4,(.5,.5),W), S(P+"again",22.1,(.5,.5),W), S(P+"again",23.4,(.5,.45),(1.2,1.4),punch=1),
],[
 C(-0.2,3.2,"HE TOLD EVERYONE HIS PIN.",.30),
 C(5.0,7.0,"VOLUME: MAX"),
 C(10.6,11.6,"HIS RASH."),
 C(13.6,15.3,"*knows about the rash*"),
 C(17.5,20.3,"\"CAN YOU HEAR ME?!\""),
 C(23.4,25.4,"*to explain the tunnel*"),
],[(0.0,"boom"),(1.6,"ding"),(2.5,"boom"),(3.3,"pop"),(5.9,"boom"),(10.7,"sad"),(13.6,"pop"),(15.4,"ding"),(17.5,"boom"),(19.1,"boom"),(20.4,"ding"),(23.5,"sad")])
Q="sm2T_"
R("sm3","supermarket_pt2",["Every Type of Person","at the Supermarket"],25.2,[
 S(Q+"smug",0,(.5,.45),(1.0,1.3),punch=1,shake=1.2), S(Q+"smug",1.9,(.45,.78),(1.2,1.6),punch=1),
 S(Q+"queue",2.8,(.5,.55),(1.0,1.25),punch=1,shake=0.6),
 S(Q+"start",4.5,(.5,.5),W), S(Q+"start",6.2,(.55,.55),(1.15,1.25)), S(Q+"start",7.5,(.6,.45),(1.2,1.5),punch=1),
 S(Q+"husband",8.5,(.5,.5),(1.0,1.15),punch=1,shake=0.8), S(Q+"husband",10.4,(.45,.55),(1.2,1.35)),
 S(Q+"son",12.2,(.5,.5),(1.0,1.15),punch=1,shake=0.8), S(Q+"son",13.2,(.75,.5),(1.2,1.35)),
 S(Q+"grandma",14.5,(.5,.5),(1.0,1.15),punch=1,shake=0.8), S(Q+"grandma",15.7,(.7,.6),(1.25,1.4)),
 S(Q+"icecream",17.0,(.5,.5),W), S(Q+"icecream",18.4,(.45,.5),(1.05,1.3),punch=1),
 S(Q+"next",20.5,(.5,.5),W), S(Q+"next",22.0,(.35,.25),(1.2,1.6),punch=1),
 S(Q+"shutter",23.0,(.5,.5),(1.0,1.15),punch=1,shake=1.2), S(Q+"shutter",24.0,(.55,.6),(1.2,1.35)),
],[
 C(-0.2,2.7,"ONE TIN OF BEANS.",.30),
 C(7.5,8.4,"EASY."),
 C(8.6,10.3,"+ HUSBAND"), C(12.3,14.4,"+ SON"), C(14.6,16.9,"+ GRANDMA (x2)"),
 C(19.6,20.4,"SOUP."),
 C(22.0,22.9,"\"NEXT!\""),
 C(23.1,25.1,"*CLOSED*"),
],[(0.0,"boom"),(1.9,"pop"),(2.8,"boom"),(7.5,"ding"),(8.5,"boom"),(12.2,"boom"),(14.5,"boom"),(18.4,"sad"),(22.0,"ding"),(23.0,"crunch"),(23.3,"boom")])
print("ok")

import json
S=lambda img,t,f,z: {"img":img,"t":t,"focus":list(f),"zoom":list(z)}
C=lambda s,e,text,y=.34: {"type":"card","start":s,"end":e,"text":text,"y":y}
B=lambda s,e,text,x,y,tail: {"type":"bubble","start":s,"end":e,"text":text,"x":x,"y":y,"tail":list(tail)}
W=(1.0,1.08)
def P(s,e,msgs,side,clock,title,av="Leo",me="Sam",group=True):
    return {"type":"phone","start":s,"end":e,"scale":1.2,"side":side,"group":group,"me":me,"title":title,"title_av":av,"clock":clock,
            "msgs":[{"t":t,"from":f,"text":x} for t,f,x in msgs]}
def R(n,out,title,end,scenes,ov,sfx,music=True):
    d={"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":["Follow for","Part 6"],
       "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]}
    if music: d.update(music="music_comedy1.mp3",music_vol=0.35)
    json.dump(d,open(n+".json","w"),indent=1)

# ---------- Friend pt5: let's plan a trip ----------
R("fr5","friend_pt5",["Every Type of Friend","Explained pt 5"],55.0,[
 S("fr5_midnight",0,(.5,.5),W), S("fr5_midnight",3.0,(.6,.35),(1.5,1.65)),
 S("fr5_midnight",6.5,(.5,.5),(1.05,1.12)), S("fr5_midnight",8.8,(.65,.35),(1.7,1.85)),
 S("fr5_midnight",11.2,(.25,.65),(1.8,1.95)),
 S("fr5_links",12.9,(.5,.5),W),
 S("fr5_links",16.4,(.3,.25),(1.6,1.75)), S("fr5_links",18.3,(.25,.2),(2.1,2.25)), S("fr5_links",19.1,(.45,.2),(2.1,2.25)),
 S("fr5_links",19.9,(.3,.45),(1.9,2.0)),
 S("fr5_links",21.7,(.82,.5),(1.8,1.95)), S("fr5_links",23.6,(.42,.45),(1.8,1.95)),
 S("fr5_sheet",25.4,(.5,.5),W), S("fr5_sheet",27.9,(.3,.62),(1.8,1.95)),
 S("fr5_deposit",30.9,(.5,.5),W), S("fr5_deposit",32.2,(.33,.3),(1.6,1.75)), S("fr5_deposit",34.2,(.68,.62),(1.8,1.95)),
 S("gc2_cobweb",35.3,(.5,.5),(1.0,1.1)),
 S("fr5_midnight",38.2,(.5,.5),(1.15,1.2)),
 S("fr5_cafe",41.6,(.5,.5),W), S("fr5_cafe",44.6,(.65,.4),(1.6,1.75)), S("fr5_cafe",47.9,(.64,.38),(1.95,2.1)),
 S("fr5_cafe",50.6,(.32,.38),(1.7,1.85)), S("fr5_cafe",52.6,(.5,.5),W),
],[
 C(6.6,8.6,"12:00 AM"),
 B(8.8,11.1,"guys. we need to go on a trip.",.5,.2,(.68,.3)),
 C(11.3,12.8,"EVERYONE: \"yes\"",.62),
 P(13.0,21.6,[(13.1,"Leo","BALI TRIP!!!"),(16.5,"Leo","villa.com/..."),(17.0,"Leo","flights.com/..."),(17.5,"Leo","boats4u.com/..."),(18.0,"Leo","+37 more links")],"left","12:04","BALI TRIP!!!"),
 B(21.8,23.5,"when?",.78,.24,(.8,.36)),
 B(23.7,25.3,"soon.",.45,.22,(.45,.34)),
 C(25.5,27.8,"WEEK 1"), C(27.9,30.8,"WEEK 2: COLOURS"),
 C(31.0,32.1,"WEEK 3"), C(32.3,34.1,"\"deposit pls\"",.62),
 C(34.3,35.2,"*silence*"),
 C(35.4,38.1,"MONTH 2"),
 P(38.3,41.5,[(38.4,"Maya","renamed the group"),(39.8,"Maya","bali??")],"right","6 months later","bali??"),
 C(41.7,44.5,"1 YEAR LATER"),
 B(47.9,50.5,"guys. we need to go on a trip.",.5,.2,(.62,.32)),
],[(13.1,"pop"),(16.5,"pop"),(17.0,"pop"),(17.5,"pop"),(18.0,"pop"),(34.3,"sad"),(39.8,"pop"),(48.0,"boom")])

# ---------- Group chat pt5: the "k" replier ----------
R("gc5","group_chat_pt5",["Every Type of Person","in a Group Chat","Explained pt 5"],57.0,[
 S("gc5_typing",0,(.5,.5),W), S("gc5_typing",3.5,(.5,.4),(1.5,1.65)),
 S("gc5_typing",7.3,(.5,.5),(1.05,1.12)), S("gc5_typing",9.1,(.45,.6),(1.7,1.85)), S("gc5_typing",12.6,(.5,.3),(1.8,1.95)),
 S("gc5_lazy",14.4,(.5,.5),W), S("gc5_lazy",16.0,(.45,.62),(1.4,1.55)),
 S("gc5_typing",17.1,(.5,.35),(1.6,1.75)), S("gc5_lazy",18.6,(.5,.7),(1.6,1.75)),
 S("gc5_shock",20.1,(.5,.5),W), S("gc5_shock",22.6,(.5,.75),(1.6,1.75)),
 S("gc5_shock",24.7,(.5,.35),(1.4,1.55)), S("gc5_shock",26.1,(.5,.35),(1.7,1.85)), S("gc5_shock",27.5,(.5,.35),(2.0,2.15)),
 S("gc5_typing",29.3,(.5,.5),(1.1,1.2)),
 S("gc5_shock",31.4,(.45,.3),(1.8,1.9)), S("gc5_shock",32.7,(.55,.3),(1.9,2.0)), S("gc5_shock",33.8,(.5,.3),(2.1,2.2)),
 S("gc5_committee",35.0,(.5,.5),W), S("gc5_committee",37.0,(.5,.3),(1.5,1.65)),
 S("gc5_typing",38.5,(.5,.4),(1.4,1.55)), S("gc5_lazy",41.6,(.5,.5),(1.2,1.3)),
 S("gc5_shock",43.5,(.5,.45),(1.3,1.4)), S("gc5_committee",45.1,(.5,.6),(1.4,1.55)),
 S("gc5_fine",47.0,(.5,.5),W), S("gc5_fine",48.9,(.78,.45),(1.6,1.75)), S("gc5_fine",50.6,(.3,.3),(1.7,1.85)),
 S("gc5_fine",53.4,(.5,.5),W),
],[
 P(7.4,14.3,[(9.2,"Sam","hey so..."),(10.0,"Sam","I've been thinking"),(10.7,"Sam","about everything"),(11.7,"Sam","and our plans..."),(12.7,"Sam","I'm really sorry"),(14.0,"Sam","(+9 paragraphs)")],"right","11:42 PM","Leo",group=False),
 C(15.8,17.0,"typing...",.62), C(17.2,18.5,"...",.62), C(18.7,20.0,"typing...",.62),
 P(20.1,23.45,[(22.6,"Leo","k")],"right","11:58 PM","Leo",group=False),
 C(23.5,24.6,"JUST K.",.62),
 C(24.7,26.0,"NOT \"ok\""), C(26.1,27.4,"NOT \"okay\""), C(27.5,29.2,"NO FULL STOP"),
 C(29.4,31.3,"READ: 11 TIMES"),
 C(31.4,32.6,"ANGRY?",.62), C(32.7,33.7,"BUSY?",.62), C(33.8,34.9,"OKAY?",.62),
 C(37.1,38.4,"EMERGENCY MEETING"),
 P(38.6,46.9,[(39.0,"Sam","are you mad?"),(42.9,"Leo","no.")],"right","1:58 AM","Leo",group=False),
 C(38.6,40.4,"2 HOURS LATER",.62),
 C(44.0,45.0,"WITH A FULL STOP.",.62), C(45.2,46.9,"HE'S MAD."),
 C(47.1,48.8,"NEXT DAY"),
 B(48.9,50.5,"hey man!",.75,.24,(.78,.36)),
 C(50.7,53.2,"\"what are you talking about?\""),
],[(16.0,"pop"),(18.7,"pop"),(22.7,"ding"),(23.6,"boom"),(29.4,"pop"),(37.1,"pop"),(39.0,"pop"),(42.9,"ding"),(45.2,"boom"),(50.7,"sad")])
print("ok")

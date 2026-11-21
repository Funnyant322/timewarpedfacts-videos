import json
S=lambda img,t,f,z: {"img":img,"t":t,"focus":list(f),"zoom":list(z)}
C=lambda s,e,text,y=.62: {"type":"card","start":s,"end":e,"text":text,"y":y}
B=lambda s,e,text,x,y,tail: {"type":"bubble","start":s,"end":e,"text":text,"x":x,"y":y,"tail":list(tail)}
W=(1.0,1.08)
def P(s,e,msgs,side,clock,title="The Squad"):
    return {"type":"phone","start":s,"end":e,"scale":1.2,"side":side,"group":True,"me":"Sam","title":title,"title_av":"Jay","clock":clock,
            "msgs":[{"t":t,"from":f,"text":x} for t,f,x in msgs]}
def R(n,out,title,end,scenes,ov,sfx):
    json.dump({"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":["Follow for","Part 5"],
               "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]},open(n+".json","w"),indent=1)

# ---------- Friend pt4 ----------
R("fr4","friend_pt4",["Every Type of Friend","Explained pt 4"],52.4,[
 S("fr4_counter",0,(.5,.55),W), S("fr4_counter",4.2,(.7,.4),(1.6,1.75)),
 S("fr4_counter",6.6,(.5,.5),(1.1,1.2)), S("fr4_counter",9.8,(.7,.35),(1.8,1.95)),
 S("fr4_stare",12.5,(.3,.6),(1.5,1.65)), S("fr4_stare",16.0,(.5,.5),W), S("fr4_stare",17.4,(.72,.4),(1.8,1.95)),
 S("fr4_stare",18.6,(.3,.45),(1.7,1.85)), S("fr4_stare",19.9,(.72,.4),(1.6,1.75)),
 S("fr4_grab",23.4,(.5,.5),W), S("fr4_grab",25.0,(.65,.55),(1.6,1.75)), S("fr4_grab",27.2,(.78,.68),(1.9,2.05)),
 S("fr4_empty",29.8,(.5,.5),W), S("fr4_empty",30.8,(.68,.45),(1.6,1.75)), S("fr4_empty",32.5,(.3,.5),(1.7,1.85)),
 S("fr4_empty",34.9,(.7,.4),(1.7,1.85)), S("fr4_empty",37.3,(.3,.4),(1.9,2.05)),
 S("fr4_counter",39.6,(.5,.5),(1.1,1.2)), S("fr4_counter",42.0,(.3,.4),(1.7,1.85)),
 S("fr4_two",44.2,(.68,.45),(1.6,1.75)), S("fr4_two",45.9,(.65,.6),(1.4,1.5)), S("fr4_two",47.5,(.5,.5),W),
],[
 B(9.8,12.3,"nah I'm good. I'm not hungry",.62,.22,(.7,.33)),
 C(13.2,15.6,"1 LARGE FRIES (FOR YOU)"),
 B(19.9,21.6,"can I just have one?",.62,.2,(.72,.3)),
 C(21.7,23.3,"ONE.",.34), C(24.1,25.0,"THREE.",.34), C(26.3,27.1,"THE BIGGEST ONE",.34),
 C(29.8,31.2,"10 MINUTES LATER",.34),
 B(34.9,37.2,"these are so good, man",.6,.2,(.7,.3)),
 C(38.1,39.5,"YOU PAID FOR THEM"),
 C(40.6,41.9,"2 LARGE FRIES",.34), C(42.0,43.9,"one for you. one for him.",.34),
 B(44.2,45.8,"I'm not hungry",.62,.2,(.68,.3)),
 C(46.0,47.4,"ATE BOTH.",.34),
],[(21.7,"pop"),(24.2,"pop"),(38.2,"sad"),(46.0,"boom")])

# ---------- Group chat pt4 ----------
R("gc4","group_chat_pt4",["Every Type of Person","in a Group Chat","Explained pt 4"],54.6,[
 S("gc4_laugh",0,(.5,.5),W), S("gc4_laugh",4.8,(.5,.45),(1.5,1.65)),
 S("gc4_buzz",7.4,(.5,.5),W), S("gc4_buzz",12.0,(.5,.5),(1.1,1.2)), S("gc4_buzz",13.8,(.65,.72),(1.9,2.05)),
 S("gc4_buzz",19.6,(.4,.4),(1.4,1.55)), S("gc4_laugh",22.6,(.5,.5),W), S("gc4_laugh",24.0,(.5,.4),(1.7,1.85)),
 S("gc4_laugh",27.3,(.5,.5),(1.0,1.05)),
 S("gc4_duck",30.8,(.5,.5),W), S("gc4_duck",34.2,(.5,.3),(1.8,1.95)),
 S("gc4_panic",35.6,(.5,.5),W), S("gc4_panic",38.6,(.6,.35),(1.6,1.75)),
 S("gc4_duck",40.8,(.5,.45),(1.1,1.15)),
 S("gc4_asleep",42.2,(.5,.5),W), S("gc4_asleep",44.2,(.42,.3),(1.7,1.85)),
 S("gc4_laugh",48.7,(.5,.5),W),
],[
 P(7.4,11.9,[(7.5,"Jay","ok see you guys")],"right","2 weeks ago"),
 C(10.4,11.9,"*silence*",.34),
 C(12.0,13.7,"3:00 AM",.34),
 P(15.4,19.5,[(15.5,"Leo","LMAOOO"),(16.6,"Leo","wait this one"),(17.8,"Leo","and this"),(18.2,"Leo","and this"),(18.6,"Leo","HAHAHA")],"left","3:01"),
 C(19.6,20.8,"NOBODY ASKED",.34), C(20.9,22.5,"NOBODY IS AWAKE",.34),
 C(26.2,27.2,"ALONE.",.34), C(27.3,28.6,"IN THE DARK.",.34),
 P(28.7,30.7,[(28.8,"Leo","when the when u"),(29.6,"Leo","bro im crying")],"left","3:04"),
 C(33.1,34.1,"NO CAPTION.",.34), C(34.2,35.5,"JUST A DUCK.",.34),
 C(36.4,38.5,"47 NOTIFICATIONS",.62),
 C(40.8,42.1,"IT'S THE DUCK.",.34),
 C(45.4,48.6,"NEXT REPLY: 3:00 AM",.34),
],[(14.5,"pop"),(15.5,"pop"),(16.6,"pop"),(17.8,"pop"),(36.5,"boom"),(40.9,"sad")])

# ---------- Cinema pt4 ----------
R("cn4","cinema_pt4",["Every Type of Person","at the Cinema","Explained pt 4"],52.9,[
 S("cn4_kick",0,(.5,.5),W), S("cn4_kick",4.6,(.35,.3),(1.6,1.75)),
 S("cn4_happy",6.2,(.5,.5),W), S("cn4_happy",8.1,(.5,.45),(1.4,1.5)), S("cn4_happy",10.7,(.5,.2),(1.4,1.5)),
 S("cn4_happy",12.1,(.5,.45),(1.7,1.85)),
 S("cn4_kick",14.2,(.6,.45),(1.5,1.6)), S("cn4_happy",15.4,(.5,.45),(1.5,1.6)),
 S("cn4_kick",17.0,(.62,.5),(1.7,1.85)), S("cn4_kick",17.9,(.6,.45),(1.9,2.05)),
 S("cn4_kick",20.2,(.5,.5),W), S("cn4_kick",21.4,(.33,.3),(1.7,1.85)),
 S("cn4_thumbs",26.5,(.4,.6),(1.7,1.85)), S("cn4_thumbs",27.8,(.7,.3),(1.8,1.95)),
 S("cn4_kick",29.4,(.5,.5),W), S("cn4_kick",32.3,(.45,.3),(1.8,1.95)), S("cn4_kick",34.0,(.62,.55),(1.6,1.7)),
 S("cn4_kick",36.3,(.55,.4),(2.0,2.15)),
 S("cn4_happy",39.5,(.5,.45),(1.2,1.3)), S("cn4_thumbs",43.8,(.5,.5),W), S("cn4_thumbs",46.6,(.7,.3),(1.6,1.7)),
 S("cn4_kick",48.2,(.5,.5),W),
],[
 C(7.4,9.3,"PERFECT SEAT",.34),
 C(13.3,14.1,"*THUMP*",.34),
 C(17.0,17.8,"*THUMP*",.34), C(17.9,18.7,"*THUMP*",.34), C(18.8,20.1,"NOT AN ACCIDENT",.34),
 C(24.3,26.4,"5-STAR HOME SOFA",.34),
 C(30.3,32.2,"ACTION SCENE",.34),
 C(34.6,36.2,"FREE MASSAGE CHAIR",.34),
 C(41.5,43.6,"MORE KICKS THAN THE BAD GUY",.34),
 B(46.6,48.1,"great seats, right?",.4,.22,(.62,.3)),
],[(13.4,"boom"),(17.0,"boom"),(17.9,"boom"),(28.4,"pop"),(32.6,"boom"),(33.2,"boom"),(46.7,"sad")])

# ---------- Sibling pt4 ----------
R("sb4","sibling_pt4",["Every Type of Sibling","Explained pt 4"],51.7,[
 S("sb4_walk",0,(.5,.5),W), S("sb4_walk",4.0,(.7,.4),(1.6,1.75)),
 S("sb4_mirror",5.4,(.3,.3),(1.6,1.75)), S("sb4_mirror",6.9,(.5,.5),W), S("sb4_mirror",7.8,(.72,.35),(1.6,1.75)),
 S("sb4_guitar",9.5,(.4,.6),(1.4,1.5)), S("sb4_guitar",11.4,(.65,.25),(1.7,1.85)),
 S("sb4_dinner",13.7,(.2,.45),(1.7,1.85)), S("sb4_dinner",15.6,(.5,.5),W), S("sb4_dinner",18.3,(.78,.3),(1.6,1.75)),
 S("sb4_dinner",21.0,(.45,.4),(1.7,1.85)),
 S("sb4_walk",22.7,(.5,.5),(1.05,1.12)), S("sb4_walk",31.8,(.5,.5),W), S("sb4_walk",33.1,(.7,.45),(1.6,1.75)),
 S("sb4_walk",36.0,(.5,.5),(1.15,1.2)),
 S("sb4_jacket",37.3,(.3,.45),(2.0,2.1)), S("sb4_jacket",43.8,(.5,.5),W), S("sb4_jacket",44.6,(.72,.5),(1.6,1.75)),
 S("sb4_jacket",46.9,(.5,.5),W),
],[
 C(5.4,6.8,"NEW HAIRCUT",.62), C(6.9,7.7,"NEXT DAY",.34),
 C(17.1,18.2,"5 MINUTES LATER",.34), C(20.0,20.9,"LOUDER.",.34),
 B(22.7,24.8,"stop copying me",.3,.28,(.3,.4)),
 B(24.9,27.3,"stop copying me",.7,.28,(.7,.4)),
 B(27.4,29.5,"I'm serious",.3,.28,(.3,.4)),
 B(29.6,31.7,"I'm serious",.7,.28,(.7,.4)),
 C(34.4,35.9,"SAME DIRECTION",.34), C(36.0,37.2,"BEHIND YOU",.34),
 C(37.3,38.9,"YEARS LATER",.34), C(39.5,42.7,"your own style. finally.",.34),
 C(44.6,46.8,"YOUR. EXACT. JACKET.",.34),
],[(21.0,"cheer"),(43.9,"boom")])
print("ok")

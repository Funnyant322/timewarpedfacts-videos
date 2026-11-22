import json
S=lambda img,t,f,z: {"img":img,"t":t,"focus":list(f),"zoom":list(z)}
C=lambda s,e,text,y=.34: {"type":"card","start":s,"end":e,"text":text,"y":y}
B=lambda s,e,text,x,y,tail: {"type":"bubble","start":s,"end":e,"text":text,"x":x,"y":y,"tail":list(tail)}
W=(1.0,1.08)
def P(s,e,msgs,side,clock,title,av="Leo",me="Sam",group=True):
    return {"type":"phone","start":s,"end":e,"scale":1.2,"side":side,"group":group,"me":me,"title":title,"title_av":av,"clock":clock,
            "msgs":[{"t":t,"from":f,"text":x} for t,f,x in msgs]}
def R(n,out,title,end,scenes,ov,sfx,music=True):
    d={"out":out,"voice":n+"_vo.mp3","words":n+"_words.json","end":end,"title":title,"footer":["Follow for","more"],
       "scenes":scenes,"overlays":ov,"sfx_events":[{"t":t,"kind":k} for t,k in sfx]}
    if music: d.update(music="music_comedy1.mp3",music_vol=0.35)
    json.dump(d,open(n+".json","w"),indent=1)

# ---------- Friend pt6: every type at once ----------
R("fr6","friend_pt6",["Every Type of Friend","Explained pt 6"],53.2,[
 S("fr3_door",0,(.5,.5),W), S("fr3_door",4.3,(.4,.3),(1.5,1.65)),
 S("fr3_text",8.9,(.5,.5),W), S("fr3_text",13.1,(.5,.35),(1.5,1.6)),
 S("gc4_asleep",16.7,(.5,.5),W),
 S("cafe_waiting",18.1,(.5,.5),(1.0,1.1)), S("fr2_pockets",20.2,(.3,.4),(1.5,1.65)),
 S("fr4_counter",21.8,(.5,.5),W), S("fr4_counter",23.0,(.7,.4),(1.4,1.55)),
 S("fr4_grab",24.7,(.6,.5),(1.2,1.3)), S("fr4_stare",26.6,(.5,.45),(1.3,1.45)),
 S("fr4_two",27.8,(.7,.4),(1.3,1.45)),
 S("fr2_receipt",29.9,(.5,.6),W), S("fr2_pockets",31.1,(.3,.4),(1.6,1.75)), S("fr2_pockets",33.0,(.3,.35),(2.0,2.15)),
 S("fr3_game_night",34.2,(.5,.5),W), S("fr3_game_sunrise",36.9,(.5,.5),W),
 S("fr5_midnight",38.6,(.35,.65),(1.5,1.6)), S("fr5_midnight",41.4,(.6,.35),(1.5,1.65)),
 S("fr4_stare",44.5,(.6,.4),(1.3,1.4)),
 S("fr5_cafe",46.0,(.5,.5),W), S("fr5_cafe",48.0,(.6,.4),(1.5,1.6)), S("fr5_cafe",49.4,(.5,.5),W),
],[
 P(9.0,16.6,[(9.9,"You","where are you?"),(12.2,"Leo","parking."),(15.3,"Leo","5 mins away")],"right","7:00 PM","Leo",me="You",group=False),
 C(13.2,14.5,"HE HAS NO CAR.",.62),
 C(16.8,18.0,"STILL IN BED",.62),
 C(18.2,20.1,"1 HOUR LATE"),
 C(20.3,21.7,"WALLET: AT HOME",.62),
 B(23.1,24.6,"I'm not hungry.",.72,.22,(.72,.34)),
 C(26.7,27.7,"ONE. AT. A. TIME.",.62),
 B(27.9,29.8,"I'm on a diet.",.7,.2,(.7,.32)),
 C(31.2,32.9,"*pat pat pat*",.62), C(33.1,34.1,"TWICE."),
 B(34.3,36.8,"one more game.",.5,.2,(.4,.36)),
 C(37.0,38.5,"4:00 AM"),
 B(41.5,44.4,"guys. we need to go on a trip.",.5,.2,(.62,.32)),
 C(44.6,45.9,"YOU SHOULD HATE HIM."),
 C(46.1,49.3,"BEST FRIEND.",.62),
],[(9.9,"pop"),(12.2,"ding"),(13.2,"boom"),(15.3,"ding"),(16.8,"sad"),(20.3,"sad"),(24.8,"crunch"),(26.7,"crunch"),(33.1,"boom"),(37.0,"ding"),(41.9,"boom"),(46.1,"cheer")])

# ---------- Group chat pt6: leaves the group ----------
R("gc6","group_chat_pt6",["Every Type of Person","in a Group Chat","Explained pt 6"],50.3,[
 S("gc4_scroll",0,(.5,.5),W), S("gc3_phantom",5.0,(.5,.4),(1.2,1.3)),
 S("gc4_typer",8.4,(.5,.5),W), S("gc4_typer",12.6,(.5,.45),(1.3,1.4)), S("gc3_cafe",15.8,(.5,.45),(1.2,1.3)),
 S("gc5_shock",20.9,(.5,.5),W), S("gc5_shock",22.0,(.5,.4),(1.4,1.5)),
 S("gc5_committee",23.4,(.5,.5),W), S("gc5_committee",25.9,(.5,.5),(1.15,1.25)),
 S("gc5_typing",29.4,(.5,.45),(1.1,1.2)),
 S("gc4_laugh",33.4,(.5,.5),W), S("gc4_laugh",35.4,(.5,.4),(1.4,1.5)),
 S("gc4_typer",36.8,(.5,.5),W),
 S("gc3_cafe",40.0,(.5,.5),W), S("gc5_shock",42.6,(.5,.4),(1.3,1.4)), S("gc4_laugh",43.6,(.5,.4),(1.3,1.4)),
 S("gc4_scroll",45.0,(.5,.5),W),
],[
 P(8.5,20.8,[(10.8,"Maya","pineapple on pizza is elite"),(11.6,"Sam","absolutely not"),(13.3,"Ben","[voice note 7:02]"),(17.1,"Leo","k"),(19.1,"Leo","*left the group*")],"right","9:14 PM","Squad"),
 C(21.0,21.9,"SILENCE."),
 C(23.5,25.8,"12 PEOPLE. STARING."),
 P(26.0,33.3,[(27.0,"Maya","should we add him back?"),(29.4,"Ben","no."),(31.8,"Sam","*added Leo*")],"right","9:20 PM","Squad"),
 C(30.4,31.7,"5 MINUTES LATER",.2),
 B(35.5,36.7,"what did I miss?",.5,.2,(.5,.34)),
 C(37.0,39.9,"*like nothing happened*",.62),
 C(40.1,41.3,"NEXT WEEK"),
 C(41.4,42.5,"SAME ARGUMENT",.62), C(42.6,43.5,"SAME EXIT",.62), C(43.6,44.9,"SAME COMEBACK",.62),
],[(10.8,"pop"),(11.6,"pop"),(13.3,"pop"),(17.1,"ding"),(19.1,"boom"),(21.0,"sad"),(27.0,"pop"),(29.4,"ding"),(31.8,"pop"),(35.5,"ding"),(42.6,"boom")])

# ---------- Cinema pt6: claps at the end ----------
R("cn6","cinema_pt6",["Every Type of Person","at the Cinema","Explained pt 6"],49.5,[
 S("cinema_quiet",0,(.5,.5),W), S("cn4_happy",4.7,(.5,.5),(1.1,1.2)),
 S("cinema_quiet",8.9,(.55,.35),(1.4,1.5)), S("cn2_sun",10.2,(.5,.5),W), S("cn2_behind",11.8,(.5,.5),W),
 S("cn4_happy",14.0,(.5,.5),(1.0,1.05)), S("cn4_happy",15.3,(.5,.5),(1.3,1.35)), S("cn4_happy",16.2,(.5,.5),(1.55,1.6)), S("cn4_happy",17.0,(.5,.5),(1.8,1.85)),
 S("cinema_quiet",17.9,(.35,.65),(1.6,1.75)),
 S("cinema_quiet",21.8,(.6,.4),(1.8,1.95)),
 S("cn4_thumbs",27.0,(.4,.6),(1.2,1.3)),
 S("cn4_happy",29.8,(.5,.5),(1.4,1.55)),
 S("cn2_behind",31.5,(.5,.4),(1.3,1.45)), S("cn5_row",35.6,(.45,.6),(1.5,1.6)),
 S("cn5_toilet",36.7,(.5,.5),W), S("cn5_toilet",38.7,(.5,.5),(1.1,1.2)),
 S("cn3_glare",40.5,(.5,.5),(1.0,1.1)),
 S("cn4_happy",42.8,(.5,.5),W),
],[
 C(9.0,10.1,"THE END"),
 C(10.3,11.7,"*LIGHTS ON*"),
 C(11.9,13.9,"*everyone leaves quietly*",.62),
 C(15.3,16.1,"CLAP."), C(16.2,16.9,"CLAP."), C(17.0,17.8,"CLAP."),
 C(19.1,21.7,"ALONE.",.62),
 C(22.0,23.3,"THE DIRECTOR: NOT HERE"), C(23.5,24.8,"THE ACTORS: NOT HERE"), C(25.0,26.9,"THE SCREEN: CAN'T HEAR YOU"),
 C(27.1,28.5,"NOBODY JOINS IN.",.62),
 C(30.1,31.4,"*CLAPS LOUDER*"),
 C(32.2,35.5,"OLD MAN: *clap*",.62),
 C(35.9,36.6,"A KID: *clap*",.62),
 C(38.8,40.4,"STANDING OVATION"),
 C(41.0,42.7,"THE FILM: TERRIBLE",.62),
 C(44.1,45.0,"LEGEND."),
],[(9.0,"ding"),(10.3,"boom"),(15.3,"pop"),(16.2,"pop"),(17.0,"pop"),(19.1,"sad"),(25.0,"sad"),(30.1,"pop"),(30.5,"pop"),(32.2,"pop"),(35.9,"pop"),(37.4,"cheer"),(41.0,"sad"),(44.1,"boom")],music=False)

# ---------- Sibling pt6: secretly your best friend ----------
R("sb6","sibling_pt6",["Every Type of Sibling","Explained pt 6"],37.5,[
 S("sb4_mirror",0,(.5,.5),W), S("sb4_mirror",4.2,(.5,.4),(1.3,1.4)),
 S("sb4_jacket",8.3,(.65,.45),(1.2,1.3)), S("sb2_snitch",9.8,(.5,.55),(1.3,1.4)), S("sb4_walk",11.2,(.5,.5),W),
 S("sb5_knock",13.3,(.5,.5),W), S("sb3_kitchen",15.0,(.5,.5),W),
 S("sb4_walk",18.6,(.7,.35),(1.4,1.5)), S("fr3_beg",21.1,(.75,.25),(1.8,1.95)),
 S("sb5_mum",24.3,(.5,.5),W), S("sb5_mum",25.6,(.35,.4),(1.5,1.6)),
 S("gc3_bed_buzz",27.2,(.5,.5),(1.0,1.1)),
 S("sb4_jacket",30.4,(.5,.5),W), S("sb4_mirror",32.8,(.5,.5),W),
],[
 C(8.4,9.7,"YOUR HOODIE",.62),
 C(15.1,18.5,"THE TV REMOTE: WAR",.62),
 C(21.9,24.2,"*SCARIEST PERSON ALIVE*"),
 B(25.8,27.1,"it was me too.",.4,.2,(.35,.32)),
 C(27.3,30.3,"2:00 AM"),
 C(30.5,32.7,"STILL YOUR HOODIE.",.62),
],[(8.6,"pop"),(10.1,"ding"),(13.5,"pop"),(15.8,"crunch"),(21.8,"boom"),(25.8,"ding"),(27.5,"sad"),(31.0,"pop")])
print("ok")

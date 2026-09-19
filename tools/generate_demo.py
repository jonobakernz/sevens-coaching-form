import random, json, csv, io, statistics
from datetime import datetime, timezone, timedelta
from collections import Counter
random.seed(21)
NZ = timezone(timedelta(hours=12))
AREAS = ['fitness','foul','breakdown','setphase','awareness','management','communication']
REFS = {
 'Aroha Pene':   dict(fitness=4.7, foul=4.6, breakdown=4.6, setphase=4.5, awareness=4.7, management=4.6, communication=4.8),
 'Hemi Walker':  dict(fitness=4.7, foul=3.6, breakdown=4.0, setphase=4.0, awareness=4.1, management=3.9, communication=4.0),
 'Sione Tuala':  dict(fitness=3.9, foul=3.9, breakdown=3.8, setphase=4.3, awareness=3.8, management=3.9, communication=3.3),
 'Priya Nair':   dict(fitness=3.8, foul=3.9, breakdown=3.1, setphase=3.8, awareness=3.7, management=3.7, communication=3.9),
 'Tom Hale':     dict(fitness=3.4, foul=3.6, breakdown=3.5, setphase=3.4, awareness=3.4, management=3.5, communication=3.5),
 'Lucy Parata':  dict(fitness=4.0, foul=4.2, breakdown=4.0, setphase=3.9, awareness=4.1, management=4.2, communication=4.7),
 'Ethan Cole':   dict(fitness=3.1, foul=2.4, breakdown=2.9, setphase=3.1, awareness=2.8, management=2.9, communication=3.1),
 'Manu Faleolo': dict(fitness=3.7, foul=3.5, breakdown=3.7, setphase=3.6, awareness=3.6, management=3.5, communication=3.6),
 'Jordan Wu':    dict(fitness=4.0, foul=3.8, breakdown=3.9, setphase=3.9, awareness=4.0, management=3.8, communication=3.7),
 'Kiri Ngata':   dict(fitness=4.6, foul=4.5, breakdown=4.5, setphase=4.4, awareness=4.5, management=4.4, communication=4.6),
 'Ben Walker':   dict(fitness=3.6, foul=3.4, breakdown=3.5, setphase=3.5, awareness=3.4, management=3.6, communication=3.5),
 'Anika Brown':  dict(fitness=3.8, foul=3.7, breakdown=3.7, setphase=3.6, awareness=3.8, management=3.7, communication=3.8),
}
COACHES = {'Dave Rangi':-0.45, 'Hannah Price':0.30, 'Wiremu Ashby':0.0, 'Lena Fischer':0.10}
PLAN = {
 'Aroha Pene':['Dave Rangi','Hannah Price','Wiremu Ashby','Lena Fischer','Dave Rangi'],
 'Hemi Walker':['Hannah Price','Lena Fischer','Wiremu Ashby','Dave Rangi','Hannah Price'],
 'Sione Tuala':['Wiremu Ashby','Dave Rangi','Lena Fischer','Wiremu Ashby'],
 'Priya Nair':['Lena Fischer','Hannah Price','Wiremu Ashby','Lena Fischer'],
 'Tom Hale':['Dave Rangi','Wiremu Ashby','Dave Rangi','Lena Fischer'],
 'Lucy Parata':['Hannah Price','Wiremu Ashby','Lena Fischer','Hannah Price'],
 'Ethan Cole':['Dave Rangi','Dave Rangi','Dave Rangi'],
 'Manu Faleolo':['Hannah Price','Lena Fischer','Hannah Price'],
 'Jordan Wu':['Lena Fischer','Wiremu Ashby'],
 'Kiri Ngata':['Hannah Price'],
 'Ben Walker':['Wiremu Ashby','Hannah Price','Lena Fischer','Wiremu Ashby','Dave Rangi'],
}
FINALS_COUNT={'Aroha Pene':3,'Hemi Walker':3,'Lucy Parata':2,'Sione Tuala':2,'Priya Nair':2,'Manu Faleolo':1,'Jordan Wu':1,'Kiri Ngata':1,'Ben Walker':1,'Tom Hale':0,'Ethan Cole':0}
SENIORITY=['Aroha Pene','Hemi Walker','Lucy Parata','Sione Tuala','Priya Nair','Jordan Wu','Manu Faleolo','Kiri Ngata','Ben Walker']
AR_GAMES = [('Jordan Wu','Assistant referee 1','Wiremu Ashby',True),('Anika Brown','Assistant referee 1','Lena Fischer',True),('Anika Brown','Assistant referee 2','Hannah Price',True),('Ben Walker','Assistant referee 2','Dave Rangi',False),('Lucy Parata','Assistant referee 1','Wiremu Ashby',True)]
LOW={ 'fitness':['Fell behind play after the second restart.','Late to the breakdown twice in the second half.','Struggled with the pace in the last two minutes.'],
 'foul':['Missed a high tackle in the first half.','Yellow card shown without a clear warning first.','Inconsistent at the tackle, players confused.'],
 'breakdown':['Slow to see the ball on the ground. Penalty came late.','Missed a hand in the ruck twice.','Turnover call was slow and unclear.'],
 'setphase':['Kick-off signals were unclear.','Slow to reset after the try. Lost time.','Scrum crouch, bind, set was rushed.'],
 'awareness':['Lost sight of the ball at the breakdown.','Late to see offside on the far side.','Got in the way of the passing lane twice.'],
 'management':['Slow to manage the players after the sin-bin.','Clock use was loose in the second half.','Let a heated moment run too long.'],
 'communication':['Signals were late and players asked for reasons.','Voice was quiet, whistle was hesitant.','Talked over the captain at a key moment.']}
HIGH={ 'fitness':['Always on the ball line. Quick recovery after turnovers.','Kept up with play the whole game.'],
 'foul':['Early warning, then a clear yellow. Players understood.','Consistent sanctions, calm and firm.','Managed head contact very well.'],
 'breakdown':['Clear tackle release calls. Quick, accurate turnover decisions.','Good picture at the ruck, no wasted words.'],
 'setphase':['Quick, clean restarts all game.','Clear kick-off signals, no confusion.'],
 'awareness':['Read the play early and was well placed for the try.','Good use of advantage.'],
 'management':['Good clock and advantage use. Calm at key moments.','Handled the sin-bin restart well.'],
 'communication':['Strong whistle, clear voice.','Calm with players, short clear reasons.']}
KEEP=['Stayed on the ball line all game.','Clear voice and calm manner.','Strong advantage calls.','Quick decisions at the breakdown.','Firm and fair with players.','Good early warnings.']
WORK=['Call the tackle release earlier.','Get closer to the contest without getting in the way.','Explain decisions in fewer words.','Keep pace late in the day.','Be clear on the kick-off signal.','Use the warning before the yellow card.','Watch the offside line on the far side.']
PRIV_HI=['Ready for Cup games.','Recommend for the regional panel.','Good candidate for a mentoring role.']
PRIV_MID=['Steady. Give a Cup pool game to test.','Needs a second look at foul play.']
PRIV_LO=['Needs fitness work before the next event.','Discuss foul play judgement at the debrief.','Not ready for Cup games yet.']
def clip(x): return max(1,min(5,int(round(x))))

pool_slots=[('Pool play',t,f) for t in [f'{h:02d}:{m:02d}' for h in (9,10,11) for m in (0,20,40)] for f in (1,2,3,4)]
pool_slots=sorted(random.sample(pool_slots,25),key=lambda s:(s[1],s[2]))
fin=[('Cup','15:00',1,'Cup final'),('Cup','14:20',1,'Cup 3rd place play-off'),('Plate','15:00',2,'Plate final'),('Bowl','15:00',3,'Bowl final'),('Plate','14:40',2,'Plate 3rd place play-off'),('Bowl','14:40',3,'Bowl 3rd place play-off'),
 ('Cup','13:40',1,'Cup semi-final 1'),('Cup','13:40',2,'Cup semi-final 2'),('Plate','14:00',1,'Plate semi-final 1'),('Plate','14:00',2,'Plate semi-final 2'),('Bowl','14:00',3,'Bowl semi-final 1'),('Bowl','14:00',4,'Bowl semi-final 2'),
 ('Cup','13:00',1,'Cup quarter-final 1'),('Cup','13:00',2,'Cup quarter-final 2'),('Cup','13:00',3,'Cup quarter-final 3'),('Cup','13:00',4,'Cup quarter-final 4'),
 ('Plate','13:20',1,'Plate quarter-final 1'),('Plate','13:20',2,'Plate quarter-final 2'),('Bowl','13:20',3,'Bowl quarter-final 1'),('Bowl','13:20',4,'Bowl quarter-final 2')]
pc={'A':0,'B':0,'C':0,'D':0}; pool_named=[]
for i,(lv,t,f) in enumerate(pool_slots):
    p='ABCD'[i%4]; pc[p]+=1; pool_named.append((lv,t,f,f'Pool {p}, game {pc[p]}'))
tasks=[]
for ref,coaches in PLAN.items():
    k=FINALS_COUNT[ref]
    for j,c in enumerate(coaches): tasks.append(dict(ref=ref,role='Referee',coach=c,j=j,tot=len(coaches),fin=(j>=len(coaches)-k)))
for ref,role,c,fin_flag in AR_GAMES: tasks.append(dict(ref=ref,role=role,coach=c,j=0,tot=1,fin=fin_flag))
fin_tasks=[t for t in tasks if t['fin']]; pool_tasks=[t for t in tasks if not t['fin']]
assert len(fin_tasks)==len(fin) and len(pool_tasks)==len(pool_named)

# finals: greedy by seniority, most important free slot where the person is not already busy at that time
ref_fin=sorted([t for t in fin_tasks if t['role']=='Referee'],key=lambda t:(SENIORITY.index(t['ref']),t['j']))
ar_fin=[t for t in fin_tasks if t['role']!='Referee']
busy={}; free=list(fin); final_assign=[]
for t in ar_fin+ref_fin:
    cands=[s for s in free if s[1] not in busy.get(t['ref'],set())]
    if t['role']!='Referee': cands=[s for s in cands if 'quarter' in s[3]] or cands
    s=cands[0]; free.remove(s); busy.setdefault(t['ref'],set()).add(s[1]); final_assign.append((t,s))
# a referee's own finals games in j order = time order
byp={}
for t,s in final_assign: byp.setdefault((t['ref'],t['role']),[]).append((t,s))
fa=[]
for k,lst in byp.items():
    ts=sorted([x[0] for x in lst],key=lambda t:t['j']); ss=sorted([x[1] for x in lst],key=lambda s:(s[1],s[2])); fa+=list(zip(ts,ss))
final_assign=fa
# pool: retry until nobody has two games at the same time and each referee's games run in order
for attempt in range(20000):
    pt=pool_tasks[:]; random.shuffle(pt); pt.sort(key=lambda t:(t['j']/t['tot']+random.random()*0.4))
    pa=list(zip(pt,pool_named)); ok=True; seen={}
    for t,s in pa:
        key=(t['ref'],s[1])
        if key in seen: ok=False; break
        seen[key]=1
    if ok:
        last={}
        for t,s in sorted(pa,key=lambda x:(x[1][1],x[1][2])):
            if t['role']!='Referee': continue
            if last.get(t['ref'],-1)>t['j']: ok=False; break
            last[t['ref']]=t['j']
    if ok: break
assert ok,'no valid pool draw'
allas=sorted(final_assign+pa,key=lambda x:(x[1][1],x[1][2]))
forms=[]
for n,(t,(level,tm,fld,label)) in enumerate(allas,1):
    ref,role,coach,j=t['ref'],t['role'],t['coach'],t['j']
    bias=COACHES[coach]; hour=int(tm[:2])+int(tm[3:])/60; sc={}
    for a in AREAS:
        mean=REFS[ref][a]+bias*0.85
        if a=='fitness' and ref=='Tom Hale': mean-=max(0,(hour-9.5))*0.55
        sc[a]=clip(random.gauss(mean,0.45))
    sc['rating']=clip(random.gauss(sum(sc.values())/7+bias*0.3,0.25))
    comments={}
    for a in AREAS:
        if random.random()<(0.8 if sc[a]<=2 or sc[a]>=5 else 0.22): comments[a]=random.choice(LOW[a] if sc[a]<=3 else HIGH[a])
    tc=iw=gp=False
    if sc['awareness']<=2:
        if random.random()<0.6: tc=True
        else: iw=True
        comments['contest']=random.choice(['Kept drifting into the passing lane.','Too tight to the ruck on the near side.'])
    elif sc['awareness']>=4 and random.random()<0.55: gp=True
    keep=random.choice(KEEP) if random.random()<0.8 else ''
    work=random.choice(WORK) if random.random()<0.8 else ''
    r=sc['rating']; priv=''
    if random.random()<0.32: priv=random.choice(PRIV_HI if r>=4 else PRIV_MID if r==3 else PRIV_LO)
    dt=datetime(2026,9,19,int(tm[:2]),int(tm[3:]),tzinfo=NZ)
    upd=int((dt+timedelta(minutes=random.randint(14,24))).timestamp()*1000)
    name='Priya Naire' if (ref=='Priya Nair' and t['tot']-j in (1,3)) else ref
    forms.append({'id':f'demo-{n:03d}','coach':coach,'tournament':'Demo Sevens 2026','level':level,'game':label,'role':role,'referee':name,'field':str(fld),'time':tm,'date':'2026-09-19',
      'scores':sc,'comments':comments,'tooClose':tc,'inWay':iw,'goodPos':gp,'keep':keep,'work':work,'priv':priv,
      'created':upd-1500000,'updated':upd,'uploadedAt':upd+120000,'uploadedVersion':upd})
config={'v':1,'t':'Demo Sevens 2026','c':'demo','f':['1','2','3','4'],'r':list(REFS.keys()),'k':list(COACHES.keys()),'l':['Pool play','Cup','Plate','Bowl','Final']}
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','demo')+os.sep
json.dump({'config':config,'forms':forms},open(D+'demo.json','w'),ensure_ascii=False,separators=(',',':'))
json.dump({'app':'sevens-form','version':2,'forms':forms},open(D+'demo-backup.json','w'),ensure_ascii=False,indent=1)
cols=['form_id','version','code','tournament','level','game','date','time','field','referee','role','coach']
for a in AREAS+['rating']: cols+=['score_'+a,'comment_'+a]
cols+=['too_close','in_the_way','good_position','contest_comments','keep','work','private_notes']
buf=io.StringIO(); w=csv.writer(buf); w.writerow(cols)
for f in forms:
    row=[f['id'],f['updated'],'demo',f['tournament'],f['level'],f['game'],f['date'],f['time'],f['field'],f['referee'],f['role'],f['coach']]
    for a in AREAS+['rating']: row+=[f['scores'].get(a,''),f['comments'].get(a,'')]
    row+=['yes' if f['tooClose'] else '','yes' if f['inWay'] else '','yes' if f['goodPos'] else '',f['comments'].get('contest',''),f['keep'],f['work'],f['priv']]
    w.writerow(row)
open(D+'demo-results.csv','w',encoding='utf-8-sig').write(buf.getvalue())
rf=[f for f in forms if f['role']=='Referee']
print(len(forms),'forms',dict(Counter(f['level'] for f in forms)))
for c in COACHES: print(' ',c, round(statistics.mean(f['scores']['rating'] for f in rf if f['coach']==c),2))
by={}
for f in rf: by.setdefault(f['referee'].replace('Naire','Nair'),[]).append(f['scores']['rating'])
print({k:(round(statistics.mean(v),2),len(v)) for k,v in sorted(by.items(),key=lambda x:-statistics.mean(x[1]))})
# clash check
seen={}
clash=0
for f in forms:
    k=(f['referee'].replace('Naire','Nair'),f['time'])
    if k in seen: clash+=1
    seen[k]=1
print('double bookings:',clash)
print([(f['time'],f['game'],f['referee']) for f in forms if 'final' in f['game'] or '3rd' in f['game']])

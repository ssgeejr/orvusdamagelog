#import tailer
#import mysql.connector
import sqlite3
import os

global dbcon
global cur
cntr = 0

ford_dmg = 0.0
chevy_dmg = 0.0
ford_cnt = 0
chevy_cnt = 0
action_list = ["HEAL","COMBAT"]

def main(args=None):
    openConnection()
    preload()
    results()
    closeConnection()

def results():
    global dbcon, cur
    # cur.execute("select time,action,amount,source,target from orbus where target = 'Rushed Stafrusher(18320)' and action = 'COMBAT'")
    # cur.execute("select sum(amount),source,target from orbus where target = 'Rushed Stafrusher(18320)' and action = 'COMBAT' group by source");
#    cur.execute("select sum(amount) as totaldamage,source,target from orbus where action = 'COMBAT' group by source order by totaldamage desc");


    cur.execute("select max(time) as mx, min(time) as mn from orbus where target like 'Lich King%' and action = 'COMBAT' and time like '14:%' ");
    # cur.execute("select Cast(( JulianDay(max(time)) - JulianDay(min(time)) ) * 24 * 60 * 60 As Integer)from orbus where target like 'Lich King%' and action = 'COMBAT'");
    for row in cur:
        cmbseconds = (toseconds(row[0]) - toseconds(row[1]))
        print("Combat Seconds: %s" % cmbseconds)



    print("****RAW DAMAGE****")
    cur.execute("select time,amount,target,source from orbus where target like 'Lich King%' and action = 'COMBAT'  and time like '14:%' order by time");
    for row in cur:
        print(row)


    print("****TOTAL DAMAGE****")
    cur.execute("select sum(amount) as totaldamage,source,target from orbus where target like 'Lich King%' and action = 'COMBAT'  and time like '14:%' group by source,target order by target");
    for row in cur:
        print("Raw Damage [%s], DPS [%s], Player [%s]" % (row[0], dps(row[0],cmbseconds),row[1]))





    return

    print("*****COMBAT*****")
    cur.execute("select sum(amount) as totaldamage,source,target from orbus where action = 'COMBAT' group by source,target order by target");
    for row in cur:
        print(row)

    print("*****HEALING*****")
    cur.execute("select sum(amount) as totaldamage,source,target from orbus where action = 'HEAL' group by source, target order by totaldamage desc");
    for row in cur:
        print(row)
        # zz += 1
        # if zz > 10: exit(0)

def dps(x,y):
    try:
        return round(x/y,2)
    except ZeroDivisionError:
        return 0.00
def toseconds(time_str):
    # print("TIME_STR" + time_str)
    time_str = time_str[0:8]
    print(time_str)
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def openConnection():
    global dbcon, cur
    try:
        dbcon = sqlite3.connect(":memory:")
        #ensure we auto-commit
        dbcon.isolation_level = None
        print(dbcon)
        cur = dbcon.cursor()
        cur.execute("create table orbus(time,action,amount,source,target)")
#        cur.execute("insert into orbus(time,action,amount,source,target) values('20:52:38:001','HEAL',1000,'Stewdog','Bral')")
#        cur.execute("insert into orbus(time,action,amount,source,target) values('20:52:38:110','COMBAT',75,'Stewdog','Bral')")
#        cur.execute("select time,action,amount,source,target from orbus")

#        for row in cur:
#            print(row)

    except Exception as dbe:
        print("************ SOMETHING WENT TRAGICALLY WRONG (EXCEPTION) ****************")
        print(str(dbe))
        print("****************************************")
#    finally:
 #       dbcon.close()

def closeConnection():
    dbcon.close()

def parseline(line):
    global action_list, cur, dbcon
    if "You are" in line:
        return
#    print(line)
    if " [Combat] " in line:
        # print(line)
#start at 22
#        damagelog = line.
#        playerlog = line.split()
        try:
            i = 0
            time = line[0:12]
            tookloc = line.index(" took")
            # print("location %s" % tookloc)
            target = line[22:tookloc]
            # print("target [%s]" % target)
            # print(line[tookloc])
            playerlog = line[tookloc:].split()
            # print(playerlog)
            dmg_heelz = float( playerlog[1])
            dmg_heelz_type = 1
            if dmg_heelz < 0:
                # print("***HEALING***")
                dmg_heelz_type = 0
                dmg_heelz = dmg_heelz * -1
            # else:
                # print("***HEALING***")
#            TIME ACTION ACTION_KEY AMOUNT SOURCE TARGET CRITICAL ACTUAL
#             print(".............")
            # print("TIME: %s" % time)
            # print("ACTION: %s" % action_list[dmg_heelz_type])
            # print("ACTION_KEY: %s" % dmg_heelz_type)
            # print("AMOUNT: %s" % dmg_heelz)
            # print("SOURCE: %s" % playerlog[4])
            # print("TARGET: %s" % target)
            # print("CRITICAL: %s" % "NOT_IMPLEMENTED")
            # print("ACTUAL: %s" % line)
            # print(".............")
            cur.execute("insert into orbus(time,action,amount,source,target) values(?,?,?,?,?)" , (time,action_list[dmg_heelz_type],dmg_heelz,playerlog[4],target))


#            print(" >> target[%s] damage[%s] player[%s]" % (target,dmg_heelz,playerlog[3],))
#            while i < len(playerlog):
#                print("%s: %s" % (i, playerlog[i]))
#                i += 1

        except Exception as e:
            print("************ EXCEPTION ****************")
            print(line)
            print(str(e))
            #18:13:02:562 [Combat] You are now in combat.
            # exit(-1)
            return
            print("****************************************")


#        print(" >> target[%s] damage[%s] player[%s]" % (parsedlog[3], ))
#        print("1: %s" % parsedlog[1])
#        0: 18:08:15:329
#        1: [Combat]
#        2: Practicedummy(243)
#        3: took
#        4: 1535
#        5: damage
#        6: from
#        7: Rakan
 #       i = 0
 #       while i < len(parsedlog):
  #          print("%s: %s" % (i, parsedlog[i]))
  #          i += 1

#        exit(0)
#        print(" >> target[%s] damage[%s] player[%s] [%s]" % (parsedlog[2],parsedlog[4],parsedlog[7],line))


def preload():
    # print(".....preload.....")
    filepath = ("%s\AppData\LocalLow\Orbus Online, LLC\OrbusVR\combat.log" % os.environ['USERPROFILE'])
    print(filepath)
    global cntr
    with open(filepath) as fp:
        line = fp.readline()
        cntr = 0
#        brick = []
        while line:
            parseline(line)
            line = fp.readline()
            cntr += 1
#            if cntr == 15:
#               printdmg()

#    print("Ford Dmg: [%s]" % dps(ford_dmg, ford_cnt))
#    print("Chevy Dmg: [%s]" % dps(chevy_dmg, chevy_cnt))
#    print("..................................")
#    print("..................................")

if __name__ == "__main__":
    main()



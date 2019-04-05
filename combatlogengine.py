#import tailer
#import mysql.connector
import sqlite3

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
#    preload()
#    testtwo()
#    testthree()

def openConnection():
    global dbcon, cur
    try:
        dbcon = sqlite3.connect(":memory:")
        dbcon.isolation_level = None
        print(dbcon)
        cur = dbcon.cursor()
        cur.execute("create table orbus(ttime,)")
        cur.execute("insert into test(i) values (99)")
        cur.execute("insert into test(i) values (100)")
        cur.execute("select sum(i) from test")
        print(cur.fetchone()[0])
    except Exception as dbe:
        print("************ SOMETHING WENT TRAGICALLY WRONG (EXCEPTION) ****************")
        print(str(dbe))
        print("****************************************")
    finally:
        dbcon.close()

def mysqlConnection():
    global db
    try:
        db = mysql.connector.connect(user='combatengine', password='orbusdb',
                                  host='127.0.0.1',
                                  database='ORBUSDB')
        print(db)
    except Exception as dbe:
        print("************ SOMETHING WENT TRAGICALLY WRONG (EXCEPTION) ****************")
        print(str(dbe))
        print("****************************************")
    finally:
        db.close()

def testthree():
    print(".....TEST_TRE.....")
#    import tailer
    for line in tailer.follow(open('combat.log')):
        print(line)






def parseline(line):
    global action_list
    if "You are" in line:
        return
#    print(line)
    if " [Combat] " in line:
        print(line)
#start at 22
#        damagelog = line.
#        playerlog = line.split()
        try:
            i = 0
            time = line[0:12]
            tookloc = line.index(" took")
            print("location %s" % tookloc)
            target = line[22:tookloc]
            print("target [%s]" % target)
            print(line[tookloc])
            playerlog = line[tookloc:].split()
            print(playerlog)
            dmg_heelz = float( playerlog[1])
            dmg_heelz_type = 1
            if dmg_heelz < 0:
                print("***HEALING***")
                dmg_heelz_type = 0
            else:
                print("***HEALING***")
            TIME ACTION ACTION_KEY AMOUNT SOURCE TARGET CRITICAL ACTUAL
            print(".............")
            print("TIME: %s" % time)
            print("ACTION: %s" % action_list[dmg_heelz_type])
            print("ACTION_KEY: %s" % dmg_heelz_type)
            print("AMOUNT: %s" % dmg_heelz)
            print("SOURCE: %s" % playerlog[4])
            print("TARGET: %s" % target)
            print("CRITICAL: %s" % "NOT_IMPLEMENTED")
            print("ACTUAL: %s" % line)
            print(".............")

#            print(" >> target[%s] damage[%s] player[%s]" % (target,dmg_heelz,playerlog[3],))
#            while i < len(playerlog):
#                print("%s: %s" % (i, playerlog[i]))
#                i += 1

        except Exception as e:
            print("************ EXCEPTION ****************")
            print(line)
            print(str(e))
            #18:13:02:562 [Combat] You are now in combat.
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


def XparselineX(line):
    global ford_dmg, ford_cnt, chevy_dmg, chevy_cnt, cntr
#    print(line)
    brick = line.split('^')
    if brick[0] == 'Ford':
        ford_dmg += float(brick[1])
        ford_cnt = 1

    if brick[0] == 'Chevrolet':
        chevy_dmg += float(brick[1])
        chevy_cnt += 1

def printdmg():
    global ford_dmg, ford_cnt, chevy_dmg, chevy_cnt, cntr
    print("Ford Dmg: [%s]" % dps(ford_dmg, ford_cnt))
    print("Chevy Dmg: [%s]" % dps(chevy_dmg, chevy_cnt))
    print("..................................")
    cntr = 0
    ford_cnt = 0
    chevy_cnt = 0
    chevy_dmg = 0
    ford_dmg = 0


def preload():
    print(".....TEST_ONE.....")
    filepath = 'combat.out'
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


def dps(x,y):
    try:
        return round(x/y,2)
    except ZeroDivisionError:
        return 0.00

def testtwo():
    print(".....TEST_TWO.....")
    f = open('combat.log')
    p = 0
    while True:
     #   print('seeking ...')
        f.seek(p)
        latest_data = f.read()
        p = f.tell()
        if latest_data:
            print
            print(latest_data)
            print
#            str(p).center(10).center(80, '=')


if __name__ == "__main__":
    main()



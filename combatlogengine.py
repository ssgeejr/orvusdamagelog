import tailer

cntr = 0

ford_dmg = 0.0
chevy_dmg = 0.0
ford_cnt = 0
chevy_cnt = 0


def main(args=None):
    preload()
#    testtwo()
#    testthree()


def testthree():
    print(".....TEST_TRE.....")
#    import tailer
    for line in tailer.follow(open('combat.log')):
        print(line)


def parseline(line):
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
            tookloc = line.index(" took")
            print("location %s" % tookloc)
            target = line[22:tookloc]
            print("target [%s]" % target)
            print(line[tookloc])
            playerlog = line[tookloc:].split()
            print(playerlog)
            dmg_heelz = int( playerlog[1])
            dmg_heelz_type = 0
            if dmg_heelz > 0:
                print("***ATTACKING***")
                dmg_heelz_type = 1
            else:
                print("***HEALING***")




#            print(" >> target[%s] damage[%s] player[%s]" % (target,dmg_heelz,playerlog[3],))
            while i < len(playerlog):
                print("%s: %s" % (i, playerlog[i]))
                i += 1







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
    filepath = 'combat.log'
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



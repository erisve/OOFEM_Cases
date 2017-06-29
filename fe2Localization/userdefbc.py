def giveUserDefBC(iCoords, iDofNum, iTime):

    endTime = 1.
    dt = 0.1

    presVal = 0.0

    if iTime > 1.5*dt:
        presVal = 0.002*((iTime-dt)/endTime)

    return presVal


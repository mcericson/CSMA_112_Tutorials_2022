

def polyline(PointsX,PointsY,PointsZ):
    


    for h in range(len(PointsX)):
        PointsX1 = PointsX[h-h]
        PointsY1 = PointsY[h-h]
        PointsZ1 = PointsZ[h-h]

    for i in range(len(PointsX)):
        PointsX2 = PointsX[i]
        PointsY2 = PointsY[i]
        PointsZ2 = PointsZ[i]
        
        line(PointsX2,PointsY2,PointsX1,PointsY1)

        PointsX1 = PointsX2
        PointsY1 = PointsY2
        PointsZ1 = PointsZ2

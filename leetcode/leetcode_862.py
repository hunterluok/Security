
class Solutionss:
    def find(self, A, K):
        lens = len(A)
        if lens < 1:
            return -1

        maxs_len = float("inf")
        starts = 0
        sums = 0
        flag = False

        for ends in range(lens):
            second = A[ends]
            sums += second
            if second < 0:
                flag = True
            if sums >= K:
                if sums - A[starts] >= K:
                    while sums - A[starts] >= K and starts < ends:
                        sums -= A[starts]
                        starts += 1
                if maxs_len > ends - starts + 1:
                    maxs_len = ends - starts + 1

                if flag:
                    temp_sum = sums
                    temp_index = starts
                    while temp_index <= ends:# and temp_index < ends:
                        if temp_sum - A[temp_index] < K:
                            temp_sum -= A[temp_index]
                            temp_index += 1
                        else:
                            temp_index += 1
                            sums = temp_sum - A[temp_index]
                            starts = temp_index
                            temp_len = ends - temp_index + 1
                            if temp_len < maxs_len:
                                maxs_len = temp_len
                    flag = False
        if maxs_len == float("inf"):
            return -1
        return maxs_len

    def shortestSubarray(self, A, K: int) -> int:
        lens = len(A)
        if lens < 1:
            return -1
        last = float('inf')
        temp = A

        while len(temp) > 0:
            maxs_len = self.find(temp, K)
            if maxs_len != -1 and maxs_len < last:
                last = maxs_len
                print("maxs_len", maxs_len,  temp[0])
            temp = temp[1:]
        if last == float('inf'):
            return -1
        return last


if __name__ == "__main__":
    # data = [3, -1, -1, 3, -1, 3] #, -1, 3, 3]
    # # # data = [4, 5, 6, 7, -1, 2, 4, 5, -4, 7]
    # data = [2, -1, 2]
    # # data = [-47, 45, 92, 86, 17, -22, 77, 62, -1, 42]
    # k = 3
    # # data = [-30, -20, -10, 10, -50]
    # # # data = [-1, 2, -2, 4, -41]
    # # k = 5
    # data = [-28, 81, -20, 28, -29]
    # k = 89

    data = [61124, 62666, 91493, 71005, -1173, 58581, 20728, 39449, -30616, 41540, -38084, 84188, -16114, -35287, 53676,
     -34250, 29843, 12526, -38621, 12053, -882, 32085, -1363, 50409, -1231, 71958, 59016, 39379, -67, 37142, 28768,
     -11321, 73994, 20256, 2682, -37904, -39337, 80602, 11891, 40215, 27051, 36118, 63643, 26640, -18769, 78984, 6348,
     28533, -34954, 64208, 61612, 57439, 33936, 75461, 20831, 76271, 32192, -26682, 83300, -23447, 70890, -29485,
     -12708, 87090, -14337, 12169, -39444, 81991, -1148, -5233, 38278, 55871, 99575, -27175, 42094, 73448, -2077, -8193,
     65900, 98551, 18908, 56633, -42108, 30259, 96512, 60486, 89621, 99761, -29951, 39715, 87792, -10753, 58221, 73002,
     22745, 92500, 23857, 85611, 124, 13506, -30288, -7159, -21010, -39236, -42943, 2090, 82107, 24305, 1951, 90388,
     24684, 51756, 29963, -10917, -39491, -35188, 6851, 69336, -39174, -14182, 18222, 64178, 87826, -14514, -21338,
     7067, 42281, -3425, -37444, 1907, 12473, -45134, 15614, 44486, -8298, 2321, 89233, 81812, 1758, 58556, -35022,
     61007, 85162, 77893, -15426, 21029, -46258, -48340, -49700, 79088, 25880, 97246, -2936, -44991, -35680, -11505,
     -29669, 81139, -34657, 87623, -15236, 88611, -19385, 39155, 70997, 96655, 48467, 47390, 60075, -47133, 44762,
     32430, -4718, 6053, -30990, -40110, -29370, 24546, -21275, 32958, 92501, 98064, 80842, 52859, 56590, 52104, -25457,
     -18092, -24006, -19847, -4155, -1702, 85143, 44382, 73696, -29966, 52448, 73866, 48766, 94130, 29076, 760, -17998,
     16800, 19942, -14501, 59475, -32030, -31926, 52441, -594, -7080, -8818, 97895, 16346, 63758, 78512, 82609, -6232,
     88898, 90967, -31586, -40670, -7325, 95437, 30849, -38718, -6127, 24474, 82691, 90318, 42289, -13027, 31421, 29964,
     52516, 21077, 91860, 95219, 72602, 55984, 41712, 21285, -17161, 74805, 22722, 55983, 59627, 12876, 23368, 1721,
     95598, 76686, 5291, 94161, -30621, 63176, -28593, 57355, -20039, -11181, -35627, 78483, -22439, 31102, 23013,
     -48758, -21952, -35079, 9740, 50143, 95773, 13527, 13539, 95755, 72326, -34468, -11456, 46239, 94689, -13571,
     37013, 2914, 28454, 69452, 80632, -37797, 27930, 44020, 50118, -31348, -22076, -27748, 43333, -38315, 28465,
     -21872, 23867, -1731, -12258, 53083, -7694, -629, 56464, 28298, 28725, 44685, 31511, 99781, 46731, -30614, 73076,
     -14899, -24241, -17243, -2681, 26186, -34975, 63007, 77363, 125, 40714, 21773, 98047, 76206, 51191, 39405, 66801,
     50348, -14457, -1498, 47278, 51804, 69687, 4977, 64506, -23453, 32445, 46777, -31501, -22228, 72234, -44300,
     -14702, -31065, -3652, 21872, 85977, 94477, 61448, -2453, 84659, 50367, -6078, 17483, 39334, 65191, -11746, -39682,
     -18721, 82425, 13141, 21793, -14861, 65523, -20072, 78083, 7277, 38068, -26001, -48519, 35429, 56852, 96616, 40398,
     -2289, -46774, -6953, 39671, 90366, 38335, 46897, -7333, -9682, -4392, -37244, 90812, 71314, -46610, 52702, 47350,
     19056, 60589, -713, 46067, 40108, -34839, 36914, 28356, 40821, 33742, 69953, -25387, -20626, 88355, 88749, 84380,
     -31963, 23168, 43127, -45747, 61844, -13855, -35778, 50093, 3326, 61193, 31300, 11194, -45520, -28747, 78295,
     -34831, 77030, 69114, -3754, -12890, -45204, 74658, 26199, -44978, 27516, -23143, -38912, -18024, 84930, 42927,
     -33590, -15397, 59698, -28264, 75076, -28537, 51270, 77503, 98160, 53739, -22001, 61667, -33551, -16322, 41261,
     22591, 55573, -2052, 91647, 21120, -49400, 39719, -36007, 60346, 66963, -11298, 98554, 27858, 76068, 79398, 66924,
     18473, 77687, -3930, 52320, -22580, -19849, 18209, 23780, -15824, 46216, 96134, 68080, -3022, 86783, 7106, 56581,
     85301, 82245, -33373, 60243, -10176, 56717, 36000, 96988, 92545, 30951, 3207, 48757, -38564, -32669, 33658, 16306,
     56918, -16195, -26547, 12522, 36320, 48820, 79202, 84738, -22033, -15433, 71905, 13726, 38887, 11171, -1894, 12233,
     67863, -24103, -43820, 3852, -5488, 69444, -39296, 17049, 41840, 69968, 85563, -36314, -1292, -9861, 17925, 24271,
     75502, 57034, 89418, 55904, 1899, 82291, 46132, -38101, -31050, 86536, 71274, 83563, -34286, 19047, 29372, 83757,
     14025, -17637, 49769, 72495, -30828, 90019, -37148, -29615, 16479, 62700, 70983, 59817, 58812, 34989, 88512, 86325,
     44191, 50046, 67869, -11137, 2885, 30673, 56359, 86353, 2420, 67774, -8315, 40604, 40176, 44214, 62233, -38305,
     -26380, 54435, -35630, 1349, -1522, 2108, -2654, -18056, 57232, -13108, 22861, 85593, -40501, 91180, 79490, 14878,
     41218, 61800, 78683, -18, 17576, 16900, 36737, 48863, -43191, -44402, -7640, 445, -15295, 48877, 65357, 80973,
     -45553, -20313, 48716, 61496, 70049, 47304, -11341, 40708, 42275, -48097, 78428, -36364, 39964, 63927, -25429,
     49473, 35545, -40316, 81218, -1054, 45708, -33358, 2422, 39073, 72072, 68093, -44425, -46842, 66315, 73061, 89718,
     -43478, 72426, 42812, 81603, 6407, -15755, -43199, 71246, 85036, -46650, -8532, 50728, 22080, -17802, -27059,
     -14583, 1374, -39638, 59833, 80636, 69146, 6614, -38592, 26766, 52508, -13277, 43166, 24388, 63634, 13646, 49645,
     13920, 32676, 84479, 69850, 12140, 75678, 51157, 94457, -1845, 40690, 41069, 74990, 88236, 97600, -38256, -41893,
     1976, -22122, 12908, 89146, -4653, 10879, -36066, -13076, -13883, -29822, 93161, 21822, 76765, -33518, 95256,
     92204, 27973, 99523, -30522, 5936, 74643, 44033, 68532, 51942, 85261, 25173, -17116, -47754, 3637, 23343, -36144,
     14033, 52537, 51224, -48166, 83103, -43211, 92079, 85895, -20101, 53410, 48609, 40274, 8903, 72920, -33837, 50243,
     90536, -2339, 64790, -44271, 67027, 22832, 11494, 75835, -49405, 33023, 94347, 70345, 18294, 85239, 78385, 38712,
     62109, 55247, -19983, 72523, 3229, 58636, 88558, 19033, 14786, 18428, 76302, 32631, 58462, 90808, 13904, 66165,
     22037, -17175, 4629, -16213, 38004, 49494, 71612, 19408, 41559, 67479, -30863, 51727, 20451, -38212, 81230, 14715,
     -2982, -739, 25910, -26479, 44489, 28173, 28432, 5633, 47353, 48429, -19615, -21083, -18441, 31001, -45556, 37248,
     -11187, 53464, -16976, 65937, -33650, 85071, 66198, 54311, 84187, -4945, -34266, 73718, -41882, -41725, 16181,
     -46063, 28153, 67009, 28312, 71164, 55890, 76385, 19416, -15796, 97818, -5537, -48815, -45611, 82908, 53221, 96824,
     60713, -33220, 25879, 67539, -36614, -29659, 36777, -3750, 66957, -5266, 25155, 35275, -30553, 35900, 24738,
     -24496, -24131, -12643, 17051, 65288, 35545, 16309, 91993, 75059, -49849, 34149, 42891, 42716, 41257, 45407, 7346,
     -6458, 65478, 43570, 15116, -49037, -21010, 56346, 2632, -388, -13109, 26741, 19997, 50239, 28917, -21036, -21131,
     -46667, -19102, 71277, 27937, -15208, 79550, -47340, 19282, -16914, 72059, -21286, 68221, 25875, -36494, -17947,
     75581, 23681, 76145, 27240, 83968, 86442, 81110, 86771, -27816, 82844, 30806, 56698, 25119, 34935, -9173, -19351,
     80038, 90098, -38710, 83441, -29465, -15401, 21112, 81250, 29743, -49799, 15265, 43043, 29489, -39758, 87710,
     -47539, -23499, 76663, 52069, 50201, 20858, 93460, 33273, -48381, 88010, 99828, 52494, 28964, 2460, -8402, 91956,
     80400, 92109, -20757, 72140, 54186, 64339, 29064, -31573, 56578, -23307, 80471, 25553, 14884, 16539, -6168, 52738,
     62386, 78576, 53968, 71968, 87917, -23647, 27308, 8966, 59304, -33144, -40647, -1905, 76492, 723, 2185, -15480,
     42839, 29325, 91440, 57885, -45019, 20578, -37963, 8524, 99725, 31004, 94011, -15693, 26920, -46080, 38084, 65575,
     34298, 65117, 23567, -27817, -24530, 85999, 98405, 8050, 11231, 50171, 39828]
    k = 3307758

    print(sum(data), "dfdsf")
    my = Solutionss()
    print("result ", my.shortestSubarray(data, k))

    #print("result ", my.find(data[3:], k))
    #print("result ", my.find(data, k))


import sys

dicts = set(['A', 'S', 'W','D'])



strs = "A37;S1;S72;S41;W21;W32;A45;A98;" \
       "D97;D69;W57;W11;S41;S0;S24;S83;A75;" \
       "W77;S32;D18;A24;D20;A65;D95;S18;W56;" \
       "A84;W30;S3;S50;D64;S84;D82;A86;A36;" \
       "S85;S94;W64;W62;A12;W12;S84;W29;A52;" \
       "A73;W55;W71;D43;D76;D49;W19;S56;W63;" \
       "W56;A68;D68;D40;A48;W5;A12;S84;A2;S44;" \
       "A93;D51;D64;S4;W32;W27;W15;W70;A47;S77;" \
       "S88;A25;D51;D8;A34;A71;A5;D83;S36;S72;" \
       "A34;D46;S29;S5;W57;W16;S42;A23;A30;D43;" \
       "S0;W62;A34;D60;D31;W89;W91;S87;A15;S15;" \
       "S18;W83;S82;W87;W73;D42;A92;D48;A65;D36;" \
       "A11;W50;W38;W2;A0;D65;W29;D56;S64;D31;W8;" \
       "A56;A45;A56;W54;A97;D97;A90;S72;A95;A89;S78;" \
       "A35;A31;W68;W42;A73;S73;A24;S28;D69;W53;S54;" \
       "D80;D27;W24;S86;A17;A36;A41;A1;D19;S53;S96;A31;" \
       "A52;A63;A18;S54;A35;A82;W95;D8;W48;S75;W11;S9;" \
       "W60;D68;A92;A96;W32;S30;D26;W61;S0;D10;S89;W31;D4;W37;S49;D79;S56;A87;S61;A61;D96;W86;S81;D50;S91;A68;A82;A36;A16;S6;W25;D76;D94;A20;A37;D91;S58;A54;S77;S27;A35;S6;A88;A14;S72;D12;A95;W93;W1;A73;A55;A13;S55;W43;W6;D37;W19;W79;W56;S26;A36;W85;A6;W94;A54;A12;S0;A13;D18;W14;A52;W44;D83;W17;W73;A72;D56;A63;S14;A64;A84;S54;D67;A92;D46;A51;D99;W42;W2;"


def f(strs):
    a = [0, 0]
    strs = strs.strip().split(";")
    for line in strs:
        if len(line) < 2:
            continue
        char = line[0]
        if char in dicts:
            index = int(line[1:])
            if char == 'A':
                a[0] -= index
            elif char == 'D':
                a[0] += index
            elif char == 'S':
                a[1] -= index
            elif char == 'W':
                a[1] += index
            else:
                continue
    return a


a = f(strs)
print(a)

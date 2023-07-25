import sys
import numpy as np


np.set_printoptions(threshold=sys.maxsize)

a = np.asarray([[[[-1532.6981201172, -1767.2946777344, -1704.7355957031,
           -1501.4184570312, -1157.3433837891, -1141.7036132812,
           -1000.9456787109,  -813.2683715820,  -954.0263671875,
            -531.7523803711,  -390.9944152832,  -218.9568634033,
             -93.8386535645,   -15.6397762299,   -78.1988830566,
            -203.3170928955,  -359.7148437500,  -375.3546142578,
            -172.0375366211,  -140.7579803467,  -156.3977661133,
            -359.7148437500,  -390.9944152832,  -328.4353027344,
            -390.9944152832,  -484.8330688477,  -609.9512939453,
            -719.4296875000,  -797.6286010742,  -828.9081420898,
            -954.0263671875, -1032.2252197266, -1063.5047607422,
           -1157.3433837891, -1329.3809814453, -1767.2946777344,
           -1751.6549072266, -1219.9025878906, -1157.3433837891,
           -1157.3433837891, -1063.5047607422,  -813.2683715820,
            -516.1126098633,  -406.6341857910,  -140.7579803467,
             -46.9193267822,     0.0000000000,   -93.8386535645,
            -281.5159606934,  -265.8761901855,  -140.7579803467,
            -156.3977661133,  -297.1557617188,  -125.1182098389,
            -453.5534973145,  -422.2739562988,  -390.9944152832,
            -390.9944152832,  -469.1932983398,  -594.3115234375,
            -703.7899169922]],

         [[ -641.2308349609,  -641.2308349609,  -594.3115234375,
            -359.7148437500,   -78.1988830566,   -62.5591049194,
             218.9568634033,   422.2739562988,   500.4728393555,
             578.6716918945,   500.4728393555,   563.0319213867,
             641.2308349609,   578.6716918945,   578.6716918945,
             672.5103759766,   891.4672241211,   954.0263671875,
             891.4672241211,  1032.2252197266,  1094.7843017578,
             938.3865966797,   703.7899169922,   265.8761901855,
              78.1988830566,   109.4784317017,   125.1182098389,
             140.7579803467,    78.1988830566,    31.2795524597,
             -78.1988830566,  -172.0375366211,  -359.7148437500,
            -500.4728393555,  -656.8706054688,  -797.6286010742,
            -656.8706054688,  -218.9568634033,   -15.6397762299,
              31.2795524597,   297.1557617188,   453.5534973145,
             516.1126098633,   531.7523803711,   547.3921508789,
             594.3115234375,   656.8706054688,   656.8706054688,
             828.9081420898,  1016.5854492188,   922.7468261719,
             907.1069946289,  1079.1445312500,  1047.8649902344,
             875.8274536133,   750.7092285156,   500.4728393555,
              78.1988830566,    46.9193267822,    31.2795524597,
              15.6397762299]],

         [[  297.1557617188,   312.7955322266,   218.9568634033,
             390.9944152832,   516.1126098633,   375.3546142578,
             312.7955322266,   406.6341857910,   406.6341857910,
             265.8761901855,   203.3170928955,   109.4784317017,
            -156.3977661133,  -297.1557617188,  -172.0375366211,
              62.5591049194,   203.3170928955,    62.5591049194,
            -140.7579803467,  -203.3170928955,   -46.9193267822,
             187.6773071289,   281.5159606934,    93.8386535645,
              93.8386535645,   281.5159606934,   406.6341857910,
             359.7148437500,   312.7955322266,   344.0750732422,
             359.7148437500,   375.3546142578,   281.5159606934,
             281.5159606934,   297.1557617188,   359.7148437500,
             328.4353027344,   437.9137268066,   594.3115234375,
             563.0319213867,   547.3921508789,   375.3546142578,
             265.8761901855,    93.8386535645,     0.0000000000,
            -140.7579803467,  -172.0375366211,  -109.4784317017,
             203.3170928955,   -31.2795524597,  -281.5159606934,
            -250.2364196777,  -140.7579803467,   109.4784317017,
             156.3977661133,   218.9568634033,   203.3170928955,
             156.3977661133,   140.7579803467,   156.3977661133,
             344.0750732422]]]])

scale = 15.639776229858398

type = 'INPUT'


if type == 'NORMAL':
  for item in a.flatten():
    if scale == 1:
      print(item, end = ', ')
    else:
      print(round(item/scale), end = ', ')



if type == 'INPUT':
  for item in a.flatten('F'):
    if scale == 1:
      print(item, end = ', ')
    else:
      print(round(item/scale), end = ', ')



if type == 'CONV1':
  for item in a.flatten('F'):
    if scale == 1:
      print(item, end = ', ')
    else:
      print(round(item/scale), end = ', ')



if type == 'FC1':
  a = a.reshape(100,320)
  
  for i in range(len(a)):
    a[i] = a[i].reshape(20,16).flatten('F')
  for item in a.flatten():
    if scale == 1:
      print(item, end = ', ')
    else:
      print(round(item/scale), end = ', ')
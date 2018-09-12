

from tool import config, util, myfile
from tool.unit import Unit

unit = Unit()

unit.initialize(
            config.len_unit,
            config.len_w,
            config.len_layer,
            config.len_m_unit,
            config.len_m_w
        )

for count in range(config.max):
    
    e = 0

    for in_row in range(len(config.input_data)):

        unit.process_output(config.input_data, in_row)

        e += util.diff(config.correct[in_row], unit.out)

        unit.process_update_weight(config.rate, config.correct, config.input_data, in_row)

    if count % 1000 == 0:
        print (e)


print ('Machine Learning is done')

tmp = myfile.read('data_check.csv')

for in_row in range(len(tmp)):
    unit.process_output(tmp, in_row)
    print (unit.out)

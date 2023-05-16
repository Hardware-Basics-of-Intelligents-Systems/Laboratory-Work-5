from form_generators import make_fdnf, make_fcnf, make_dednf_qmc, make_decnf_qmc
from main import print_truth_table


def print_info(title, tt, variables):
    print(title)
    print("-" * 100)
    print_truth_table(tt, variables)
    print("FDNF: ", make_fdnf(tt, variables))
    print("FCNF: ", make_fcnf(tt, variables))
    dednf = make_dednf_qmc(tt, variables)
    print("Dead-end DNF: ", dednf)
    print("Dead-end CNF: ", make_decnf_qmc(tt, variables))


def ods3_pdnf():
    res_tt = [
        ((False, False, False), False,),
        ((False, False, True), True,),
        ((False, True, False), True,),
        ((False, True, True), False,),
        ((True, False, False), True,),
        ((True, False, True), False,),
        ((True, True, False), False,),
        ((True, True, True), True,)
    ]

    tran_tt = [
        ((False, False, False), False,),
        ((False, False, True), False,),
        ((False, True, False), False,),
        ((False, True, True), True,),
        ((True, False, False), False,),
        ((True, False, True), True,),
        ((True, True, False), True,),
        ((True, True, True), True,)
    ]

    variables = ["A", "B", "P"]

    print_info("ОДС-3 - Результат", res_tt, variables)
    print_info("ОДС-3 - Перенос", tran_tt, variables)


def counter():
    y1 = [
        ((True, True, True, True), False),
        ((True, True, False, True), False),
        ((True, False, True, True), False),
        ((True, False, False, True), True),
        ((False, True, True, True), False),
        ((False, True, False, True), False),
        ((False, False, True, True), False),
        ((False, False, False, True), True),

        ((True, True, True, True), False),
        ((True, True, False, False), False),
        ((True, False, True, False), False),
        ((True, False, False, False), False),
        ((False, True, True, False), False),
        ((False, True, False, False), False),
        ((False, False, True, False), False),
        ((False, False, False, False), False),
    ]

    y2 = [
        ((True, True, True, True), False),
        ((True, True, False, True), True),
        ((True, False, True, True), False),
        ((True, False, False, True), True),
        ((False, True, True, True), False),
        ((False, True, False, True), True),
        ((False, False, True, True), False),
        ((False, False, False, True), True),
        ((True, True, True, True), False),
        ((True, True, False, False), False),
        ((True, False, True, False), False),
        ((True, False, False, False), False),
        ((False, True, True, False), False),
        ((False, True, False, False), False),
        ((False, False, True, False), False),
        ((False, False, False, False), False),
    ]

    y3 = [
        ((True, True, True, True), True),
        ((True, True, False, True), True),
        ((True, False, True, True), True),
        ((True, False, False, True), True),
        ((False, True, True, True), True),
        ((False, True, False, True), True),
        ((False, False, True, True), True),
        ((False, False, False, True), True),
        ((True, True, True, True), False),
        ((True, True, False, False), False),
        ((True, False, True, False), False),
        ((True, False, False, False), False),
        ((False, True, True, False), False),
        ((False, True, False, False), False),
        ((False, False, True, False), False),
        ((False, False, False, False), False),
    ]

    vars = ["x1", "x2", "x3", "V"]
    y1 = make_dednf_qmc(y1, vars)
    y2 = make_dednf_qmc(y2, vars)
    y3 = make_dednf_qmc(y3, vars)

    print(y1)
    print(y2)
    print(y3)


def pt8421(bias):
    def to_bool(s: str):
        return s == "1"

    inputs = []
    outputs = []

    for i in range(0, 10):
        inp = "{0:04b}".format(i)
        inp_vect = (inp[0] == "1", inp[1] == "1", inp[2] == "1", inp[3] == "1")
        inputs.append(inp_vect)
        out = "{0:04b}".format(i + bias)
        out_vect = (out[0] == "1", out[1] == "1", out[2] == "1", out[3] == "1")
        outputs.append(out_vect)
        print(inp, out)

    for i in range(10, 16):
        inp = "{0:04b}".format(i)
        inp_vect = (inp[0] == "1", inp[1] == "1", inp[2] == "1", inp[3] == "1")
        inputs.append(inp_vect)
        out_vect = (False, False, False, False)
        outputs.append(out_vect)

    for i in range(0, 4):
        table = []
        for j, values in enumerate(inputs):
            table.append((values, outputs[j][i]))
        print(make_dednf_qmc(table, ["X1", "X2", "X3", "X4"]))


if __name__ == '__main__':
    # ods3_pdnf()
    # pt8421(1)
    counter()

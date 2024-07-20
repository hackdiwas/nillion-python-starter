from nada_dsl import *

def nada_main():

    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Inputs from each party
    int1 = SecretInteger(Input(name="int1", party=party1))
    int2 = SecretInteger(Input(name="int2", party=party2))
    int3 = SecretInteger(Input(name="int3", party=party3))

    # Perform some operations
    sum_int = int1 + int2 + int3
    product_int = int1 * int2 * int3
    comparison = (int1 > int2) & (int2 > int3)

    # Outputs to parties
    output1 = Output(sum_int, "sum_output", party1)
    output2 = Output(product_int, "product_output", party2)
    output3 = Output(comparison, "comparison_output", party3)

    return [output1, output2, output3]
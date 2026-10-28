def to_twos_complement_8bit(val):
    if not (-128 <= val <= 127):
        raise ValueError(f"Value {val} out of 8-bit signed range (-128 to 127)")
    return f"{val & 0xFF:08b}"

def from_twos_complement_8bit(binary_str):
    val = int(binary_str, 2)
    if val & 0x80:
        val -= 256
    return val

def check_overflow(op1, op2, result, operation='+'):
    if operation == '+':
        if (op1 >= 0 and op2 >= 0 and result < 0) or (op1 < 0 and op2 < 0 and result >= 0):
            return True
    elif operation == '-':
        if (op1 >= 0 and op2 < 0 and result < 0) or (op1 < 0 and op2 >= 0 and result >= 0):
            return True
    return False

def run_arithmetic_demo(op1, op2, operation):
    print(f"--- Expression: ({op1}) {operation} ({op2}) ---")
    
    bin1 = to_twos_complement_8bit(op1)
    bin2 = to_twos_complement_8bit(op2)
    print(f"Operand 1 ({op1:4d}): {bin1}")
    print(f"Operand 2 ({op2:4d}): {bin2}")
    
    if operation == '+':
        actual_res_dec = op1 + op2
        bin_sum = (int(bin1, 2) + int(bin2, 2)) & 0xFF
        result_bin = f"{bin_sum:08b}"
    elif operation == '-':
        actual_res_dec = op1 - op2
        neg_op2_bin = to_twos_complement_8bit(-op2)
        bin_sum = (int(bin1, 2) + int(neg_op2_bin, 2)) & 0xFF
        result_bin = f"{bin_sum:08b}"
        print(f"2's Comp of Op2: {neg_op2_bin} (used for addition)")

    interpreted_dec = from_twos_complement_8bit(result_bin)
    
    print(f"Binary Result  : {result_bin}")
    print(f"Decimal Result : {interpreted_dec}")
    
    overflow = check_overflow(op1, op2, interpreted_dec, operation)
    print(f"Arithmetic Overflow Detected: {overflow}")
    print()

run_arithmetic_demo(34, 27, '+')
run_arithmetic_demo(-34, -27, '-')
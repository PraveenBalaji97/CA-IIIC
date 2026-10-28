def rotate_left_without_carry(bin_str, positions):
    val = int(bin_str, 2)
    val = val & 0xFF
    steps = []
    
    current_val = val
    for i in range(1, positions + 1):
        msb = (current_val & 0x80) >> 7
        current_val = ((current_val << 1) & 0xFF) | msb
        steps.append(f"Step {i}: {current_val:08b}")
        
    return f"{current_val:08b}", steps

def rotate_left_with_carry(bin_str, positions, initial_carry=0):
    val = int(bin_str, 2) & 0xFF
    carry = initial_carry
    steps = []
    
    current_val = val
    current_carry = carry
    
    for i in range(1, positions + 1):
        new_carry = (current_val & 0x80) >> 7
        current_val = ((current_val << 1) & 0xFF) | current_carry
        current_carry = new_carry
        steps.append(f"Step {i}: Binary = {current_val:08b}, Carry = {current_carry}")
        
    return f"{current_val:08b}", current_carry, steps

orig_bin = "10110110"
print(f"Original 8-bit Number: {orig_bin}\n")

result_a, steps_a = rotate_left_without_carry(orig_bin, 2)
print("--- a) Rotate Left Without Carry (ROL) by 2 positions ---")
for step in steps_a:
    print(step)
print(f"Final Result: {result_a}\n")

init_c = 0
result_b, final_c, steps_b = rotate_left_with_carry(orig_bin, 2, initial_carry=init_c)
print(f"--- b) Rotate Left With Carry (RCL) by 2 positions (Initial Carry = {init_c}) ---")
for step in steps_b:
    print(step)
print(f"Final Binary: {result_b} | Final Carry: {final_c}")
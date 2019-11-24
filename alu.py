def get_inverse(val):
	return 0 if val == 1 else 1

def multiplexer(input_one, input_two, selector):
	return input_one if selector == 0 else input_two

def logic_one(a, b, a_invert, b_invert):
	a_inverse = get_inverse(a)
	b_inverse = get_inverse(b)
	a_output  = multiplexer(a, a_inverse, a_invert)
	b_output  = multiplexer(b, b_inverse, b_invert)
	return a_output, b_output

def and_op(a, b):
	return 1 if a ==  b else 0

def or_op(a, b):
	return 1 if a or b else 0

def carry_op(a, b, cin):
	if cin == 1:
		if a == 1 and b == 1:
			return 1, 1
		if (a == 0 and b == 1) or (a == 1 and b == 0):
				return 0, 1
		return cin, 0

	if (a == 0) and (b == 0) :
		return 0, 0
	if (a == 1) and (b == 1):
		return 0, 1
	if ((a==0) and (b==1)) or ( (a==1) and (b==0)):
		return 1, 0
	return "wtf?"
	
def final_logic(input_a, input_b, input_carry, op):
	return input_carry
	if op == "sub":
		return input_b
	if op == "add":
		return input_a
	
def one_bit_alu(a, b, a_invert, b_invert, cin):
	a_output, b_output = logic_one(a, b, a_invert, b_invert)
	and_output = and_op(a_output, b_output)
	or_output  = or_op(a_output, b_output)
	cin_output, cin_carry = carry_op(a_output, b_output, cin)
	res = final_logic(and_output, or_output, cin_output, "sub")
	print("Cin is: ", cin_output, " Res is: ", res)
	return cin_carry, res

bits_one = [1, 1, 0, 0, 0, 0, 0, 0]
bits_two = [1, 0, 1, 0, 0, 0, 0, 0]
for i in range(55):
	bits_one.append(0)
	bits_two.append(0)

carry_output = 1
for bit_one, bit_two in zip(bits_one, bits_two):
	carry_output, res = one_bit_alu(bit_one, bit_two, 0, 1, carry_output)

#carry_output, res = one_bit_alu(1, 1, 1, 0, 0)

#print(one_bit_alu(1,1,1,0,0))



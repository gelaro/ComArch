	lw	0	1	x	#load x
	lw	0	4	fibA	#load fibo addr
	lw	0	2	one	#temp1=1
	jalr	4	7	#call fibo
end	halt
fibo	lw	0	6	neg	#temp2=-1	
	beq	0	1	retX	#if x=0 return x
	beq	2	1	retX	#if x=1	return x
	add	1	6	1	#x - 1
	sw	5	7	stack	#save return addr
	add	5	2	5	#sp + 1
	sw	5	1	stack	#save x-1
	add	5	2	5	#sp + 1
	jalr	4	7	#call fib x-1
	lw	0	6	neg	#temp2=-1
	add	5	6	5	#sp - 1
	lw	5	1	stack	#load x-1
	add	5	6	5	#sp - 1
	lw	5	7	stack	#load old return addr
	add	1	6	1	# (x-1)-1 = x-2
	sw	5	3	stack	#save first return
	add	5	2	5	#sp + 1
	sw	5	7	stack	#save return addr
	add	5	2	5	#sp + 1
	jalr	4	7	#call fib x-2
	lw	0	6	neg	#temp2=-1
	add	5	6	5	#sp - 1
	lw	5	7	stack	#load return addr
	add	5	6	5	#sp - 1
	lw	5	6	stack	#load first return to 6
	add	3	6	3	#add first return and second return
	jalr	7	6	#return
retX	add	0	1	3	#mov x from r1 to r3
	jalr	7	6	return
one	.fill	1
neg	.fill	-1
x	.fill	6
fibA	.fill	fibo
stack	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
	.fill	0
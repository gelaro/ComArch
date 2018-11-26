		lw		0	1	input
		lw      0   6   pos1
		lw      0   4	fib
		jalr	4	7
		halt

fib		beq		1	0	re0
		beq		1	6	re1
		lw		0	2	neg1
		add		1	2	1

		lw		0	4	pos1
		add		3	4	0
		add		1	1	2
		beq		1	0	return
		sw		5	4	0
		add		5	4	5
		sw		5	3	0

for		lw		0	6	neg1
		add		1	6	1
		lw		0	4	5
		add		5	6	5
		lw		0	2	5
		add		3	2	4
		sw		5	4	0
		lw		0	6	pos1
		add		5	6	5
		sw		5	3	5
		
		beq		1	0	return
		beq		0	0	for

re0		add		3	0	0
		beq		0	0	return
re1		lw		0	3	pos1
return	jalr	7	4	
input	.fill	5
pos1	.fill	1
neg1	.fill	-1

	lw	0	2	mplier	#op2
	lw	0	3	mcand	#b=op1
	lw	0	4	one	#x=1,a=0in7
loop	nand	4	2	5	#!(x&op2)
	nand	5	5	5	#^x&op2
	beq	0	5	do
	add	1	3	1	#a+=b
do	add	3	3	3	#b<<=1
	add	4	4	4	#x<<=1
	beq	0	4	done
	beq	0	0	loop
	noop
done	halt
mcand	.fill	32766
mplier	.fill	10383
one	.fill	1
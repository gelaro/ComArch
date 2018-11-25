	lw	0	7	neg
	lw	0	6	tr
	lw	0	1	tr
	lw	0	2	tw
	nand	1	2	3
	sw	0	3	regmem
	add	1	7	1
	beq	0	1	2
	jalr	6	5
	noop
done	halt
tr	.fill	3
tw	.fill	12
neg	.fill	-1
regmem	.fill	0
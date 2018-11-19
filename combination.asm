	lw	0	1	n
	lw	0	2	r
	lw	0	5	sp
	lw	0	4	combiA
	jalr	4	7
	halt
combi	beq	2	0	ret1	if r == 0 return 1
	beq	1	2	ret1	if n == r return 1
	lw	0	6	neg1	,,
	add	1	6	1	n = n - 1
savest	lw	0	6	four	,,
	add	5	6	5	sp = sp + 4
	sw	5	1	0	save n-1
	sw	5	2	-1	save r
	sw	5	7	-2	save ret address
calc	lw	0	4	combiA
	jalr	4	7		call combi(n-1, r)
	sw	5	3	-3	save v
	lw	5	2	-1	load r
	lw	0	4	neg1
	add	2	4	2	r = r - 1
	lw	5	1	0	load n-1
	lw	0	4	combiA
	jalr	4	7		call combi(n-1, r-1)
	lw	5	4	-3
	add	3	4	3	ret = combi(n-1, r) + combi(n-1, r-1)
resst	lw	5	7	-2	load ret address
	lw	0	6	nfour	,,
	add	5	6	5	sp = sp - 4
	jalr	7	6		return ret
ret1	lw	0	3	one
	jalr	7	4		return 1
n	.fill	5
r	.fill	2	
one	.fill	1
neg1	.fill	-1
nfour	.fill	-4
four	.fill	4
combiA	.fill	combi
sp	.fill	sp
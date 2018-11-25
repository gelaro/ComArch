	lw	0	1	n	#load n
	lw	0	2	r	#load r
	lw	0	4	comAdr	#load addr combi
	jalr	4	7	#call combination n=3 r=2
end	halt
combi	beq	0	2	ret1
	beq	1	2	ret1	#if r=0 or r=n return 1
	lw	0	6	one	#temp=1
	sw	5	7	stack	#save return addr
	add	5	6	5	#sp + 1
	sw	5	1	stack	#save n
	add	5	6	5	#sp + 1
	sw	5	2	stack	#save r
	add	5	6	5	#sp + 1
	lw	0	6	neg	#temp=-1
	add	1	6	1	#n-1
	jalr	4	7	#call combination n=n-1 r=r
	lw	0	6	neg	#temp=-1
	add	5	6	5	#sp-1
	lw	5	2	stack	#load old r
	add	5	6	5	#sp-1
	lw	5	1	stack	#load old n
	add	5	6	5	#sp-1
	lw	5	7	stack	#load old return addr
	add	1	6	1	#n-1
	add	2	6	2	#r-1
	lw	0	6	one	#temp=1
	sw	5	3	stack	#save first return
	add	5	6	5	#sp + 1
	sw	5	7	stack	#save return addr
	add	5	6	5	#sp + 1
	jalr	4	7	#call combination n-1,r-1
	lw	0	6	neg	#temp=-1
	add	5	6	5	#sp-1
	lw	5	7	stack	#load return addr
	add	5	6	5	#sp-1
	lw	5	6	stack	#load first return to 6
	add	3	6	3	#add first return(at 6) and second return(at 3)
	jalr	7	6	#return
ret1	lw	0	3	one	#return value =1
	jalr	7	6	#return
one	.fill	1
neg	.fill	-1
n	.fill	5
r	.fill	2
comAdr	.fill	combi
st	.fill	stack
e	.fill	end
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
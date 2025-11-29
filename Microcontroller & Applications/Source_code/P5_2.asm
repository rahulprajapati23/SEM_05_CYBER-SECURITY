# ORG 1020H
# DB F5H,E4H, D1H, C6H, B8H
# ORG 0000H
	   MVI C,05
	   LXI H,1020
	   LXI D,1025

COPY:	   MOV A,M
	   STAX D
	   INX H
	   INX D
	   DCR C
	   JNZ COPY
	   MVI B,04

LOOP:	   LXI H,1025
	   MOV C,B

AGAIN:	   MOV A,M
	   INX H
	   CMP M
	   JC NO_SWAP
	   MOV D,M
	   MOV M,A
	   DCX H
	   MOV M,D
	   INX H

NO_SWAP:	   DCR C
	   JNZ AGAIN
	   DCR B
	   JNZ LOOP

HOLD:	   HLT

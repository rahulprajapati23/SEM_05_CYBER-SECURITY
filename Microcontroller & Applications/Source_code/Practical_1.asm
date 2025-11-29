	   MVI A,F2H
	   OUT 15H
	   MVI A,03H
	   OUT 16H

	   IN 16H
	   MOV C,A	// COUNTER
	   IN 15H
	   MVI D,00H
	   
AGAIN:	   ADD D
	   MOV D,A
	   DCR C
	   MOV A,C
	   CPI 00H
	   IN 15H
	   JNZ AGAIN

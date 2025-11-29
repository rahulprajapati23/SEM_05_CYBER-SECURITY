#include <reg51.h>

void delay(){
	int i;
	int j;
	for (i=0;i<200;i++){
		for(j=0;j<100;j++){
		}
	}
}

void main(){
	while(1){
		P1 = 0x01;
		delay();
		P1 = 0x02;
		delay();																																   
		P1 = 0x04;
		delay();
		P1 = 0x08;
		delay();
		P1 = 0x10;
		delay();
		P1 = 0x20;
		delay();
		P1 = 0x40;
		delay();
		P1 = 0x80;
		delay();
		P1 = 0xFF;
		delay();
		
	}
}
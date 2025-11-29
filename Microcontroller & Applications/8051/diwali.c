#include <reg51.h>

void delay(){
	int i;
	int j;
	for (i=0;i<350;i++){
		for(j=0;j<150;j++){
		}
	}
}

void main(){
	while(1){
		P1 = 0x80;
		P0 = 0X01;
		delay();
		P1 = 0x40;
		P0 = 0X02;
		delay();																																   
		P1 = 0x20;
		P0 = 0x04;
		delay();
		P1 = 0x10;
		P0 = 0x08;
		delay();
		P1 = 0x08;
		P0 = 0x10;
		delay();
		P1 = 0x04;
		P0 = 0x20;
		delay();
		P1 = 0x02;
		P0 = 0x40;
		delay();
		P1 = 0x01;
		P0 = 0x80;
		delay();
		P1 = 0xFF;
		P0 =0xFF;
		delay();
		
	}
}
#include <reg51.h>

void delay(){
 	int i,j;
	for (i=0;i<380;i++){
		for (j=0;j<250;j++){
		}
	}
}

int select_dig(int led_no){
	int num[]={0xFE,0xFD,0xFB,0xF7,0xF0};
	return (num[led_no]);
}

int get_hex(int led_no){
	int num[]={0x3F,0x06,0x5B,0xCF,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
	return(num[led_no]);
}

int main(){
 	int led_no[]={1,0,2,0};
	while(1){
		int i;
		for(i=0;i<4;i++){
			P2=select_dig(i);
			P1=get_hex(led_no[i]);
			delay();
			
		}
	}
}
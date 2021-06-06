#include<stdio.h>
#include<conio.h>
#include"POSTFIX.TXT"
#include"PREFIX.TXT"
#include<string.h>
#include <dos.h>
//void side_line();
void project_name();
void main()
{


	int i;
	int ch;


	label:
	clrscr();
	project_name();
	side_line();



	clrscr();
	side_line();
	gotoxy(18,9);
	cprintf("\n-> Enter the type of Expression to be Evaluated:-");
	gotoxy(18,12);
	cprintf("1] Prefix Expression.");
	gotoxy(18,14);
	cprintf("2] Postfix Expression.");
	gotoxy(18,16);
	cprintf(" ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
		pre();
		break;

		case 2:
		postfix();
		break;

		default:
		gotoxy(18,15);
		cprintf(" ");
		cprintf("Invalid Input!!!");
	}
	getch();
 }/*
void side_line()
{
	int i,j;
	for(i=5;i<25;i++)
	{
	       gotoxy(5,i);
	       cprintf("Û");
	}
	gotoxy(3,22);
	cprintf("ÜÜÛÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ");
	gotoxy(3,23);
	cprintf("  Û");

	for(j=3;j<22;j++)
	{

		gotoxy(75,j);
		cprintf("Û");
	}
	gotoxy(29,3);
	cprintf("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÛÜÜÜ");
	gotoxy(75,2);
	cprintf("Û");
	delay(400);

}
*/
void project_name()
{
	highvideo();
	textcolor(15);
	gotoxy(29,11);
	cprintf("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ");
	gotoxy(29,12);
	cprintf("Ý");
	gotoxy(31,12);
	textcolor(14);
	cprintf("EXPRESSION EVALUATOR ");
	textcolor(15);
	gotoxy(52,12);
	cprintf("Þ");
	gotoxy(29,13);
	cprintf("ßßßßßßßßßßßßßßßßßßßßßßßß");


}
/*
void side_line()
{
	int i,j;
	for(i=5;i<24;i++)
	{
	       gotoxy(5,i);
	       cprintf("Û");
	}
	gotoxy(3,23);
	cprintf("ÜÜÛÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ");
	gotoxy(3,24);
	cprintf("  Û");

	for(j=3;j<22;j++)
	{

		gotoxy(75,j);
		cprintf("Û");
	}
	gotoxy(29,4);
	cprintf("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÛÜÜÜ");
	gotoxy(75,5);
	cprintf("Û");


}
*/
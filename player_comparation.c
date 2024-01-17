/*
1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
The system should also allow comparison between two players. Use the following player profiles:

Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
The program functions as follows: The coach accesses the system and encounters a menu with the following options:

Player Review: By entering the player's jersey number, they can access the player's characteristics.
Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
Identify the fastest player: Displays the player with the most points in speed.
Identify the top goal scorer: Displays the player with the most points in goals.
Identify the player with the most assists: Displays the player with the most points in assists.
Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
The system should also allow returning to the main menu.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Player "object" with all the characteristics
typedef struct player{
    char name[40];
    int goals;
    int speed;
    int assists;
    int passing_accuracy;
    int defensive_involvemnt;
    int jersey_number;
}player;

//Procedure to display the characteristic of a specific player
void display_player(int index, player * list){
    printf("\nThe player:%s\nGoals:%i\nSpeed:%i\nAssists:%i\nPassing accurecy:%i\nDefensive involvement:%i\n\n",list[index].name,list[index].goals,list[index].speed,list[index].assists,list[index].passing_accuracy,list[index].defensive_involvemnt);
}

int main(){
    player players[5];
    //First player
    strcpy(players[0].name , "Bruno Fernandez");
    players[0].goals = 5;
    players[0].speed = 6;
    players[0].assists = 9;
    players[0].passing_accuracy = 10;
    players[0].defensive_involvemnt = 3;
    players[0].jersey_number = 8;
    //Second player
    strcpy(players[1].name , "Rasmus Hojlund");
    players[1].goals = 12;
    players[1].speed = 8;
    players[1].assists = 2;
    players[1].passing_accuracy = 6;
    players[1].defensive_involvemnt = 2;
    players[1].jersey_number = 11;
    //Third player
    strcpy(players[2].name, "Harry Maguire");
    players[2].goals = 1;
    players[2].speed = 5;
    players[2].assists = 1;
    players[2].passing_accuracy = 7;
    players[2].defensive_involvemnt = 9;
    players[2].jersey_number = 5;
    //forth player
    strcpy(players[3].name,"Alejandro Garnacho" );
    players[3].goals = 8;
    players[3].speed = 7;
    players[3].assists = 8;
    players[3].passing_accuracy = 6;
    players[3].defensive_involvemnt = 0;
    players[3].jersey_number = 17;
    //fith player
    strcpy(players[4].name,"Mason Mount");
    players[4].goals = 5;
    players[4].speed = 6;
    players[4].assists = 4;
    players[4].passing_accuracy = 8;
    players[4].defensive_involvemnt = 1;
    players[4].jersey_number = 7;

    int menu = 1;
    int option;
    int jersey_option;
    int jersey_option2;
    int aux;
    int index1;
    int index2;
    int index_top;
    int error_flag;
    int exit_option;
    while(menu==1){
        //Display a player with his jersey number
        printf("MENU:\n1-Player review\n2-Compare two players\n3-Identify de fastest player\n4-Identify the top goal scorer\n");
        printf("5-Identify the player with most assists\n6-Identify the player with the highest passing accurency\n7-Display the player with the most defensive involment\n8-Exit\n\n");
        scanf("%i",&option);
        index_top=0;
        switch(option){
            case 1:
                error_flag = 0;
                printf("\nEnter the jersey number of the player(8,11,5,17,7):");            
                scanf("%i",&jersey_option);
                for(int i = 0; i < 5; i++){
                    if(players[i].jersey_number==jersey_option){
                        display_player(i,players);
                        error_flag = 1;
                        break;
                    }
                }
                if(error_flag == 0){
                    printf("Incorrect jersey number\n");
                }
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            //Display or "compare" two players with their jersey number
            case 2:
                aux = 0;
                printf("Please enter the jersey number of the first player:");
                scanf("%i",&jersey_option);
                printf("Now enter the jersey number of the second player:");
                scanf("%i",&jersey_option2);
                printf("First player:\n");
                for(int i = 0; i < 5;i++){
                    if(players[i].jersey_number==jersey_option){
                        index1 = i;
                        aux++;
                    }
                    if(players[i].jersey_number == jersey_option2){
                        index2 = i;
                        aux++;
                    }
                }
                if(aux == 2){
                    display_player(index1,players);
                    printf("\n");
                    display_player(index2,players);
                }else{
                    printf("Incorrect Jersey number, try again\n");
                }
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            //Show the fastest player
            case 3:
                for(int i = 1; i < 4; i++){
                    if(players[index_top].speed<players[i].speed){
                        index_top = i;
                    }
                }
                printf("The fastest is:\n");
                display_player(index_top,players);
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
                //Show the player with the most goals
            case 4:
                for(int i = 1; i < 4; i++){
                    if(players[index_top].goals<players[i].goals){
                        index_top = i;
                    }
                }
                printf("The player with the most amount of goals is:\n");
                display_player(index_top,players);
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            case 5:
            //Show the player with the most assists
                for(int i = 1; i < 4; i++){
                    if(players[index_top].assists<players[i].assists){
                        index_top = i;
                    }
                }
                printf("The player with the most assists is:\n");
                display_player(index_top,players);
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            //Show the player with the most acurrecy
            case 6:
                for(int i = 1; i < 4; i++){
                    if(players[index_top].passing_accuracy<players[i].passing_accuracy){
                        index_top = i;
                    }
                }
                printf("The player with the highest passing accurecy is:\n");
                display_player(index_top,players);
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            //Show the player withe the most defensive involvement
            case 7:
                for(int i = 1; i < 4; i++){
                    if(players[index_top].defensive_involvemnt<players[i].defensive_involvemnt){
                        index_top = i;
                    }
                }
                printf("The player with the most defensive involvement is:\n");
                display_player(index_top,players);
                printf("\nDo you want to exit?\n1-Exit\n2-Return to the Menu\n\n");
                scanf("%i",&exit_option);
                if(exit_option!=2){
                    menu = 0;
                }
                break;
            //Exit
            case 8:
                menu = 0;
                break;
            default:
                menu = 0;
                break;
        }
    }
    return 0;
}
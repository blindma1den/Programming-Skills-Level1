/*
A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
 Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

Clue: You could consider the user's budget
*/

#include <stdio.h>
#include <string.h>
//Each coutry

typedef struct country{
    char activities[30];
    char season[10];
    char country_name[15];
    int cost;
}country;


int main(){
   country countries[8];
    //First season (Winter)
    strcpy(countries[0].activities,"Skiing Activities");
    strcpy(countries[1].activities,"Tour of the Swiss Alphs");
    strcpy(countries[0].season,"winter");
    strcpy(countries[1].season,"winter");
    strcpy(countries[0].country_name,"Andorra");
    strcpy(countries[1].country_name,"Switzerland");
    countries[0].cost = 100;
    countries[1].cost = 100;
    //Second season(Summer)
    strcpy(countries[2].activities,"Hiking and Extreme Sports");
    strcpy(countries[3].activities,"Activities on the Beaches");
    strcpy(countries[2].season,"summer");
    strcpy(countries[3].season,"summer");
    strcpy(countries[2].country_name,"Spain");
    strcpy(countries[3].country_name,"Portugal");
    countries[2].cost = 400;
    countries[3].cost = 400;
    //Third season(Spring)
    strcpy(countries[4].activities,"Extreme Sports");
    strcpy(countries[5].activities,"Cultural and Historical tour");
    strcpy(countries[4].season,"spring");
    strcpy(countries[5].season,"spring");
    strcpy(countries[4].country_name,"France");
    strcpy(countries[5].country_name,"Italy");
    countries[4].cost = 300;
    countries[5].cost = 300;
    //Forth season (Autumn)
    strcpy(countries[6].activities,"Extreme Sports");
    strcpy(countries[7].activities,"Cultural and Historical tour");
    strcpy(countries[6].season,"autumn");
    strcpy(countries[7].season,"autumn");
    strcpy(countries[6].country_name,"Belgium");
    strcpy(countries[7].country_name,"Austria");
    countries[6].cost = 200;
    countries[7].cost = 200;

    char * activities [] = {"Skiing","Extreme Sports","Hiking","Tour of the Swiss Alphs","Activities on the Beaches","Cultural and Historical tour"};
    int budget;
    int activity;
    int flag_season;
    int final_choice;
    char season[10];
        printf("Travel agency Menu\nPlease respond the next set of questions to help you decide a destination\n");
        //Selecting an activity
        printf("Which activity do you prefer?\n1-Skiing\n2-Extreme sports\n3-Hiking\n4-Tour of the Swiss Alphs\n5-Activities on the Beaches\n6-Cultural and Historical Tour\n\n");
        scanf("%i",&activity);
        //Selecting a season
        printf("Write the season you like the most (Winter,Summer,Autumn,Spring):");
        scanf("%s",season);
        //Choosing the budget
        printf("Now please enter your budget:");
        scanf("%i",&budget);
        //Validations
        if(budget<100){
            printf("Invalid amount for budget\n\n");
        }else{
            if(activity<1 || activity>6){
                printf("Invalid activity number\n\n");
            }else{
                flag_season = 0;
                for(int i = 0; i < 8;i++){
                    if(NULL!=strstr(countries[i].activities,activities[activity-1])){
                        flag_season = 1;
                    }
                }
                if(flag_season == 0){
                    printf("Wrong season\n\n");
                }else{
                    //Final choice
                    final_choice = 0;
                    for(int i = 0; i < 8;i++){
                        if(NULL != strstr(countries[i].activities,activities[activity-1])&& 0 == strcmp(countries[i].season,season)&& countries[i].cost <= budget ){
                            printf("Your best destinations is %s\n",countries[i].country_name);
                            final_choice = 1;
                        }
                    }
                    if(final_choice == 0){
                        printf("There no destination available with all those things");
                    }
                }
            }
        }
    return 0;
}
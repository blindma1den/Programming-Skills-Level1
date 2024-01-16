/*5. Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:
It must have a login and validate the data; after the third failed attempt, it should be locked.
The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
The user must choose if they want to check an additional piece of luggage into the hold.
Hand luggage is free of charge.
The user must purchase both the outbound and return tickets.
The user can choose their preferred meal: Regular, Vegetarian, Kosher.
The program must collect the following data: Name, country of origin, passport, and destination country.
Upon completing the process, the system will display everything the user has previously chosen along with their information. 
The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//I don't have much time so this algorithm will be simpler than the other ones

int main(){
    int menu = 1;
    int menu_option;
    int account_flag = 0;
    int log_in_flag=0;
    int origin_country;
    int destiny_country;
    int log_in_counter = 0;
    int last_flag = 0;
    int year;
    int month;
    int day;
    int days;
    int return_day;
    int return_month;
    int return_year;
    int condition;
    char * conditions[]={"Economy","First class"};
    char * ptruser_username;
    char * ptruser_password;
    char * ptraux_username;
    char * ptraux_password;
    char * countries[]={"Turkey","Greece","Lebanon","Spain","Portugal"};
    int meal_option;
    char * meals[]={"Regular","Vegetarian","Kosher"};
    int additional_luggage;
    char * luggage_options[]={"Yes","No"};
    char * name;
    char * id;
    int final_response;
    while(menu == 1){
        //Menu
        printf("Turkish Airlines Menu, choose an option\n\n1-Create an account\n2-Log in and buy tickets\n3-Exit\n\n");
        scanf("%i",&menu_option);     
        switch (menu_option){      
            //Creating an account      
            case 1:
                if(account_flag==0){
                    ptruser_username = malloc(sizeof(char));
                    ptruser_password = malloc(sizeof(char));
                    printf("Creating a new Account , please enter a new username:");
                    scanf("%s",ptruser_username);
                    printf("Now enter your new password:\n");
                    scanf("%s",ptruser_password);
                    printf("Account created successfuly\n\n");
                    account_flag=1;
                }else{
                    printf("You already created an Account\n\n");
                }   
                break;
            case 2:
            //Log in
                if(account_flag==1){
                    ptraux_username = malloc(sizeof(char));
                    ptraux_password = malloc(sizeof(char));
                    printf("To continue please enter your Credentials\nUsername:");
                    scanf("%s",ptraux_username);
                    printf("Now enter the password:");
                    scanf("%s",ptraux_password);
                    //Validating credentials
                    if( 0 == strcmp(ptruser_username, ptraux_username) && 0 == strcmp(ptruser_password,ptraux_password)){
                        printf("Log in Successful\nNow please choose an Origin Country\n\n");
                        log_in_flag = 1;
                        for(int i = 0; i < 5; i++){
                            printf("%i-%s\n",i+1,countries[i]);
                        }
                        //Origin country
                        scanf("%i",&origin_country);
                        if(origin_country>0 && origin_country<6){
                            printf("Now please select a destiny country:\n\n");  
                            for(int i = 0; i < 5; i++){
                                if(0 == strcmp(countries[i],countries[origin_country-1])){
                                    
                                    continue;
                                }
                                printf("%i-%s\n",i+1,countries[i]);
                            }
                            //Destiny country
                            scanf("%i",&destiny_country);
                            if(destiny_country<6 && destiny_country>0){
                                //Date of the fly
                                printf("Now please enter the date of the flight\nYear(number):");
                                scanf("%i",&year);
                                printf("Month:");
                                scanf("%i",&month);
                                printf("Day:");
                                scanf("%i",&day);
                                if(year>=2024 && month>0 && month<13 && day>0 && day <31){
                                    //Condition of the seat
                                    printf("\n\nSelect a condition:\n1-Economy\n2-VIP\n\n");
                                    scanf("%i",&condition);
                                    if(condition>0 && condition<3){
                                        //Additional luggage
                                        printf("Do you want to check an additional piece of luggage?(It has an additional cost):\n1-Yes\n2-No\n");
                                        scanf("%i",&additional_luggage);                                        
                                        if(additional_luggage>0 && additional_luggage<3){
                                            //Meal Type
                                            printf("What type of meal do you prefer?:\n1-Regular\n2-Vegetarian\n3-Kosher\n");
                                            scanf("%i",&meal_option);                     
                                            if(meal_option>0 && meal_option<4){
                                                //Calculating the return fly date
                                                printf("\nHow long do you plan to stay?(number of days):");
                                                scanf("%i",&days);
                                                return_day = day;
                                                return_month = month;
                                                return_year = year;
                                                if(return_day + days > 31){                                                    
                                                    return_day = (return_day + days) % 31; 
                                                    if(return_day==0){
                                                        return_day++;
                                                    }                                                   
                                                    if(return_month == 12){
                                                        return_month = 1;
                                                        return_year++;                                                        
                                                    }else{
                                                        month++;
                                                    }                                                                               
                                                }else{
                                                    return_day =return_day + days;
;                                                }
                                                last_flag = 1;
                                                name = malloc(sizeof(char));
                                                id = malloc(sizeof(char));
                                                //Asking personal info
                                                printf("\nNow please enter your name:");
                                                scanf("%s",name);
                                                printf("\nEnter your passport number:");
                                                scanf("%s",id);
                                                //Showing all the choices 
                                                printf("\nFINAL PREVIEW\n\nName:%s\nPassport:%s\nOutbound ticket: Origin country:%s Destination country:%s\nDate(month/day/year):%i/%i/%i",name,id,countries[origin_country-1],countries[destiny_country-1],month,day,year);
                                                printf("\nReturn ticket: Origin country:%s Destiny country:%s\nDate(month/day/year):%i/%i/%i\n\n",countries[destiny_country-1],countries[origin_country-1],return_month,return_day,return_year);
                                                printf("Additional luggage: %s\n Meal type:%s",luggage_options[additional_luggage-1],meals[meal_option-1]);
                                                printf("Do you agree with this ?:\n1-Yes\n2-No\n");
                                                scanf("%i",&final_response);
                                                //Final choiche
                                                switch (final_response){
                                                    case 1:
                                                        printf("\n\nCongratulations");
                                                        menu=0;
                                                        break;
                                                    case 2:
                                                        break;
                                                    default:
                                                    printf("Invalid option\n\n");                                                        
                                                       break;
                                                }
                                            }else{
                                                printf("Invalid option\n\n");
                                            }
                                        }else{
                                            printf("Invalid option\n\n");
                                        }
                                    }else{
                                        printf("invalid option\n\n");
                                    }
                                }else{
                                    printf("Invalid date\n\n");
                                }                               
                            }else{
                                printf("Invalid option\n\n");
                            } 
                        }else{
                            printf("Invalid option\n\n");
                        }                                            
                    }else{
                        printf("Wrong credentials\n\n");
                        log_in_counter++;
                        if(log_in_counter==3){
                            printf("To many attempts, Locking the system");
                            menu=0;
                        }
                    }
                    break;
                }else{
                    printf("Please create an Account\n\n");
                }                
            default:
                menu=0;
                break;        
        }    
    }
    //Freing memory 
    if(account_flag==1){
        free(ptruser_password);
        free(ptruser_username);
    }
    if(log_in_flag == 1){
        free(ptraux_password);
        free(ptraux_username);
    }
    if(last_flag==0){
        free(name);
        free(id);
    }
    return 0;
}
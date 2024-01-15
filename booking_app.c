/*The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

Login; it should be locked after the third failed attempt.
The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
Single rooms are priced at $100 per night, double rooms at $200 per night, group rooms at $350 per night, VIP suites at $450 per night, and luxury suites at $550 per night, applicable at any time of the year.
The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), 
print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.*/

#include <stdio.h>
#include <string.h>
//Reservation data type
typedef struct reservation{
    char country[10];
    char city [10];
    char suit_type[10];
    char month[10];
    char day[10];
    char hour[10];
    int cost;
}reservation;

//User data type
typedef struct user{
    char username[20];
    char password[20];
    char name[20];
    char surname[20];
    char id[20];
    int first_time;
    int reservation_index;
    int total_cost;
    struct reservation reservations[256];
}user;

//Procedure to intialize a user data type
void user_constructor(user * u, char * user_u, char * user_p, int user_index){
    for(int i = 0; i < 20; i++){
        u[user_index].username[i]=' ';
        u[user_index].password[i]=' ';
        u[user_index].name[i]=' ';
        u[user_index].surname[i]=' ';
        u[user_index].id[i]=' ';
    }
    strcpy(u[user_index].username,user_u);
    strcpy(u[user_index].password,user_p);
    u[user_index].reservation_index=0;
    u[user_index].total_cost = 0;
    u[user_index].first_time = 0;

}
//Procedure to add a reservation to an user's account
void add_reservation(user* u, int user_index,char * country, char * city,char * month, char * day, char * hour , int cost){
    strcpy(u[user_index].reservations[u[user_index].reservation_index].city , city);
    strcpy(u[user_index].reservations[u[user_index].reservation_index].country , country);
    strcpy(u[user_index].reservations[u[user_index].reservation_index].month , month);
    strcpy(u[user_index].reservations[u[user_index].reservation_index].day , day);
    strcpy(u[user_index].reservations[u[user_index].reservation_index].hour , hour);
    u[user_index].reservations[u[user_index].reservation_index].cost = cost;
    u[user_index].reservation_index++;
    u[user_index].total_cost = u[user_index].total_cost + u[user_index].reservations[u[user_index].reservation_index].cost;
}

//Procedure to add the personal data to an user's account
void add_personal_information(user * u, int user_index, char * name, char *surname, char *id){
    strcpy(u[user_index].name , name);
    strcpy(u[user_index].surname, surname);
    strcpy(u[user_index].id, id);
    u[user_index].first_time=1;
}

int main(){
    int menu1=1;
    int menu2;
    int menu_option;
    int user_counter = 0;
    int log_in_flag;
    int log_in_fails = 0;
    int user_index;
    int country_option;
    int place_option;
    int city_flag;
    char month[10];
    char day[10];
    char hour[5];
    int room_option;
    int room_amount;
    int nights;
    int total_price;
    int price_option;
    int another_reservation;
    user users[256];
    char user_u [20];
    char user_p [20];
    char user_name[20];
    char user_surname[20];
    char user_id[20];
    //Available countries
    char * countries []= {"Spain" , "Germany","Italy","France","Portugal"};
    char * cities[5][3];
    //spain's cities
    cities[0][0]="Barcelona";
    cities[0][1]= "Madrid";
    cities[0][1]="Valencia";
    //Germany's cities
    cities[1][0]="Munich";
    cities[1][1]="Berlin";
    //Italy's cities
    cities[2][0]="Rome";
    cities[2][1]="Milan";
    //France's Cities
    cities[3][0]="Paris";
    cities[3][1]="Marseille";
    //Portugal's cities
    cities[4][0]="Madeira";
    cities[4][1]="Lisbon";
    cities[4][2]="Porto";
    // single rooms, double rooms, group rooms , VIP suites,luxury suites
    int rooms[]={ 3 ,6 ,6, 6,3};
    //Price for room
    int rooms_price[]={100 ,200, 350,450, 550}; 
    while(menu1==1){
        //Main Menu
        printf("RH Hotels Menu\nPlease Select an option\n1-Create an account\n2-Log in\n3-Exit\n\n");
        scanf("%i",&menu_option);
        switch(menu_option){
            //Creating an Account
            case 1:
                printf("Creating an Account\nPlease enter a new Username(no blanck spaces):");
                scanf("%s",user_u);
                printf("Now please enter a new password (No blank spaces):");
                scanf("%s",user_p);
                user_constructor(users,user_u,user_p,user_counter);
                user_counter++;
                for(int i = 0 ; i < 20; i++){
                    user_u[i]=' ';
                    user_p[i]=' ';
                }
                break;
            case 2:
            //Log in
                if(user_counter>=1){
                    printf("Log in\nPlease enter your Credentials\n\nUsername:");
                    scanf("%s",user_u);
                    printf("Now the password:");
                    scanf("%s",user_p);
                    log_in_flag = 0;
                    //Validating the credentials
                    for(int i = 0; i < user_counter; i++){
                        if(0 == strcmp(users[i].username,user_u) && 0 == strcmp(users[i].password,user_p)){
                            log_in_flag = 1;
                            user_index = i;
                        }
                    }                    
                    for(int i = 0 ; i < 20; i++){
                        user_u[i]=' ';
                        user_p[i]=' ';
                    }
                    //Choosing a Country
                    if(log_in_flag == 1){
                        printf("Log In Successful\n\nNow choose the an hotel location:\n1-Spain\n2-Germany\n3-Italy\n4-France\n5-Portugal\n\n");
                        scanf("%i",&country_option);
                        //Validating the country option
                        if(country_option<=5 && country_option>0){
                            printf("Please select a location:");
                            city_flag=0;
                            //Asking the city based on the choosen country and validating the answer
                            switch(country_option){
                                case 1:
                                    printf("The options are:\n1-Barcelona\n2-Madrid\n3-Valencia\n\n");
                                    scanf("%i",&place_option);
                                    if(place_option>0 && place_option<4){
                                        city_flag = 1;
                                    }else{
                                        printf("Invalid option\n\n");
                                    }
                                    break;                                
                                case 2:     
                                    printf("The options are:\n1-Munich\n2-Berlin\n\n");
                                    scanf("%i",&place_option);  
                                    if(place_option==1 || place_option==2){
                                        city_flag = 1;
                                    }else{
                                        printf("Invalid option\n\n");
                                    }                         
                                    break;
                                case 3:
                                    printf("The options are:\n1-Rome\n2-Milan\n\n");
                                    scanf("%i",&place_option);
                                    if(place_option==1 || place_option==2){
                                        city_flag = 1;
                                    }else{
                                        printf("Invalid option\n\n");
                                    }
                                    break;
                                case 4:
                                    printf("The options are:\n1-Paris\n2-Marseille\n\n");
                                    scanf("%i",&place_option);
                                    if(place_option==1 || place_option==2){
                                        city_flag = 1;
                                    }else{
                                        printf("Invalid option\n\n");
                                    }
                                    break;
                                case 5:
                                    printf("The option are:\n1-Madeira\n2-Lisbon\n3-Porto\n\n");
                                    scanf("%i",&place_option);
                                    if(place_option>0 && place_option<4){
                                        city_flag = 1;
                                    }else{
                                        printf("Invalid option\n\n");
                                    }
                                    break;                                
                                default:
                                    printf("Invalid option\n\n");
                                    break;
                            }
                            //Getting the date of the reservation
                            if(city_flag==1){
                                printf("\nEnter the month's name:");
                                scanf("%s",month);
                                printf("\nEnter the day's name:");
                                scanf("%s",day);
                                printf("\nEnter the hour:");
                                scanf("%s",hour);
                                menu2=1;
                                while(menu2==1){
                                    //The type of room, amount of rooms and nights
                                    printf("Reservation MENU\n\n");                                    
                                    printf("Now select a room type\n1-Single room\n2-Double room\n3-Group room\n4-VIP suite\n5-Luxury suite\n\n");
                                    scanf("%i",&room_option);
                                    if(room_option>0 && room_option<6){
                                        printf("\nNow enter the amount of rooms:");
                                        scanf("%i",&room_amount);
                                        if(room_amount<=rooms[room_option-1] && room_amount>0){                                            
                                            printf("\nPlease enter the number of nights:");
                                            scanf("%i",&nights);
                                            if(nights>0){
                                                //Calculating the price
                                                total_price =  rooms_price[room_option-1] * nights;
                                                rooms[room_option-1] = rooms[room_option-1] - room_amount;
                                                //Getting the user personal info
                                                //Only the first time we ask the user his personal info
                                                if(users[user_index].first_time==0){
                                                    printf("Enter your name:");
                                                    scanf("%s",user_name);
                                                    printf("\nEnter your surname:");
                                                    scanf("%s",user_surname);
                                                    printf("\nEnter your ID/Passport number:");
                                                    scanf("%s",user_id);
                                                }
                                                //Showing the total price
                                                printf("The total price would be %i, do you agree ?\n1-Yes\n2-No\n\n",total_price);
                                                scanf("%i",&price_option);
                                                switch(price_option){
                                                    case 1:
                                                        add_reservation(users,user_index,countries[country_option-1],cities[country_option-1][place_option-1],month,day,hour,total_price);
                                                        if(users[user_index].first_time==0){
                                                            add_personal_information(users,user_index,user_name,user_surname, user_id);
                                                        }                                                        
                                                        printf("\nReservation Successful\n\n");
                                                        //Asking if he wants to make another reservation
                                                        printf("Do you want to reserve another type or book?\n1-Yes\n2-No\n\n");
                                                        scanf("%i",&another_reservation);
                                                        switch(another_reservation){
                                                            case 1:
                                                                break;
                                                            case 2:
                                                                menu2=0;
                                                                printf("\n");
                                                                break;
                                                            default:
                                                                printf("Invalid option");
                                                                menu2=0;
                                                                menu1=0;
                                                                break;
                                                        }
                                                        break;
                                                    case 2:
                                                        menu2=0;
                                                    default:
                                                        printf("Invalid option");
                                                        menu2=0;
                                                        menu1=0;
                                                        break;                                            
                                                }
                                            }else{
                                                printf("Invalid amount\n\n");
                                            }                            
                                        }else{
                                            printf("There are no enough rooms of that type avalaible, try again\n\n");
                                        }
                                    }else{
                                        printf("Invalid option\n\n");
                                        menu2=0;
                                    }
                                }
                            }else{
                                printf("Invalid option\n\n");
                                menu2=0;
                            }
                        }else{
                            printf("Invalid option");
                            menu2=0;
                        }
                    }else{
                        printf("Wrong Credentials\n");
                        log_in_fails++;
                        if(log_in_fails == 3){
                            printf("Too many Attempts");
                            menu1=0;
                        }
                    }
                }else{
                    printf("Please create an Account");
                }
                break;  
            default:
                menu1=0;
                break;
        }
    }
    return 0;
}
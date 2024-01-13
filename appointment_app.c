/*The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
*/

#include <stdio.h>
#include <string.h>

typedef struct user{
    char username[20];
    char password[20];
    int appointments;
    int specialties[9];
    char *doctors[3];
    int doctor_index;
}user;
//Procedure to initialize a user data type
void user_constructor(user * u,const int index_u,const char * username, const char * password){
    strcpy(u[index_u].username,username);
    strcpy(u[index_u].password,password);
    u[index_u].appointments = 0;
    u[index_u].doctor_index = 0;
    for(int i =0; i <9;i++ ){
        u[index_u].specialties[i]=0;
    }
}
//Procedure to erase the data inside of a user data type
void user_erase_data(user * u, const int id,const int specialty_opt){
    u[id].specialties[specialty_opt] = 0;
    u[id].doctor_index--;
    u[id].doctors[u[id].doctor_index] = ' ';
}

int main(){
    int menu1 = 1;
    int menu_option;
    int menu2 ;
    char username[20];
    char password[20];
    int specialty_option;
    int doctor_option;
    int time_option;
    int hour_option;
    int log_in_counter = 0;
    user users[256];
    int user_index = 0;
    int user_ID;
    int log_in_flag;
    int doctor_flag;
    char *doctors[]={"Bob","Chacin","Sirica"};
    while(menu1==1){
        printf("Appointment Menu\nPlease select an option\n\n1-Create an account\n2-Log in\n3-Exit\n\n");
        scanf("%i",&menu_option);
        switch(menu_option){
            //Creating an Account
            case 1:
                printf("Creating an Account\nPlease enter a new username(No blank spaces):");
                scanf("%s",username);
                printf("Now enter a new password(No blank spaces):");
                scanf("%s",password);
                user_constructor(users,user_index,username,password);
                user_index++;
                break;
            case 2:
                menu2 = 1;
                if(user_index>=1){
                    while( menu2== 1){
                        //Verifying the credentials
                        for(int i = 0; i < 20; i++){
                        username[i]=' ';
                        password[i]=' ';
                        }
                        log_in_flag=0;     
                        printf("Enter your credentials\nUsername:");
                        scanf("%s",username);
                        printf("Now enter your password:");
                        scanf("%s",password);
                        for(int i = 0; i < user_index; i ++){
                            if(0 == strcmp(username,users[i].username) && 0 == strcmp(password,users[i].password)){
                                user_ID = i;
                                log_in_flag=1;
                            }
                        }
                        if(users[user_ID].appointments<3){
                            //Valid credentials
                            if(log_in_flag==1){
                                if(users[user_ID].appointments<3){
                                    printf("Please select a specialty:\n\n1-General Medicine\n2-Emergency Care\n3-Clinical Analysis\n4-Cardiology\n5-Neurology\n6-Nutrition\n7-Physiotherapy\n8-Traumatology\n9-Internal Medicine\n\n");
                                    //Selecting a specialty
                                    scanf("%i",&specialty_option);                                    
                                    if(specialty_option <10 && specialty_option >0){
                                        specialty_option = specialty_option - 1;
                                        //Verifying if is a valid specialty
                                        if(0 == users[user_ID].specialties[specialty_option]){
                                            //Saving the specialty choice
                                            users[user_ID].specialties[specialty_option] = 1;
                                            //Showing the doctors
                                            printf("Now select a doctor:\n\n");
                                            for(int i = 0; i < 3; i++){
                                                printf("%i- %s\n",i+1,doctors[i]);
                                            }
                                            //Selecting a doctor
                                            scanf("%i",&doctor_option);
                                            if(doctor_option<4 && doctor_option >0){
                                                doctor_option = doctor_option -1;
                                                doctor_flag= 0;
                                                //Verifying if the user have already an Appointemt with the selected doctor
                                                for(int i = 0; i < users[user_ID].doctor_index; i++){
                                                    if(0 == strcmp(users[user_ID].doctors[i],doctors[doctor_option])){
                                                        doctor_flag = 1;
                                                    }
                                                }                                        
                                                if( doctor_flag == 0){
                                                    //saving the doctor choice
                                                    users[user_ID].doctors[users[user_ID].doctor_index]=doctors[doctor_option];
                                                    users[user_ID].doctor_index++;
                                                    printf("At what time would you like?\n1-Morning\n2-Afternoon\n\n");
                                                    //Selecting a time of the day and hour
                                                    scanf("%i",&time_option);
                                                    switch(time_option){
                                                        //Morning
                                                        case 1:
                                                            printf("Now select an hour:\n\n1- 8:00 am\n2- 9:00 am\n3- 10:00 am\n\n");
                                                            scanf("%i",&hour_option);
                                                            if(hour_option<4 && hour_option>0){
                                                                printf("Congratulations,your appointment is booked\n\n");
                                                                users[user_ID].appointments++;
                                                            }else{
                                                                printf("Invalid option");
                                                                user_erase_data(users,user_ID,specialty_option);                                                                
                                                            }
                                                            
                                                            menu2=0;
                                                            break;  
                                                        //Afternoon                                                      
                                                        case 2:                                                    
                                                            printf("Now select an hour:\n\n1- 4:00 am\n2- 5:00 am\n3- 6:00 am\n\n");
                                                            scanf("%i",&hour_option);
                                                            if(hour_option<4 && hour_option>0){
                                                                printf("Congratulations,your appointment is booked\n\n");
                                                                users[user_ID].appointments++;
                                                            }else{
                                                                printf("Invalid option");
                                                                user_erase_data(users,user_ID,specialty_option);
                                                            }                                                            
                                                            menu2=0;
                                                            break;
                                                        default:
                                                            printf("Invalid option\n\n");
                                                            menu2 = 0;
                                                            user_erase_data(users,user_ID,specialty_option);                                    
                                                            break;
                                                        }                                             
                                                }else{
                                                    printf("You already have an appointment with doctor %s\n\n",doctors[doctor_option]);
                                                    users[user_ID].specialties[specialty_option] = 0;
                                                }
                                            }else{
                                                printf("Invalid option\n\n");
                                                menu2=0;
                                            }                                    
                                        }else{
                                            printf("You already have an appointment in that specialty\n\n");
                                        }
                                    }else{
                                        printf("Invalid option\n\n");
                                        menu2 = 0;
                                    }
                                }else{
                                    printf("Too many appointments");
                                    menu2=0;
                                }
                            }else{
                                log_in_counter++;
                                printf("Wrong credential\n\n");
                                if(log_in_counter==3){
                                    printf("Too many attempts");
                                    menu2=0;
                                    menu1=0;
                                }
                            }
                        }else{
                            printf("You have to many appointments\n\n");
                        }
                    }
                }else{
                    printf("Please create an account\n\n");
                }        
                break;
            default:
                menu1=0;
                break;
        }
    }
    return 0;
}
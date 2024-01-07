Author: [@blindma1den](https://github.com/blindma1den)

# Level 1 exercises

## 1. Manchester United FC program

Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.

The system should also allow comparison between two players. Use the following player profiles:

| Player             | Goals | Speed points | Assists points | Passing accuracy points | Defensive involvements points | Jersey number |
| ------------------ | ----- | ------------ | -------------- | ----------------------- | ----------------------------- | ------------- |
| Bruno Fernandes    | 5     | 6            | 9              | 10                      | 3                             | 8             |
| Rasmus Hojlund     | 12    | 8            | 2              | 6                       | 2                             | 11            |
| Harry Maguire      | 1     | 5            | 1              | 7                       | 9                             | 5             |
| Alejandro Garnacho | 8     | 7            | 8              | 6                       | 0                             | 17            |
| Mason Mount        | 2     | 6            | 4              | 8                       | 1                             | 7             |

The program functions as follows: The coach accesses the system and encounters a menu with the following options:

- [ ] **Player Review:** By entering the player's jersey number, they can access the player's characteristics.
- [ ] **Compare two players:** The system prompts for two jersey numbers and displays the data of both players on screen.
- [ ] **Identify the fastest player:** Displays the player with the most points in speed.
- [ ] **Identify the top goal scorer:** Displays the player with the most points in goals.
- [ ] **Identify the player with the most assists:** Displays the player with the most points in assists.
- [ ] **Identify the player with the highest passing accuracy:** Displays the player with the most points in passing accuracy.
- [ ] **Identify the player with the most defensive involvements:** Displays the player with the most points in defensive involvements.
- [ ] The system should also allow returning to the main menu.

## 2. Travel agency system

A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

- **Winter:** Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
- **Summer:** Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
- **Spring:** France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
- **Autumn:** Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.

> [!NOTE]  
> Traveling in winter costs `$100`, in autumn `$200`, in spring `$300`, and in summer `$400`.

Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.

> [!IMPORTANT]  
> With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

> [!TIP]
> You could consider the user's budget

## 3. Hospital appointment algorithm

The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

- [ ] It must have a login and validate the data; after the third failed attempt, it should be locked.
- [ ] The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
- [ ] There are 3 doctors for each specialty.
- [ ] The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
- [ ] The maximum limit for appointments, in general, is 3.
- [ ] Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
- [ ] Display available specialists.
- [ ] The user can choose their preferred specialist.

The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.

## 4. Hotel reservation algorithm

The RH Hotels chain has hired you to design the booking algorithm for their mobile application:

- [ ] Login; it should be locked after the third failed attempt.
- [ ] The RH Hotels chain exists in 5 countries: Spain, France, Portugal, Italy, and Germany.
- [ ] Each country has its own hotels located in: Madrid, Barcelona, Valencia, Munich, Berlin, Rome, Milan, Paris, Marseille, Madeira, Lisbon, and Porto.
- [ ] All hotels have 24 rooms each: 6 VIP suites, 3 single rooms, 6 double rooms, 6 group rooms, and 3 luxury suites.
- [ ] The user can make reservations at any time of the year and at any hour, and book as many rooms as desired.
- [ ] Single rooms are priced at `$100` per night, double rooms at `$200` per night, group rooms at `$350` per night, VIP suites at `$450` per night, and luxury suites at `$550` per night, applicable at any time of the year.
- [ ] The algorithm functions as follows: Login, choose country, choose city, choose room type, select the number of nights, collect user data (name, surname, ID/passport), print the total cost, and if the user agrees, print a confirmation message for the reservation. If not, return to the main menu.

## 5. Airline ticket reservation algorithm

Turkish Airlines has just launched an offer to travel among the following destinations: Turkey, Greece, Lebanon, Spain, and Portugal. Develop an algorithm with the following characteristics:

- [ ] It must have a login and validate the data; after the third failed attempt, it should be locked.
- [ ] The user must choose the origin country and the destination country, the flight date, and the condition: Economy or First Class.
- [ ] The user must choose if they want to check an additional piece of luggage into the hold.
- [ ] Hand luggage is free of charge.
- [ ] The user must purchase both the outbound and return tickets.
- [ ] The user can choose their preferred meal: Regular, Vegetarian, Kosher.
- [ ] The program must collect the following data: Name, country of origin, passport, and destination country.
- [ ] Upon completing the process, the system will display everything the user has previously chosen along with their information.
- [ ] The system will provide the option to confirm the reservation or cancel it. If the user chooses YES, a confirmation message will appear. If not, it will return to the main menu.

---

Enjoy!

Author: [@blindma1den](https://github.com/blindma1den)

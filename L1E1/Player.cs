using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace L1E1
{
    internal class Player
    {

        public int number { get; set; }
        public string name { get; set; }
        public int goals { get; set; }
        public int speedPoints { get; set; }   
        public int assistsPoints { get; set; }
        public int passingPoints { get; set; }
        public int defensePoints { get; set; }

        public Player(string playerName, int playerNumber, int playerGoals, int playerSpeed, int playerAssistsPoints, int playerPassingPoints, int playerDefensePoints)
        {
            this.name = playerName;
            this.number = playerNumber;
            this.goals = playerGoals;
            this.speedPoints = playerSpeed;
            this.assistsPoints = playerAssistsPoints;
            this.passingPoints = playerPassingPoints;
            this.defensePoints = playerDefensePoints;

        }

    }
}

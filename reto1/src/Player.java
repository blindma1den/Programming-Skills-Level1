public class Player {

    private final String NAME;
    private Integer goals;
    private Integer speed;
    private Integer assists;
    private Integer accuracy;
    private Integer defence;

    public Player(String NAME, Integer goals, Integer speed, Integer assists, Integer accuracy, Integer defence) {
        this.NAME = NAME;
        this.goals = goals;
        this.speed = speed;
        this.assists = assists;
        this.accuracy = accuracy;
        this.defence = defence;
    }

    public String getNAME() {
        return NAME;
    }

    public Integer getGoals() {
        return goals;
    }

    public void setGoals(Integer goals) {
        this.goals = goals;
    }

    public Integer getSpeed() {
        return speed;
    }

    public void setSpeed(Integer speed) {
        this.speed = speed;
    }

    public Integer getAssists() {
        return assists;
    }

    public void setAssists(Integer assists) {
        this.assists = assists;
    }

    public Integer getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(Integer accuracy) {
        this.accuracy = accuracy;
    }

    public Integer getDefence() {
        return defence;
    }

    public void setDefence(Integer defence) {
        this.defence = defence;
    }

    @Override
    public String toString() {
        return "Player{" +
                "NAME='" + NAME + '\'' +
                ", goals=" + goals +
                ", speed=" + speed +
                ", assists=" + assists +
                ", accuracy=" + accuracy +
                ", defence=" + defence +
                '}';
    }
}

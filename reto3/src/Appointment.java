
public class Appointment {
    private String name;
    private String speciality;
    private Integer date;


    public Appointment(String name, String speciality, Integer date) {
        this.name = name;
        this.speciality = speciality;
        this.date = date;
    }

    public Appointment() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSpeciality() {
        return speciality;
    }

    public void setSpeciality(String speciality) {
        this.speciality = speciality;
    }

    public Integer getdate() {
        return date;
    }

    public void setdate(Integer date) {
        this.date = date;
    }

    @Override
    public String toString() {
        return "Appointment{" +
                "name='" + name + '\'' +
                ", speciality='" + speciality + '\'' +
                ", date=" + date +
                '}';
    }
}

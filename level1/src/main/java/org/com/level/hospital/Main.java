package org.com.level.hospital;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

import static org.com.level.hospital.Printer.printOptions;

public class Main {
    static Authenticator authenticator = new Authenticator();
    static Scanner scanner = new Scanner(System.in);
    static User user;

    public static void main(String[] args) {
        user = new User("lol", "pass", Map.of());
        authenticator.authProcessFor(3, user);
        while (authenticator.isLogged && ! user.userHave3Appointments()) {
            searchAppointment();
            authenticator.shouldLogOut();
        }
    }


    private static void searchAppointment() {

        System.out.println("Select the speciality");
        var selectedSpeciality = printOptions(Utils.specialities);
        var possibleDoctors    = filterDoctorsBySpeciality(selectedSpeciality);

        System.out.println("Possible Doctors for this Speciality");
        var numberSelectedDoctor = printOptions(possibleDoctors.stream()
                                                               .map(Doctor :: name)
                                                               .toList());

        var selectedDoctorByUser = possibleDoctors.get(numberSelectedDoctor);
        var possibleSlots = filterSlotsByDoctorAndUser(selectedDoctorByUser);

        System.out.println("Select a free slot");
        var numberOfSelectedSlot = printOptions(possibleSlots);

        var appointment = possibleSlots.get(numberOfSelectedSlot).registerAppointment();

        user = user.registerAppointment(selectedDoctorByUser, appointment);

        Doctor updatedDoctor = updateDoctorWithNewAppointment(appointment, selectedDoctorByUser);

        updateDoctorsList(updatedDoctor);

    }

    private static Doctor updateDoctorWithNewAppointment(Slot appointment,
                                                         Doctor selectedDoctorByUser) {
        var updatedSlotList = selectedDoctorByUser.getFreeSlotStream(user)
                                                  .map(slot -> slot.id().equals(appointment.id()) ? appointment : slot)
                                                  .toList();
        return selectedDoctorByUser.registerAppointment(updatedSlotList);
    }

    private static List<Slot> filterSlotsByDoctorAndUser(Doctor selectedDoctorByUser) {
        return selectedDoctorByUser.getFreeSlotStream(user).toList();
    }

    private static void updateDoctorsList(Doctor selectedDoctor)
    {
        Utils.doctors = Utils.doctors.stream().map(doctor ->
                                                           doctor.name()
                                                                 .equals(selectedDoctor.name())?
                                                                   selectedDoctor: doctor).toList();
    }


    private static List<Doctor> filterDoctorsBySpeciality(int selectedSpeciality) {
        return Utils.doctors.stream()
                            .filter(doctor -> (doctor.speciality()
                                                     .equals(Utils.specialities.get(selectedSpeciality)) &&
                                               (! user.doctorAndAppointment()
                                                      .containsKey(doctor.name()))
                            )).toList();
    }

}

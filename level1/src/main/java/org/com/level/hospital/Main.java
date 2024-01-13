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

        var appointment = possibleSlots.get(numberOfSelectedSlot)
                                               .registerAppointment();

        user = user.registerAppointment(selectedDoctorByUser,
                                        appointment);

        Utils.doctors = updateDoctor(possibleSlots,
                                     appointment,
                                     selectedDoctorByUser);

    }

    private static List<Slot> filterSlotsByDoctorAndUser(Doctor selectedDoctorByUser) {
        return selectedDoctorByUser.slotList()
                                   .stream()
                                   .filter(Slot :: free)
                                   .filter(Main :: isFreeForUser)
                                   .toList();
    }

    private static List<Doctor> updateDoctor(List<Slot> possibleSlots,
                                             Slot newSlot,
                                             Doctor selectedDoctor)
    {
        var updatedSlotList = possibleSlots.stream()
                                           .map(slot -> slot.id()
                                                            .equals(newSlot.id()) ? newSlot : slot)
                                           .toList();

        return Utils.doctors.stream().map(doctor -> {
            if (doctor.name().equals(selectedDoctor.name())) {
                return new Doctor(selectedDoctor.speciality(),
                                  selectedDoctor.name(),
                                  updatedSlotList);
            }
            return doctor;
        }).toList();
    }

    private static boolean isFreeForUser(Slot slot) {
        return user.getUserSlotsStream()
                   .noneMatch(slotFromUser -> slotFromUser.timeStamp().equals(slot.timeStamp()));
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

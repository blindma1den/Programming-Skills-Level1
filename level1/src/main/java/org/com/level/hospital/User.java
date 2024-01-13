package org.com.level.hospital;

import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public record User(String name,
                   String password,
                   Map<String, Slot> doctorAndAppointment) {
    Stream<Slot> getUserSlotsStream() {
        return this.doctorAndAppointment()
                .values()
                .stream();
    }

    User registerAppointment(Doctor selectedDoctor,
                             Slot newSlot) {
        var newMapSlot =
                Stream.concat(this.doctorAndAppointment().entrySet().stream(),
                              Stream.of(Map.entry(selectedDoctor.name(), newSlot)))
                      .collect(Collectors.toMap(Map.Entry :: getKey,
                                                Map.Entry :: getValue));
        return new User(this.name(), this.password(), newMapSlot);
    }

    boolean userHave3Appointments() {
        if (this.doctorAndAppointment().size() >= 3) {
            System.out.println("Maximal Number Appointments gotten");
            return true;
        }
        return false;
    }
}

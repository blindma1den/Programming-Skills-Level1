package org.com.level.hospital;

import java.util.List;
import java.util.stream.Stream;

public record Doctor(String speciality, String name, List<Slot> slotList) {
     Stream<Slot> getFreeSlotStream(User user) {
        return this.slotList().stream().filter(user :: isFreeForUser)
                   .filter(Slot :: free);
    }

    Doctor registerAppointment(List<Slot> updatedSlotList) {
        return new Doctor(this.speciality(),
                          this.name(),
                          updatedSlotList);
    }
}

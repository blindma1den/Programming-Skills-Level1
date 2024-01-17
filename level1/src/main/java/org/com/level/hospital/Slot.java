package org.com.level.hospital;

public record Slot(Integer id, String timeStamp, boolean free) {
    Slot registerAppointment() {
        return new Slot(this.id(),
                        this.timeStamp(),
                        false);
    }
}

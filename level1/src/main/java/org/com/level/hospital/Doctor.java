package org.com.level.hospital;

import java.util.List;

public record Doctor(String speciality, String name, List<Slot> slotList) {
}

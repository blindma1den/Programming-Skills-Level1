package org.com.level.hospital;

import java.util.List;

public class Utils {
    static List<String> specialities = List.of("General Medicine",
                                               "Emergency Care",
                                               "Clinical Analysis",
                                               "Cardiology",
                                               "Neurology",
                                               "Nutrition",
                                               "Physiotherapy",
                                               "Traumatology",
                                               "Internal Medicine");
    static List<Doctor> doctors = List.of(
            new Doctor("General Medicine", "Dr. Ana Torres", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("General Medicine", "Dr. Carlos Ruiz", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("General Medicine", "Dr. Laura García", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Emergency Care", "Dr. Roberto Fernández", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Emergency Care", "Dr. Sofia Martínez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Emergency Care", "Dr. Juan Pérez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Clinical Analysis", "Dr. María López", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Clinical Analysis", "Dr. Jorge Gómez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Clinical Analysis", "Dr. Patricia Díaz", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Cardiology", "Dr. Fernando Sánchez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Cardiology", "Dr. Isabel Rodríguez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Cardiology", "Dr. Luis Jiménez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Neurology", "Dr. Carmen Ortiz", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Neurology", "Dr. Diego Vázquez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Neurology", "Dr. Elena Moreno", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Nutrition", "Dr. Sara Navarro", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Nutrition", "Dr. Rafael Morales", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Nutrition", "Dr. Clara Fernández", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Physiotherapy", "Dr. José González", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Physiotherapy", "Dr. Teresa Romero", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Physiotherapy", "Dr. Daniel Castillo", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Traumatology", "Dr. Laura Martín", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Traumatology", "Dr. Miguel Ángel Soto", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Traumatology", "Dr. Beatriz Rivas", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Internal Medicine", "Dr. Óscar Domínguez", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Internal Medicine", "Dr. Alicia Vega", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true))),
            new Doctor("Internal Medicine", "Dr. Guillermo Alonso", List.of(
                    new Slot(1, "8-9", true),
                    new Slot(2, "9-10", true),
                    new Slot(3, "10-11", true)))
    );
}

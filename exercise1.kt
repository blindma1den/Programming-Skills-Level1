package com.reyesmicaela.programmingskillslevel1kotlin

data class Player(
    val name: String,
    val goals: Int,
    val pointsSpeed: Int,
    val pointsAssists: Int,
    val pointsPassing: Int,
    val defensiveInvolvements: Int,
    val jerseyNumber: Int
)

val players = listOf(
    Player("Bruno Fernandes", 5, 6, 9, 10, 3, 8),
    Player("Rasmus Hojlund", 12, 8, 2, 6, 2, 11),
    Player("Harry Maguire", 1, 5, 1, 7, 9, 5),
    Player("Alejandro Garnacho", 8, 7, 8, 6, 0, 17),
    Player("Mason Mount", 2, 6, 4, 8, 1, 7)
)

val menuOptions = listOf(
    "Ver Jugador",
    "Comparar dos jugadores",
    "Jugador más rápido",
    "Máximo goleador",
    "Jugador con más asistencias",
    "Jugador con la mayor precisión en pases",
    "Jugador con más intervenciones defensivas",
    "Volver al Menú Principal"
)

fun main() {
    while (true) {
        when (selectOption("seleccionar una opcion", menuOptions)) {
            1 -> {
                val player =
                    selectOption("ingresar un numero de camiseta", players.map { it.name })
                println(players[player - 1])
            }

            2 -> {
                val player1Index = selectOption(
                    "ingresar numero del primer jugador",
                    players.map { it.name }
                )
                val player1 = players[player1Index - 1]
                val player2 = selectOption(
                    menssage = "ingresar numero del segundo jugador",
                    list = players.map { it.name },
                    notAvailable = player1Index
                )
                println(player1)
                println(players[player2 - 1])
            }

            3 -> println(players.sortedBy { it.pointsSpeed }.last())
            4 -> println(players.sortedBy { it.goals }.last())
            5 -> println(players.sortedBy { it.pointsAssists }.last())
            6 -> println(players.sortedBy { it.pointsPassing }.last())
            7 -> println(players.sortedBy { it.defensiveInvolvements }.last())
            8 -> continue
        }
    }
}

private fun selectOption(menssage: String, list: List<String>, notAvailable: Int? = null): Int {
    while (true) {
        println(menssage)
        list.forEachIndexed { index, it -> println("${index + 1}. $it") }
        try {
            val input = readln().toInt()
            if (input == notAvailable) {
                println("seleccione un jugador distinto al primero")
                continue
            }
            if (input > list.size || input == notAvailable) {
                println("ingrese un numero valido")
                continue
            } else {
                return input
            }
        } catch (e: NumberFormatException) {
            println("ingrese un numero válido")
            continue
        }
    }
}
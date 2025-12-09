package at.possnig.aoc25.day1.part1

import java.io.File

fun main(args: Array<String>) {
    var position = 50
    var counter = 0
    File("src/main/resources/day1/${args[0]}").useLines { it.toList() }
        .map { it.substring(1).toInt() * if (it[0] == 'L') -1 else 1}
        .forEach {
            position += it
            if (position % 100 == 0) counter++
        }
    println(counter)
}
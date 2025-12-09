package at.possnig.aoc25.day1.part2

import java.io.File
import kotlin.math.abs

fun main(args: Array<String>) {
    var counter = 0
    var position = 50
    File("src/main/resources/day1/${args[0]}").useLines { it.toList() }
        .map { it.substring(1).toInt() * if (it[0] == 'L') -1 else 1 }
        .forEach {
            position += it
            if (position <= 0 && it != position) {
                counter++
            }
            counter += abs(position) / 100
            position = position.mod(100)
        }
    println(counter)
}
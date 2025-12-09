package at.possnig.aoc25.day4

import java.io.File
import kotlin.math.max
import kotlin.math.min

fun main(args: Array<String>) {
    File("src/main/resources/day4/${args[0]}").useLines { it.toList() }
        .map { it.toCharArray() }
        .toTypedArray()
        // Part 1 verändert den Array in-place, ist also gleichzeitig der erste Durchlauf für Part 2
        .also { input ->
            input.also { part1(it) }
                .let { input.flatMap { it.asSequence() }.count { it == 'X' } }
                .also { println("Part 1: $it") }
        }.also { input ->
            var changed: Boolean
            do {
                changed = part2(input)
            } while (changed)
            input.flatMap { it.asSequence() }.count { it == 'X' }
                .also { println("Part 2: $it") }
        }
}

fun part1(lines: Array<CharArray>) = markAccessible(lines, setOf('@', 'X'))
fun part2(lines: Array<CharArray>) = markAccessible(lines, setOf('@'))

fun markAccessible(lines: Array<CharArray>, markers: Set<Char>): Boolean {
    var changed = false
    for (i in lines.indices) {
        for (j in lines[i].indices) {
            if (lines[i][j] == '.' || lines[i][j] == 'X') continue
            val occupied = countOccupiedNeighbours(markers, lines, i, j)
            if (occupied < 4) {
                lines[i][j] = 'X'
                changed = true
            }
        }
    }
    return changed
}

fun countOccupiedNeighbours(markers: Set<Char>, lines: Array<CharArray>, i: Int, j: Int): Int {
    var occupied = 0
    for (k in max(i - 1, 0)..min(i + 1, lines.size - 1)) {
        for (l in max(j - 1, 0)..min(j + 1, lines[i].size - 1)) {
            if (k == i && l == j) continue
            if (markers.contains(lines[k][l])) {
                occupied++
            }
        }
    }
    return occupied
}
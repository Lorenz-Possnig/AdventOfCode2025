package at.possnig

import java.io.File
import java.util.regex.Pattern

fun main(args: Array<String>) {
    val lines = File("src/main/resources/day6/${args[0]}").useLines { it.toList() }
    val numberLines = lines.subList(0, lines.size - 1)
    val last = lines.last()
    val numbers = numberLines
        .map { it.trim() }
        .map { line -> line.split(Pattern.compile(" +"))
            .map { it.trim() }
            .map { it.toLong() }
        }.transpose()
    val operations = last.split(Pattern.compile(" +")).map { it.toOperation() }
    operations.mapIndexed { i, op -> numbers[i].reduce(op) }
        .sum()
        .also { println("Part 1: $it") }
    val maxLen = numberLines.maxOf { it.length }
    val cephMath = numberLines.map { it + " ".repeat(maxLen - it.length) }
        .map { it.toList() }
        .transpose()
        .map { it.asString() }
        .splitOn { it.isBlank() }
        .map { it.reversed() }
        .reversed()
        .map { ls -> ls.map { it.trim().toLong() } }
    operations.reversed().mapIndexed { i, op -> cephMath[i].reduce(op) }
        .sum()
        .also { println("Part 2: $it") }
    println()
}

fun String.toOperation(): (Long, Long) -> Long =
    when (this.trim()) {
        "*" -> Long::times
        "+" -> Long::plus
        else -> throw Exception("Unknown operator")
    }

fun <T> List<List<T>>.transpose(): List<List<T>> =
    (this[0].indices).map { i -> (this.indices).map { j -> this[j][i] } }

fun <T> List<T>.splitOn(f: (T) -> Boolean): List<List<T>> {
    val result = mutableListOf<List<T>>()
    var current = mutableListOf<T>()
    for (i in this) {
        if (f(i)) {
            result.add(current)
            current = mutableListOf()
        } else {
            current.add(i)
        }
    }
    if (current.isNotEmpty()) {
        result.add(current)
    }
    return result
}

fun List<Char>.asString(): String {
    val sb = StringBuilder(this.size)
    this.forEach(sb::append)
    return sb.toString()
}
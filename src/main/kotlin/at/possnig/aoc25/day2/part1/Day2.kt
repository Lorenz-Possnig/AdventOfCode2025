package at.possnig.aoc25.day2.part1

import java.io.File
import java.util.regex.Pattern

fun main(args: Array<String>) {
    File("src/main/resources/day2/${args[0]}").readText()
        .split(",")
        .also { ranges ->
            ranges.asSequence()
                .flatMap { range(it) }
                .filter { it.part1() }
                .sum()
                .also { println("Part 1: $it") }
        }.also { ranges ->
            ranges.asSequence()
                .flatMap { range(it) }
                .filter { it.part2() }
                .sum()
                .also { println("Part 2: $it") }
        }
}

fun Long.part1(): Boolean =
    this.toString().let { it.length % 2 == 0 && it.substring(0, it.length / 2) == it.substring(it.length / 2) }

fun Long.part2(): Boolean = this.toString().let {
    1.rangeTo((it.length / 2) + 1).any { i ->
        "^(${it.substring(0, i)}){2,}$".let(Pattern::compile).matcher(it).matches()
    }
}

fun range(range: String): Sequence<Long> =
    range.split("-").let { it[0].toLong().rangeTo(it[1].toLong()) }.asSequence()
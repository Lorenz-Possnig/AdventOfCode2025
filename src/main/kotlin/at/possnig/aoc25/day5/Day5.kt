package at.possnig.aoc25.day5

import java.io.File
import kotlin.math.max

fun main(args: Array<String>) {
    val lines = File("src/main/resources/day5/${args[0]}").useLines { it.toList() }
    val idRanges = lines.takeWhile { it.isNotBlank() }
        .map { Range(it) }
    val ingredientIds = lines.dropWhile { it.isNotBlank() }.drop(1).map { it.toLong() }
    ingredientIds.count { ingredientId -> idRanges.any { it.contains(ingredientId) } }
        .also { println("Part 1: $it") }
    Range.mergeRanges(idRanges).sumOf { it.size() }
        .also { println("Part 2: $it") }
}

private class Range {

    companion object {
        fun mergeRanges(idRanges: Collection<Range>): Set<Range> =
            idRanges.sortedBy { it.begin }.let {
                val result = mutableSetOf<Range>()
                for (i in it.indices) {
                    val start = it[i].begin
                    var end = it[i].end
                    if (result.size > 0 && result.last().end >= end) continue
                    for (j in (i + 1)..<it.size) {
                        if (it[j].begin <= end) {
                            end = max(end, it[j].end)
                        }
                    }
                    result.add(Range(start, end))
                }
                result
            }
    }

    constructor(str: String) {
        val split = str.split("-")
        begin = split[0].toLong()
        end = split[1].toLong()
    }

    constructor(begin: Long, end: Long) {
        this.begin = begin
        this.end = end
    }

    val begin: Long
    val end: Long

    fun contains(long: Long) = long in begin..end

    fun size() = end - begin + 1

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Range

        if (begin != other.begin) return false
        if (end != other.end) return false

        return true
    }

    override fun hashCode(): Int {
        var result = begin.hashCode()
        result = 31 * result + end.hashCode()
        return result
    }
}
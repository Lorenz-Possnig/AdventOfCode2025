package at.possnig.aoc25.day3

import java.io.File
import java.math.BigInteger

fun main(args: Array<String>) {
    File("src/main/resources/day3/${args[0]}").useLines { it.toList() }
        .also { println("Part1: ${Day3.part1(it)}") }
        .also { println("Part2: ${Day3.part2(it)}") }
        .also { println("Extra Credit: ${Day3.extraCredit(it)}") }
}

object Day3 {
    fun part1(batteryBanks: List<String>) = solvePart(batteryBanks, 2)

    fun part2(batteryBanks: List<String>) = solvePart(batteryBanks, 12)

    fun extraCredit(batteryBanks: List<String>) = solvePart(batteryBanks, 50)

    private fun solvePart(batteryBanks: List<String>, amountOfBatteries: Int): BigInteger {
        var line = 0
        return batteryBanks.sumOf { batteries ->
            findMaxJoltage(batteries, amountOfBatteries)
        }
    }

    private fun findMaxJoltage(batteries: String, amount: Int) =
        findMaxJoltageMemo(batteries, amount, HashMap(200 * 100))

    private fun findMaxJoltageMemo(batteries: String, amount: Int, cache: MutableMap<Key, BigInteger>): BigInteger {
        val key = Key(batteries, amount)
        var result = cache[key]
        if (result != null) return result
        if (amount == 0) return BigInteger.ZERO
        if (batteries.length == amount)
            return batteries.toBigInteger()
        val s = batteries.substring(1)
        val i = amount - 1
        val a = BigInteger.TEN.pow(i).times(batteries[0].digitToInt().toBigInteger()).plus(findMaxJoltageMemo(s, i, cache))
        val b = findMaxJoltageMemo(s, amount, cache)
        result = if (a > b) a else b
        cache[key] = result
        return result
    }

    private data class Key(val a: String, val b: Int)
}
package day7

import java.io.File

fun main(args: Array<String>) {
    val inputFile = "src/main/resources/day7/${args[0]}";
    var matrix = File(inputFile).useLines { it.toList() }
        .map { it.toCharArray() }.toTypedArray()
    val entryPoint = matrix[0].indexOf('S')
    part1(matrix, 1, entryPoint, 0).also {
        println("Part 1: $it")
    }
    matrix = File(inputFile).useLines { it.toList() }
        .map { it.toCharArray() }.toTypedArray()
    part2(matrix, 1, entryPoint, 0, mutableMapOf()).also {
        println("Part 2: ${it + 1}")
    }
}

fun part1(matrix: Array<CharArray>, i: Int, j: Int, acc: Int): Int {
    if (i == matrix.size) {
        return acc
    }
    if (j < 0 || j > matrix[0].size) {
        return 0
    }
    if (matrix[i][j] == '^') {
        return 1 + part1(matrix, i, j - 1, acc) + part1(matrix, i, j + 1, acc)
    } else if (matrix[i][j] == '|') {
        return 0
    } else {
        matrix[i][j] = '|'
        return part1(matrix, i + 1, j, acc)
    }
}

fun part2(matrix: Array<CharArray>, i: Int, j: Int, acc: Long, cache: MutableMap<Key, Long>): Long {
    val key = Key(i, j)
    var result = cache[key]
    if (result != null) return result
    if (i == matrix.size) {
        cache[key] = acc
        return acc
    }
    if (j < 0 || j > matrix[0].size) {
        cache[key] = 0
        return 0
    }
    result = if (matrix[i][j] == '^') {
        1 + part2(matrix, i, j - 1, acc, cache) + part2(matrix, i, j + 1, acc, cache)
    } else {
        part2(matrix, i + 1, j, acc, cache)
    }
    cache[key] = result
    return result
}

data class Key(val a: Int, val b: Int)
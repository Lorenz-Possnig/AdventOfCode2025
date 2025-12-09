package at.possnig.aoc25.day8

import java.io.File
import java.util.TreeSet
import kotlin.math.pow
import kotlin.math.sqrt

fun main(args: Array<String>) {
    val inputFile = "src/main/resources/day8/${args[0]}"
    val numConnections = if (inputFile.endsWith("demo")) 10 else 1000
    File(inputFile).useLines { lines ->
        val points = lines.map { it.split(",")
            .map { str -> str.toInt() }
            .let { ints -> Point(ints[0], ints[1], ints[2]) }
        }.toList()
        val distances = TreeSet<PointPair>()
        for(i in points.indices) {
            for (j in (i + 1)..<points.size) {
                distances.add(PointPair(points[i], points[j]))
            }
        }
        val circuits = mutableMapOf<Point, Int>()
        var connections = 0
        for (distance in distances) {
            val head1 = distance.p.findHead()
            val size1 = circuits[head1]
            val head2 = distance.q.findHead()
            val size2 = circuits[head2]
            if (size1 == null && size2 == null) {
                // new circuit
                distance.q.head = distance.p
                circuits[distance.p] = 2
            } else if (size1 != null && size2 == null) {
                // add 2 to circuit of 1
                distance.q.head = head1
                circuits[head1!!] = size1 + 1
            } else if (size1 == null && size2 != null) {
                // add 1 to circuit of 2
                distance.p.head = head2
                circuits[head2!!] = size2 + 1
            } else if (head1 != head2) {
                // merge circuits
                head2!!.head = head1
                circuits.remove(head2)
                circuits[head1!!] = size1!! + size2!!
            } else {
                // last case: head1 == head2 -> do nothing
            }
            if (++connections == numConnections) {
                circuits.values.sortedByDescending { it }
                    .take(3)
                    .fold(1, Int::times)
                    .also { println("Part 1: $it") }
            }
            if (circuits.size == 1 && circuits.containsValue(points.size)) {
                val result = distance.p.x.toLong() * distance.q.x.toLong()
                println("Part 2: $result")
                break
            }
        }
    }
}

class Point(val x: Int, val y: Int, val z: Int) {

    var head: Point? = null

    fun findHead(): Point? {
        var candidate: Point? = this
        while (candidate?.head != null) {
            candidate = candidate.head
        }
        return candidate
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Point) return false

        if (x != other.x) return false
        if (y != other.y) return false
        if (z != other.z) return false

        return true
    }

    override fun hashCode(): Int {
        var result = x
        result = 31 * result + y
        result = 31 * result + z
        return result
    }
}

data class PointPair(val p: Point, val q: Point): Comparable<PointPair> {
    private var euclid: Double? = null

    fun euclid(): Double {
        synchronized(this) {
            if (euclid == null) {
                euclid =
                    sqrt((p.x.toDouble() - q.x).pow(2) + (p.y.toDouble() - q.y).pow(2) + (p.z.toDouble() - q.z).pow(2))
            }
            return euclid!!
        }
    }

    fun contains(point: Point): Boolean = point == this.p || point == this.q

    override fun compareTo(other: PointPair): Int =
        this.euclid().compareTo(other.euclid())
}
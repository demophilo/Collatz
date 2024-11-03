module Collatz_julia

export collatz_operator, collatz_sequence_length

function collatz_operator(zahl::UInt128)::UInt128
	n = 0
	while (zahl & 1) == 0
		n += 1
		zahl >>= 1
	end
	return ((zahl << 1) + zahl + 1) << n
end

function collatz_sequence_length(n::UInt128)
    m::UInt128 = n
    count = 0

    while m != 1
		count = count + (m & 1)
        m = (m & 1 != 0) * ((m << 1) + m + 1) + (m >> 1) * (m & 1 == 0)
    end

    return count
end
end # module Collatz_julia

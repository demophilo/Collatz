module Collatz_julia

export collatz_operator, collatz_sequence_length, max_sequence_length_in_given_collatz_length

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

function max_sequence_length_in_given_collatz_length(collatz_length)
    longest_sequence_number1 = []
    longest_sequence_number2 = []
    longest_sequence = 0
    lower_limit::UInt128 = 2 << (collatz_length - 2) + 1
    upper_limit::UInt128 = 2 << (collatz_length - 1) - 1
    for i::UInt128 in lower_limit:2:upper_limit
        sequence_length = collatz_sequence_length(i)
        if sequence_length > longest_sequence
            longest_sequence = sequence_length
            longest_sequence_number1 = [i, sequence_length]
            longest_sequence_number2 = [0,0];
        elseif sequence_length == longest_sequence
            longest_sequence_number2 = [i, sequence_length]
        end
    end
    return (longest_sequence_number1, longest_sequence_number2)
end
end # module Collatz_julia
#=
using .Collatz_julia


@btime max_sequence_length_in_given_collatz_length(27)
=#
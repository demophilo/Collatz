#=
Collatz:
- Julia version: 1.85
- Author: karl
- Date: 2023-04-01
=#


function collatz_sequence_length(n::Int)
    count = 0
    while n != 1
        if n & 1 != 0
            n = 3 * n + 1
            count += 1
        else
            n >>= 1
        end
    end
    return count
end

function max_sequence_length_in_given_collatz_length(binary_digits)
    longest_sequence_number1 = 0
    longest_sequence_number2 = 0
    longest_sequence = 0
    lower_limit = 2 << (binary_digits - 2) + 1
    upper_limit = 2 << (binary_digits - 1) - 1
    for i in lower_limit:2:upper_limit
        sequence_length = collatz_sequence_length(i)
        if sequence_length > longest_sequence
            longest_sequence = sequence_length
            longest_sequence_number1 = i
            longest_sequence_number2 = 0;
        elseif sequence_length == longest_sequence
            longest_sequence_number2 = i
        end
    end
    return (longest_sequence_number1, longest_sequence_number2)
end

maxDigit = 34



for i in 2:maxDigit
    println(i," ", max_sequence_length_in_given_collatz_length(i))
end


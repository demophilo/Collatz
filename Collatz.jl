#=
Collatz:
- Julia version: 1.85
- Author: karl
- Date: 2023-04-01
=#






function max_sequence_length_in_given_collatz_length(binary_digits)
    longest_sequence_number1 = []
    longest_sequence_number2 = []
    longest_sequence = 0
    lower_limit::Int128 = 2 << (binary_digits - 2) + 1
    upper_limit::Int128 = 2 << (binary_digits - 1) - 1
    for i::Int128 in lower_limit:2:upper_limit
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

maxDigit = 40

println(max_sequence_length_in_given_collatz_length(41))
#=
for i in 2:maxDigit
    println(i," ", max_sequence_length_in_given_collatz_length(i))
end
=#

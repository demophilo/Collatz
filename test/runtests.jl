using Test
include("../src/Collatz_julia.jl")
using .Collatz_julia

@testset "Collatz" begin
	@test collatz_operator(UInt128(5)) == 16
	@test collatz_operator(UInt128(10)) == 32

end

@testset "collatz_sequence_length" begin
	@test collatz_sequence_length(UInt128(5)) == 1
	@test collatz_sequence_length(UInt128(10)) == 1
	@test collatz_sequence_length(UInt128(3)) == 2
end


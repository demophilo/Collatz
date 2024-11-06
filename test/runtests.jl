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

@testset "max_sequence_length_in_given_collatz_length" begin
    @test max_sequence_length_in_given_collatz_length(2) == ([3, 2], [0, 0])
    @test max_sequence_length_in_given_collatz_length(8) == ([231, 46], [235, 46])
end

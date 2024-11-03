module Collatz_julia

export collatz_operator

function collatz_operator(zahl::UInt128)::UInt128
	n = 0
	while (zahl & 1) == 0
		n += 1
		zahl >>= 1
	end
	return ((zahl << 1) + zahl + 1) << n
end

end # module Collatz_julia

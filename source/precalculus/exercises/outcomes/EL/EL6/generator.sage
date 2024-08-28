class Generator(BaseGenerator):
  def data(self):
    xs = [var(l) for l in sample("abcdkmnwxyz", 4)]
    bases = [ZZ(n) for n in sample(range(2,6), 2)]
    nums = [ZZ(n) for n in sample(range(2,10), 4)]
    d,d2 = sample(range(2,4),2)
    # b^(x-a)=c => x = log_b(c)+a
    eqs = [{
      "var": xs[0],
      "eq": bases[0]^(x-nums[0]) == nums[1],
      "sol": f"\\log_ { {bases[0]} }({nums[1]})+{nums[0]}"
    }]
    # b^x - a = c => x = log_b(c+a)
    eqs += [{
      "var": xs[0],
      "eq": bases[0]^x-nums[0] == nums[1],
      "sol": f"\\log_ { {bases[0]} }({nums[1]+nums[0]})"
    }]
    # a log_b(cx) = ad => b^d/c
    eqs += [{
      "var": xs[1],
      "eq": f"{nums[2]}\\log_ { {bases[1]} }({nums[3]}{xs[1]}) = {nums[2]*d}",
      "sol": bases[1]^d/nums[3]
    }]
    # a + log_b(cx) = d2+a => b^d2/c
    eqs += [{
      "var": xs[1],
      "eq": f"{nums[2]} + \\log_ { {bases[1]} }({nums[3]}{xs[1]}) = {nums[2]+d2}",
      "sol": bases[1]^d2/nums[3]
    }]
    # shuffle a bit
    if choice([True, False]):
      eqs[:2], eqs[2:] = eqs[2:], eqs[:2]
    if choice([True, False]):
      eqs[0], eqs[1] = eqs[1], eqs[0]
    if choice([True, False]):
      eqs[2], eqs[3] = eqs[3], eqs[2]
    return { "eqs": eqs }
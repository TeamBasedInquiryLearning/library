class Generator(BaseGenerator):
    def data(self):
      terms = [var(l) for l in sample("abcdkmnstwxyz", 6)]
      powers = [ZZ(n)*choice([-1,1]) for n in sample(range(2,8), 6)]
      bases = [ZZ(n) for n in sample(range(2,10), 2)]
      expand_term = prod(terms[i]^powers[i] for i in range(3))
      condensed_term = prod(terms[i]^powers[i] for i in range(3,6))
      def expanded_string(b, ts, ps):
        result = f"{ps[0]}"
        result += f"\\log_{ {b} }( {ts[0]} )"
        if ps[1] > 0:
          result += " + "
        result += f"{ps[1]}"
        result += f"\\log_{ {b} }( {ts[1]} )"
        if ps[2] > 0:
          result += " + "
        result += f"{ps[2]}"
        result += f"\\log_{ {b} }( {ts[2]} )"
        return result
      return {
        "expand_term": expand_term,
        "expand_base": bases[0],
        "expanded": expanded_string(bases[0], terms[:3], powers[:3]),
        "condense": expanded_string(bases[1], terms[3:], powers[3:]),
        "condense_base": bases[1],
        "condensed_term": condensed_term,
      } 
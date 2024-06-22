class Generator(BaseGenerator):
    def data(self):
      x=var("x")
      # INFINITE LIMITS
      #################
      # Generate 4 zeros to use in rational functions
      zeros = list(IntegerRange(-6,0))+list(IntegerRange(1,7))
      shuffle(zeros)
      # Generate a list of small nonzero powers
      biggest_power = randrange(3,7)
      smaller_powers = list(range(1,biggest_power))
      # Construct numerator and denominator with no shared zero
      top3 = (x-zeros[0])^choice(smaller_powers) * (x-zeros[1])^choice(smaller_powers)
      bottom3 = (x-zeros[2])^choice(smaller_powers) * (x-zeros[3])^choice(smaller_powers)
      f3 = top3 / bottom3
      # Evaluate the limit at one of the bottom zeros
      a3 = choice([zeros[2],zeros[3]])
      # Calculuate left- and right-hand limits
      limleftf3 = limit(f3, x=a3, dir='-')
      limrightf3 = limit(f3, x=a3, dir='+')
      same_limits = bool(limleftf3==limrightf3)

      limitsonesided = [
          {
            "f":f3,
            "a":a3,
            "limitleft":limleftf3,
            "limitright":limrightf3,
            "same_limits": same_limits,
          },
      ]

      return {
        "limitsonesided": limitsonesided,
      }
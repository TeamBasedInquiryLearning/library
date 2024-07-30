class Generator(BaseGenerator):
    def data(self):
      x=var("x")

      # Rational Function Factored
      ############################
      ### Generate 3 zeros to use in polynomials
      zeros = sample([Integer(i) for i in range(-6, 7) if i != 0], 3)
      ## Construct numerator and denominator with a shared zero
      top1 = expand((x-zeros[0]) * (x-zeros[1]))
      bottom1 = expand((x-zeros[1]) * (x-zeros[2]))
      ## Evaluate the limit at the shared zero
      a1 = zeros[1]
      limf1 = limit(top1/bottom1, x=a1)


      # Plug in the Number
      ####################
      ## 2 zeros on top, 2 zeros on bottom, 5th is where we evaluate the limit
      zeros = sample([i for i in range(-6, 7) if i != 0], 5)
      ## Construct numerator and denominator, no shared zeros
      top2 = expand((x-zeros[0]) * (x-zeros[1]))
      bottom2 = expand((x-zeros[2]) * (x-zeros[3]))
      ## Evaluate somewhere else
      a2 = zeros[4]
      limf2 = limit(top2/bottom2, x=a2)

      # Rationalize
      #############
      ## Choose some values to use that will make this not terrible
      value = choice(range(1,10))
      square = choice(range(1,7))^2
      ## Create numerator and denominator
      exp1 = sqrt(x+square-value) - sqrt(square)
      exp2 = x - value
      ## Shuffle them
      fraction = [exp1, exp2]
      shuffle(fraction)
      ## Construct top and bottom
      top3 = fraction[0]
      bottom3 = fraction[1]
      ## Evaluate at the zero
      a3 = value
      limf3 = limit(top3/bottom3, x=a3)

      # Common Denominator
      ####################
      values = sample([i for i in range(-6, 7) if i != 0], 2)
      frac = 1/values[0]
      top4 = 1/(x - values[1] + values[0]) - frac
      bottom4 = x - values[1]
      a4 = values[1]
      limf4 = limit(top4/bottom4, x=a4)

      limits = [
          {"num":top1,"den":bottom1,"a":a1,"limit":limf1},
          {"num":top2,"den":bottom2,"a":a2,"limit":limf2},
          {"num":top3,"den":bottom3,"a":a3,"limit":limf3},
          {"num":top4,"den":bottom4,"a":a4,"limit":limf4},
      ]

      # remove either ratoinalize (2) or common denominator (3)
      removed = choice([2,3])
      limits.pop(removed)

      shuffle(limits)

      return {
        "limits": limits,
      }
load("../../common/sagemath/checkit.sage")
load("../../common/sagemath/doenet.sage")
load("./outcomes/LE/LE1/generator.sage")

generator = Generator()

def doenet_option():
    generator.roll_data()
    data = generator.get_data()
    return f"""
        <m name="equation">{" ".join(latex(data["vectorequation"]).split())}</m>
        <matrix name="matrix">{doenet_matrix(data["matrix"])}</matrix>
    """

result = "<select name='checkit'>\n"
for _ in range(1_000):
    result += doenet_option()


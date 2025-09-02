from lexer import Lexer, TokenType
from parser import Parser
from t2c import ASTtoC

# Example source code
code = """
fn main() {
    #Variable declarations
    int x = 42
    float y = 3.14
    bool flag = true
    string msg = "Hello, ToyLang!"

    #Printing initial values
    print(x)
    print(y)
    print(flag)
    print(msg)

    # Arithmetic operations
    int sum = x + 10
    float product = y * 2.0

    print(sum)
    print(product)

    # Boolean comparison
    bool isPositive = sum > 0
    print(isPositive)

    # String concatenation (ToyLang style)
    string greeting = msg + " Welcome!"
    print(greeting)

    # Example conditional (for future parsing)
    if (sum > 50) {
        print("Sum is large!")
    } else {
        print("Sum is small!")
    }

    # Example while loop (for future parsing)
    int counter = 0
    while (counter < 5) {
        print(counter)
        counter = counter + 1
    }
}
"""

# -------------------- Lexing --------------------
lexer = Lexer(code)
tokens = []
tok = lexer.next_token()
while tok.type != TokenType.END:
    tokens.append(tok)
    # print(f"Token: {tok.type}, Text: '{tok.text}'")  # Debug print
    tok = lexer.next_token()

# -------------------- Parsing --------------------
parser = Parser(tokens)
func = parser.parse_function()

# -------------------- AST to C --------------------
# assuming your class is in ast_to_c.py
compiler = ASTtoC()
compiler.function(func)

# Print generated C code
print(compiler.code)

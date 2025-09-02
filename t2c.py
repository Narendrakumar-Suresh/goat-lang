from parser import *


class ASTtoC:
    def __init__(self):
        self.code = ""
        self.indent_level = 0
        self.var_types = {}  # keep track of variable types

    def indent(self):
        return "    " * self.indent_level

    def emit_line(self, line):
        self.code += f"{self.indent()}{line}\n"

    # ---------------- Expressions ----------------
    def expr(self, node):
        if isinstance(node, NumberExpr):
            return str(node.value)
        elif isinstance(node, FloatExpr):
            return str(node.value)
        elif isinstance(node, BoolExpr):
            return "1" if node.value else "0"
        elif isinstance(node, StringExpr):
            return f'"{node.value}"'
        elif isinstance(node, VariableExpr):
            return node.name
        elif isinstance(node, BinaryExpr):
            lhs = self.expr(node.lhs)
            rhs = self.expr(node.rhs)
            return f"({lhs} {node.op} {rhs})"
        else:
            raise NotImplementedError(f"Unknown expr: {node}")

    # ---------------- Statements ----------------
    def stmt(self, node):
        if isinstance(node, LetStmt):
            # Map language types to C types
            ctype = {
                "int": "int",
                "float": "float",
                "bool": "int",  # or _Bool
                "string": "char*",
            }.get(node.type, "int")  # default to int if unknown

            val = self.expr(node.value)
            self.emit_line(f"{ctype} {node.name} = {val};")
            self.var_types[node.name] = node.type  # store type

        elif isinstance(node, PrintStmt):
            val = self.expr(node.value)

            # Determine printf format
            if isinstance(node.value, (NumberExpr, BoolExpr)):
                fmt = "%d"
            elif isinstance(node.value, FloatExpr):
                fmt = "%f"
            elif isinstance(node.value, StringExpr):
                fmt = "%s"
            elif isinstance(node.value, VariableExpr):
                t = self.var_types.get(node.value.name, "int")
                fmt = {"int": "%d", "float": "%f", "bool": "%d", "string": "%s"}.get(
                    t, "%d"
                )
            else:
                fmt = "%d"  # fallback

            self.emit_line(f'printf("{fmt}\\n", {val});')

        elif isinstance(node, IfStmt):
            cond = self.expr(node.condition)
            self.emit_line(f"if ({cond}) {{")
            self.indent_level += 1
            for s in node.then_body:
                self.stmt(s)
            self.indent_level -= 1
            self.emit_line("}")
            if node.else_body:
                self.emit_line("else {")
                self.indent_level += 1
                for s in node.else_body:
                    self.stmt(s)
                self.indent_level -= 1
                self.emit_line("}")

        elif isinstance(node, WhileStmt):
            cond = self.expr(node.condition)
            self.emit_line(f"while ({cond}) {{")
            self.indent_level += 1
            for s in node.body:
                self.stmt(s)
            self.indent_level -= 1
            self.emit_line("}")

        elif isinstance(node, ExprStmt):
            val = self.expr(node.expr)
            self.emit_line(f"{val};")  # just evaluate the expression

        else:
            raise NotImplementedError(f"Unknown stmt type: {node}")

    # ---------------- Function ----------------
    def function(self, node: FunctionStmt):
        self.emit_line("#include <stdio.h>")
        self.emit_line("")
        self.emit_line("int main() {")
        self.indent_level += 1
        for s in node.body:
            self.stmt(s)
        self.emit_line("return 0;")
        self.indent_level -= 1
        self.emit_line("}")

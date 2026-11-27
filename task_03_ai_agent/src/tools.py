
import ast
import operator


def calculator(expression):
    """
    Safely perform basic mathematical calculations.
    """

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
    }

    def evaluate(node):

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value

        elif isinstance(node, ast.BinOp):
            operation = allowed_operators.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operation.")

            left = evaluate(node.left)
            right = evaluate(node.right)

            return operation(left, right)

        elif isinstance(node, ast.UnaryOp):
            operation = allowed_operators.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operation.")

            return operation(evaluate(node.operand))

        raise ValueError("Invalid mathematical expression.")

    try:
        parsed_expression = ast.parse(expression, mode="eval")
        result = evaluate(parsed_expression.body)

        return f"Calculation result: {result}"

    except Exception as error:
        return f"Calculation error: {error}"


if __name__ == "__main__":

    print(calculator("25 + 15"))
    print(calculator("10 * 5"))
    print(calculator("100 / 4"))
    print(calculator("2 ** 3"))


def read_file():

    from pathlib import Path

    file_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "sample.txt"
    )

    content = file_path.read_text(encoding="utf-8")

    return content


from ddgs import DDGS


def web_search(query):

    try:
        with DDGS() as search:

            results = search.text(
                query,
                max_results=5
            )

            if not results:
                return "No search results found."

            formatted_results = []

            for result in results:

                title = result.get("title", "")
                body = result.get("body", "")
                link = result.get("href", "")

                formatted_results.append(
                    f"Title: {title}\n"
                    f"Information: {body}\n"
                    f"Link: {link}"
                )

            return "\n\n".join(formatted_results)

    except Exception as error:
        return f"Search error: {error}"


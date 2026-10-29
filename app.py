from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>ABC Technologies Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            text-align: center;
            padding-top: 60px;
        }
        .calculator {
            background: white;
            width: 320px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px #cccccc;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        .result {
            font-size: 20px;
            color: green;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>ABC Technologies</h2>
        <h3>Simple Calculator</h3>

        <form method="POST">
            <input type="number" step="any" name="num1"
                   placeholder="Enter first number" required>

            <select name="operation">
                <option value="add">Addition (+)</option>
                <option value="subtract">Subtraction (-)</option>
                <option value="multiply">Multiplication (*)</option>
                <option value="divide">Division (/)</option>
            </select>

            <input type="number" step="any" name="num2"
                   placeholder="Enter second number" required>

            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <p class="result">Result: {{ result }}</p>
        {% endif %}

        {% if error %}
            <p style="color:red">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                error = "Cannot divide by zero!"
            else:
                result = num1 / num2

    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)

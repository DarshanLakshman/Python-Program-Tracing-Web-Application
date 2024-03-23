from flask import Flask, render_template, request, jsonify, send_file
import pytracertool.pytracertool as tracer
import errors
import traceback
import io
import sys

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(exitCode=-1, error=f"Unexpected: \n\tINTERNAL SERVER ERROR: \n\t\t{error.description}\n\t\tThe code entered cannot be processed. Sorry!"), 500


@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("index.html")


@app.route("/information", methods=["GET", "POST"])
def information():
    return render_template("information.html")


@app.route("/documentation", methods=["GET", "POST"])
def documentation():
    return render_template("documentation_display.html")


@app.route("/top_to_bottom_veiw", methods=["GET", "POST"])
def top_to_bottom_veiw():
    return render_template("index2.html")


@app.route("/generate_trace", methods=["GET", "POST"])
def generate_trace():
    if request.method == "POST":
        data = request.json
        
        #print(data)
        code = data.get("code")
        inputs = data.get("user_inputs")
        
        try:
            if code.strip().replace("\n", "") == "":
                raise errors.EmptyCodeEditorError()

            if "import " in code:
                raise errors.ImportStatementError()

            #if "input(" in code:
                #raise errors.InputFunctionError()

            input_stream = io.StringIO(inputs)
            sys.stdin = input_stream

            exec(code)
            #sys.stdin = sys.__stdin__

        except Exception as err:
            traceback_str = traceback.format_exc()
            return jsonify(
                exitCode=-1, error=f" Unexpected: The following exception occured:\n\t {traceback_str}"
            )

        try:

            #print("Received code:", code)
            userCode = tracer.CodeTracer(code,inputs)
            userCode.generate_trace_table()
            #print(userCode.execution_order)
            return jsonify(
                exitCode=0,
                traceTable=(userCode.trace_table),
                executionOrder=(userCode.execution_order),
            )
        except Exception as err:
            traceback_str = traceback.format_exc()
            return internal_server_error(traceback_str)


@app.route("/download_pyTracer_module")
def download_python_file():
    file_path = "pyTracer.py"
    return send_file(file_path, as_attachment=True)


#if __name__ == '__main__':
    #app.run()


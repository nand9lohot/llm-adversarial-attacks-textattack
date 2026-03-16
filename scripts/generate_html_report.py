import pandas as pd
import glob
import os
from difflib import ndiff

REPORT_DIR = "reports"
OUTPUT_FILE = "reports/attack_report.html"

def highlight_diff(original, adversarial):

    if not isinstance(original, str) or not isinstance(adversarial, str):
        return ""

    diff = list(ndiff(original.split(), adversarial.split()))

    highlighted = []

    for token in diff:

        if token.startswith("- "):
            highlighted.append(f"<span style='color:red'>{token[2:]}</span>")

        elif token.startswith("+ "):
            highlighted.append(f"<span style='color:green'>{token[2:]}</span>")

        elif token.startswith("  "):
            highlighted.append(token[2:])

    return " ".join(highlighted)

def load_results():

    csv_files = glob.glob(f"{REPORT_DIR}/*_results.csv")

    if not csv_files:
        print("No CSV reports found.")
        return pd.DataFrame()

    frames = []

    for file in csv_files:

        df = pd.read_csv(file)

        attack_name = os.path.basename(file).replace("_results.csv", "")

        df["attack"] = attack_name

        frames.append(df)

    return pd.concat(frames, ignore_index=True)

def generate_html(df):

    rows = []

    for _, row in df.iterrows():

        original = row.get("original_text", "")
        adversarial = row.get("perturbed_text", "")

        diff = highlight_diff(original, adversarial)

        rows.append(f"""
        <tr>
        <td>{row.get("attack","")}</td>
        <td>{original}</td>
        <td>{adversarial}</td>
        <td>{diff}</td>
        </tr>
        """)

    html = f"""
    <html>
    <head>
        <title>LLM Adversarial Attack Report</title>
        <style>
            body {{ font-family: Arial; margin:40px; }}
            table {{ border-collapse: collapse; width:100%; }}
            th,td {{ border:1px solid #ddd; padding:8px; }}
            th {{ background:#f2f2f2 }}
        </style>
    </head>

    <body>

    <h1>LLM Adversarial Attack Evaluation</h1>

    <table>
        <tr>
            <th>Attack</th>
            <th>Original Text</th>
            <th>Adversarial Text</th>
            <th>Token Differences</th>
        </tr>

        {''.join(rows)}

    </table>

    </body>
    </html>
    """

    with open(OUTPUT_FILE, "w") as f:
        f.write(html)

    print("HTML report generated:", OUTPUT_FILE)

def main():

    df = load_results()

    if df.empty:
        return

    generate_html(df)

if __name__ == "__main__":
    main()
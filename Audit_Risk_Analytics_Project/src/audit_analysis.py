
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_path = ROOT / "data" / "transactions.csv"
output_path = ROOT / "outputs"
output_path.mkdir(exist_ok=True)

df = pd.read_csv(data_path, parse_dates=["transaction_date"])

# Data quality checks
quality = pd.DataFrame({
    "check": [
        "Total transactions",
        "Missing values",
        "Duplicate vendor-date-amount combinations"
    ],
    "result": [
        len(df),
        int(df.isna().sum().sum()),
        int(df.duplicated(["vendor_id", "transaction_date", "amount"]).sum())
    ]
})
quality.to_csv(output_path / "data_quality_summary.csv", index=False)

# Rule-based audit tests
df["high_value_flag"] = df["amount"] > 100000
df["approval_exception_flag"] = df["approved"].eq("No")
df["duplicate_flag"] = df.duplicated(["vendor_id", "transaction_date", "amount"], keep=False)

df["risk_score"] = (
    df["high_value_flag"].astype(int) * 3
    + df["approval_exception_flag"].astype(int) * 3
    + df["duplicate_flag"].astype(int) * 2
)

df["risk_level"] = pd.cut(
    df["risk_score"],
    bins=[-1, 0, 2, 10],
    labels=["Low", "Medium", "High"]
)

exceptions = df[df["risk_score"] > 0].sort_values(
    ["risk_score", "amount"], ascending=[False, False]
)
exceptions.to_csv(output_path / "audit_exceptions.csv", index=False)

summary = pd.DataFrame({
    "metric": [
        "Total Transactions",
        "Total Transaction Value",
        "High Value Transactions",
        "Approval Exceptions",
        "Duplicate Transactions",
        "High Risk Transactions"
    ],
    "value": [
        len(df),
        round(df["amount"].sum(), 2),
        int(df["high_value_flag"].sum()),
        int(df["approval_exception_flag"].sum()),
        int(df["duplicate_flag"].sum()),
        int((df["risk_level"] == "High").sum())
    ]
})
summary.to_csv(output_path / "audit_summary.csv", index=False)

print("Audit analytics completed.")
print(summary.to_string(index=False))

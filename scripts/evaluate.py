import requests
import pandas as pd
import numpy as np

if __name__ == "__main__":

  df = pd.read_csv(
    "data/processed/test.csv"
  )

  correct = 0

  top3_correct = 0

  latencies = []

  total = 0

  for _, row in df.iterrows():

    query = row["query"]

    true_intent = str(
      row["intent"]
    ).strip().lower()

    try:

      res = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
          "query": query
        }
      )

      if res.status_code != 200:

        print(
          "API error:",
          res.text
        )

        continue


      data = res.json()


      pred = str(
        data.get(
          "intent",
          ""
        )
      ).strip().lower()


      lat = float(
        data.get(
          "latency_ms",
          0
        ) or 0
      )


      top_k = data.get(
        "top_k",
        [pred]
      )


      top_k_clean = [

        str(x)
        .strip()
        .lower()

        for x in top_k[:3]
      ]


      latencies.append(lat)

      total += 1


      if pred == true_intent:
        correct += 1


      if true_intent in top_k_clean:
        top3_correct += 1


    except Exception as e:

      print(
        "Error:",
        e
      )

      continue


  if total == 0:

    print(
      "No valid predictions"
    )

  else:

    acc = correct / total

    top3_acc = (
      top3_correct / total
    )

    latencies = np.array(
      latencies
    )

    print()

    print(
      "===== RESULTS ====="
    )

    print(
      "Samples:",
      total
    )

    print(
      "Accuracy (Top-1):",
      round(acc, 3)
    )

    print(
      "Accuracy (Top-3):",
      round(top3_acc, 3)
    )

    print()

    print("Latency:")

    print(
      "Avg:",
      round(
        latencies.mean(),
        2
      ),
      "ms"
    )

    print(
      "P95:",
      round(
        np.percentile(
          latencies,
          95
        ),
        2
      ),
      "ms"
    )

    print(
      "Max:",
      round(
        latencies.max(),
        2
      ),
      "ms"
    )
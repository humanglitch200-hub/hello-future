lines = ["My candle burns at both ends;",
          "It will not last the night;",
            "But ah, my foes, and oh, my friends —", 
            "It gives a lovely light."]

for line in lines:
    if line.strip().endswith(('.', '!', '?','—',';')):
        print(line)


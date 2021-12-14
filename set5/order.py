def sort(words):
  for idx, _ in enumerate(words):
    k = idx
    for i in range(k, len(words)):
      if words[k] > words[i]:
        words[k], words[i] = words[i], words[k]

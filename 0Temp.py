
# ~ # remove last indice
parts = self.name.split("-")
n = len(parts)
if (n > 1):
    last = parts[-1]
    if last.isnumeric():
        parts.pop()
self.name = "-".join(parts)
self.namedev = self.name + "-dev"

class Arxitektor:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def __call__(self):
        return f"Salom, mening ismim {self.ism} {self.familiya}"

arxitektor = Arxitektor("Ali", "Vali")
print(arxitektor())  # Salom, mening ismim Ali Vali

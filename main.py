from printer import Printer

p = Printer()

d = {
    'manu': 5,
    'elyes': 10
}

l = [1,2,3,4]

p.info(l)
p.success(l)
p.warning(l)
p.error(l)
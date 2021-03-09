from printer import Printer

p = Printer()

d = {
    'manu': 5,
    'elyes': 10
}

l = [1,2,3,4]

p.info(d, l)
p.warning(d, l)
p.success(d, l)
p.error(d, l)
#!/usr/bin/env python3
from decimal import *
import gmpy2
import operator
import functools

def gen(x):
    p = [x]
    for i in range(3):
        p.append(gmpy2.next_prime(p[i] * 2))
    return functools.reduce(operator.mul, p)

def phi(x):
    p = [x]
    for i in range(3):
        p.append(gmpy2.next_prime(p[i] * 2))
    return functools.reduce(operator.mul, [(x - 1) for x in p])

n = 0x11f06ee152896e80514c1e25dfee242af26a39cf5af2bdd53d9c45f9b8fa08c5bfc91d136cfb82dd9861e2535d8b025d2d3b46953538d3743a74df8695f1a45297bd5780618a42a42ed99689c751fd54a6efed31630efe72987a36cf640562c968ca401c9609b4b3f32739190b771ba0c715977fad267d887a6b8e792df92a4b4ebac4621c4d634101443ae1a8d230796d681cd27ca29f226f8b53383b3549eb737520e847aaca52d27af39a8898234978405c0cf460be1a6e49e8413a500d28a204d8da71c1d78913a40fd9b27ea437a724ba4ca06d0169df6add6a0d3f2b7582d35f569501a2e7f85e3226ae95d20466991917cf2a14e853981f72a9543f1858c276bee00045b88e0629d124b363128396ab6da1f7397ffc754ea6dde7a52eb528a19c9ce193c4bb8c4573ed3056dde820aad45ff496770cd316e4bd8b461f12a0ac88bab4f8b840eea12de22e2a0c1530a3028e4f3e4f45e23945d0e5f1c312f4a83733e49d44ff09f307be893bbcc364c2224cfe9dccce856c81bb106bda2d2de96018836efca6fc52d87ef92fbcce57d543be4199959db7b20bf9e00f8e633fc3ba821d0d8126c997b5fa649b0dc6bff9bf0a6f1b876098585af25626536fc0d19f3fdeb240b972f2e4e4069a79c21866c3014f57aaee3fbef1871daa653ecc3c7f14141c6d653ba959fdfee1669996777b4e02e547038b65b196a134a759
e = 0x10001
c = 0x239cad80ec8202824471f659165014e0370d483000deaabec6e12475947f603bc9d10c323c268ff682a42f8792a84cceaa4a8f68a2f7488be94544f188a7c78b18c9042ae02ad0dbbe1d403c93f86a4b71a659a7d0b31e5cdd089c0474b5a64b578e9eae622ba4d8acb0be83b8bac02ad270b7c61df9295c5709800a3c3e0032e7cd1c7c56510e9a3bb195189c8d4c85fee09d458c11f36e3bd0dc31ed24346e19d2ea46330770f6bbffe0f3c8262214aab63b56e4eabe24b1fc076bd00f329a2c1992aa364e1df5fe1d3d0a51dffe79ab6098477b30fc31eb1f690903532d9c50fdec4b3c92342d4bbfe47d22bb40cff9b64e3bea0a62e45dbfd4460176d71ca76fb7c3986c2557b09bba7a7d2946bd24ae03b99ac50bc84c078847d50d81671bbc87b8d3432518acaef20eea1c88125aa95d9f81293f5095702b63f28b222ee5da87b2aa7897d7f78aecfc5a6cf242a67e01c96fe52f70755e9c7a1a580d59a7620717307a963e86a95488167c3df6e12c0aeeb455b25e42cdd51ed9cec16335c082bccc023d45574c6334561f0e84f63cbb4c2674984f2077308c2ee4dbc28cc09ac65128650b8a4ac021534cd32d0a2386d74b3c6a8f53f402216ceb877377565b50c6843583fc3fbd73d09308e4de9eede7033544c367dd11752bc462789c5649460263dddb5ad1b3166691db01ab8caaecce1c7c8e29665281f5fe46ee4

'''
l = 2
h = 130804078415138897833610869691084947661473856443629045803131362869602165686522519062799701619297686459227139180983425852486663757331378527738514310951154218257082364889097468245936435031598204321248726295582619708492131797868732818517225619154014546126935598488122556991364038167759171876098031009844219084800

while True:
    print("l =", l)
    print("h =", h)
    m = (l + h) // 2
    m = gmpy2.next_prime(m)
    x = gen(m)
    if x > n:
        h = m
    elif x < n:
        l = m
    else:
        print(x)
        break
'''

'''
l = 130804078415138895759534235462455718399081296140935703647494101757725679530815979786315995310813147536946732990432338557876774535966798775405634174317251094501903407261914552612479549772354428675322270046259683111542298768614672004781018738907544640100534100968286213927729458294566512615200632114089537601531
h = 130804078415138895759534235462455718399081296140935703647494101757725679530815979786315995310813147536946732990432338557876774535966798775405634174317251094501903407261914552612479549772354428675322270046259683111542298768614672004781018738907544640100534100968286213927729458294566512615200632114089537605833

for m in range(l, h + 1):
    print(m % 10000)
    x = gen(m)
    if x == n:
        print(m)
        break
'''

p = 130804078415138895759534235462455718399081296140935703647494101757725679530815979786315995310813147536946732990432338557876774535966798775405634174317251094501903407261914552612479549772354428675322270046259683111542298768614672004781018738907544640100534100968286213927729458294566512615200632114089537603001
r = phi(p)
d = gmpy2.invert(e, r)
m = int(pow(c, d, n))

print(m.to_bytes(50, 'big'))

a = ord("a")
z = ord("z")
A = ord("A")
print(a)
print(z)
print(A)
print(119938 - a)
end = """&#119939;&#119958;&#119957; &#119946; &#119940;&#119938;&#119951; &#119956;&#119945;&#119952;&#119960; &#119962;&#119952;&#119958;
"""

offset = 119841
s = "Try to repeat if you can"
result =""

for char in s:
    if 64 < ord(char) < 123:
        result += "&#" + str((offset +1+ ord(char))) + ";"
    else:
        result += char
print(result)

"""𝒊 𝒄𝒂𝒏'𝒕 𝒕𝒆𝒍𝒍 𝒚𝒐𝒖 how solve you problem,𝒃𝒖𝒕 𝒊 𝒄𝒂𝒏 𝒔𝒉𝒐𝒘 𝒚𝒐𝒖 one interesting video"""

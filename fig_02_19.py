# String formatting

integerValue = 4237
print("Integer ", integerValue)
print("Decimal integer %d" % integerValue)
print("Hexadecimal integer %x\n" % integerValue)

floatValue = 123456.789
print("Float", floatValue)
print("Default float %f" % floatValue)
print("Default exponecial %e\n" % floatValue)

print("Right justify integer (%8d)" % integerValue)
print("Left justify integer  (%-8d)\n" % integerValue)

stringValue = "String foormatting"
print("Force eight digits in integer %.8d" % integerValue)
print("Five digits after deciaml in float %.5f" % floatValue)
print("(%.15s) (%.5s)" % (stringValue, stringValue))

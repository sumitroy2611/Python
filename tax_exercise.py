# income = 250_000
# lowtaxland_rate = 0.05
# ripoffland_rate = 0.43

# Lowtaxland_tax = income*lowtaxland_rate
# Ripoffland_tax = income*ripoffland_rate
# Tax_diff = Lowtaxland_tax - Ripoffland_tax 

# print(f"Your income is {income} and you would pay {Lowtaxland_tax} income tax in Lowtaxland or {Ripoffland_tax} income tax in Ripoffland. You would save {Tax_diff} by paying taxes in Lowtaxland!")

printx(~32)


aws rds describe-db-instances --query 'DBInstances[*].DBInstanceArn' --db-instance-identifier  ${dbIdentifier} --output text

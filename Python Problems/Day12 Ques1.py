def domain(email):
    return email.split('@')[1].split('.com')[0]

print(domain('amit@sccilabs.com'))
print(domain('simran@iitpr.com'))
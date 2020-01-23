def add_features(data):
    data['Sales/Cust'] = data['Sales'] /  data['Customers']
    return data
    
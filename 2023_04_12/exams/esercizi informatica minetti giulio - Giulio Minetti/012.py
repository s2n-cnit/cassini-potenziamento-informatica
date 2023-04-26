def freedom_converter():
    meters = input('Input length in non-idiotic unit: ')
    print('Miglia terrestri: ' + 1609.344 * meters)
    print('Iarde: ' + 0.9144 * meters)
    print('Piedi: ' + 0.3048 * meters)
    print('Pollici: ' + 0.0254 * meters)
    
freedom_converter()
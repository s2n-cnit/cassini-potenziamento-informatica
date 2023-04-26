def freedom_converter():
    meters = float(input('Lunghezza di input in una unità a scelta: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()
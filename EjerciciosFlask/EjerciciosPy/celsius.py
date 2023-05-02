def celsius(celsius):
    try:
        celsius = int(celsius)
        fahrenheit = (celsius*1.8) + 32
        
        return f"{celsius}º Celsius son {fahrenheit}º Fahrenheit"
        
    except:
        return "Error, introduce un valor correcto"

base_html = """<html><body><p>The last measured temperature at Sam's desk was %(temperature)0.1f degrees F at %(time)s on %(date)s.</p></body></html>"""
def make_html(temperature, time, date):
    return base_html % {"temperature" : float(temperature), "time" : time, "date" : date}

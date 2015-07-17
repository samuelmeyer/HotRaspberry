
base_html = """<html>
<head>
<title>Sam's Desk Temperature</title>
</head>
<body>
<p>The last measured temperature at Sam's desk was %(temperature)0.1f degrees F at %(time)s on %(date)s.</p>
</body>
</html>"""
def make_html(temperature, time, date):
	html = base_html % {"temperature" : float(temperature), "time" : time, "date" : date}
	return html

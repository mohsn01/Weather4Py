#Analyzing weather data
#import numpy as np
import scipy.stats
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.style.use("bmh")
data = pd.read_csv("TLS-weather-data-2013.csv")
#data = csv.reader(data)
#print(data)
data = pd.read_csv("TLS-weather-data-2013.csv")
data.head()
data.columns
assert(0 < len(data) <= 365)
for index, day in data.iterrows():
    assert(day["Max TemperatureC"] >= day["Mean TemperatureC"] >= day["Min TemperatureC"])
    assert(day["Max Wind SpeedKm/h"] >= day["Mean Wind SpeedKm/h"] >= 0)
    assert(360 >= day["WindDirDegrees"] >= 0)
def FahrenheitToCelsius(F):
    return (F - 32) * 5 / 9.0
   # as a basic test, check that our Fahrenheit and Celsius scales intersect at -40
FahrenheitToCelsius(-40)
data["Min TemperatureC"].min()
plt.plot(data["Mean TemperatureC"])
plt.ylabel("Mean daily temperature (°C)");
plt.scatter(data["Max TemperatureC"], data["Mean Sea Level PressurehPa"])
scipy.stats.pearsonr(data["Max TemperatureC"], data["Mean Sea Level PressurehPa"])
plt.scatter(data["Mean TemperatureC"], data["Mean Sea Level PressurehPa"]);
scipy.stats.pearsonr(data["Mean TemperatureC"], data["Mean Sea Level PressurehPa"])
plt.scatter(data["Mean VisibilityKm"], data["Mean Sea Level PressurehPa"])
scipy.stats.pearsonr(data["Mean VisibilityKm"], data["Mean Sea Level PressurehPa"])
# this is using the plotting functionality in pandas, rather than matplotlib
data.plot(x="Mean VisibilityKm", y="Mean Wind SpeedKm/h", kind="scatter")
scipy.stats.pearsonr(data["Mean VisibilityKm"], data["Mean Wind SpeedKm/h"])
data.plot(x="Mean Sea Level PressurehPa", y="Precipitationmm", kind="scatter");
data.plot(x="Mean TemperatureC", y="Dew PointC", kind="scatter")
scipy.stats.pearsonr(data["Mean TemperatureC"], data["Dew PointC"])
# here we generate some fake "observations"
obs = scipy.stats.norm(loc=10, scale=2).rvs(1000)
scipy.stats.norm.fit(obs)
mu, sigma = scipy.stats.norm.fit(obs)
fitted = scipy.stats.norm(mu, sigma)
plt.hist(obs, bins=30, density=True, alpha=0.5);
x = numpy.linspace(obs.min(), obs.max(), 100)
plt.plot(x, fitted.pdf(x), lw=3);
wind = data["Mean Wind SpeedKm/h"]
shape, loc, scale = scipy.stats.lognorm.fit(wind, floc=0)
fitted = scipy.stats.lognorm(shape, loc, scale)
plt.hist(wind, density=True, alpha=0.5)
support = numpy.linspace(wind.min(), wind.max(), 100)
plt.plot(support, fitted.pdf(support), "r-", lw=3)
plt.title("TLS wind speed in 2013", weight="bold")
plt.xlabel("Mean wind speed (km/h)");
wind = data["Mean Wind SpeedKm/h"]
mu, sigma = scipy.stats.norm.fit(wind)
fitted = scipy.stats.norm(mu, sigma)
scipy.stats.probplot(wind, dist=fitted, plot=plt.figure().add_subplot(111))
plt.title("Normal probability plot of TLS wind speed", weight="bold")
# also run a Kolmogorov-Smirnov test to measure goodness of fit
scipy.stats.kstest(wind, "norm")
fitted = scipy.stats.lognorm(shape, loc, scale)
scipy.stats.probplot(wind, dist=fitted, plot=plt.figure().add_subplot(111))
plt.title("Lognormal probability plot of TLS wind speed", weight="bold")
scipy.stats.kstest(wind, "lognorm", (shape,loc,scale))
p0, p1, p2 = scipy.stats.weibull_min.fit(wind, floc=0)
fitted = scipy.stats.weibull_min(p0, p1, p2)
plt.hist(wind, density=True, alpha=0.5)
plt.plot(support, fitted.pdf(support), "r-", lw=2)
plt.title("Wind speed in TLS in 2013, with Weibull fit", weight="bold")
plt.xlabel("Mean wind speed (km/h)");
scipy.stats.probplot(wind, dist=fitted, plot=plt.figure().add_subplot(111))
plt.title("Weibull probability plot for TLS wind speed", weight="bold")
scipy.stats.kstest(wind, "weibull_min", args=(p0, p1, p2))


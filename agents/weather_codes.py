class WEATHERCODE:
    def get(code, result = "Unknown weather"):
        WEATHER_CODES = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Dense Drizzle",
            56: "Light Freezing Drizzle",
            57: "Dense Freezing Drizzle",
            61: "Light Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            66: "Light Freezing Rain",
            67: "Heavy Freezing Rain",
            71: "Light Snowfall",
            73: "Moderate Snowfall",
            75: "Heavy Snowfall",
            77: "Snow Grains",
            80: "Light Rain Showers",
            81: "Moderate Rain Showers",
            82: "Violent Rain Showers",
            85: "Light Snow Showers",
            86: "Heavy Snow Showers",
            95: "Slight or Moderate Thunderstorm",
            96: "Thunderstorm with Slight Hail",
            99: "Thunderstorm with Heavy Hail",
        }
        if code in WEATHER_CODES:
            result = WEATHER_CODES[code]
                
        return result